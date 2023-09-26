import requests
import random
import os
import sys
import django
from faker import Faker

sub_category_url = "http://localhost:8002/product/sub-category/"


DJANGO_PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "data_analysis.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_analysis.settings")
django.setup()
from dataset.models import *


fake = Faker()


def sub_category():
    data = {"name": fake.job()}

    random_category = ProductCategories.objects.order_by("?").first()
    data["product_categories"] = random_category.id

    name = data["name"]
    while ProductSubCategories.objects.filter(name=name).exists():
        data["name"] = fake.job()
    return data


def create_sub_categories(user_data):
    try:
        csrf_token = None
        session = requests.Session()
        response = session.get(sub_category_url)

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
        response = session.post(sub_category_url, data=user_data, headers=headers)

        # if response.status_code == 200:
        #     print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Define the number of users you want to create
    num_users_to_create = int(input("Enter a range:. "))  # Change this as needed

    for _ in range(num_users_to_create):
        data = sub_category()
        create_sub_categories(data)
