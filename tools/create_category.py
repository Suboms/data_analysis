import requests
import random
import os
import sys
import django
from faker import Faker
import time

category_url = "http://localhost:8002/product/category/"


fake = Faker()
CATEGORIES = ["ACESSORIES", "CLOTHES", "HOUSEHOLD ITEMS", "BOOKS", "TOOLS"]
DJANGO_PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "data_analysis.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_analysis.settings")
django.setup()
from dataset.models import *


def random_category():
    category_data = {"name": fake.job()}

    name = category_data["name"]
    while ProductCategories.objects.filter(name=name).exists():
        pass
    return category_data


def create_categories(user_data):
    csrf_token = None
    session = requests.Session()
    response = session.get(category_url)

    # Check if the response has a CSRF token in the cookie
    if "csrftoken" in session.cookies:
        csrf_token = session.cookies["csrftoken"]

    if csrf_token is None:
        print(
            "CSRF token not found. Make sure you have visited the registration URL at least once."
        )
        return

    # Include the CSRF token in the request headers
    headers = {"X-CSRFToken": csrf_token}
    # Send a POST request to the registration URL with the user data and CSRF token in headers
    response = session.post(category_url, data=user_data, headers=headers)

    # if response.status_code == 200:
    #     print(response.text)


if __name__ == "__main__":
    # Define the number of users you want to create
    num_users_to_create = int(input("Enter a range:. "))  # Change this as needed

    for _ in range(num_users_to_create):
        category_data = random_category()
        create_categories(category_data)
        time.sleep(2)
