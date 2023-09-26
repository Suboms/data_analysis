import os
import sys
import django
import requests
import random
from faker import Faker


product_url = "http://localhost:8002/product/"


DJANGO_PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "data_analysis.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_analysis.settings")
django.setup()
from dataset.models import *

fake = Faker()


def products():
    name = fake.job()
    quantity = random.randint(1, 1000)
    max_price_difference = 10000
    unit_cost = round(
        random.uniform(0.50, 99990.01), 2
    )  # Adjusted the upper bound for unit_cost
    max_unit_price = unit_cost + max_price_difference
    unit_price = round(random.uniform(unit_cost, max_unit_price), 2)
    categories = ProductCategories.objects.order_by("?").first()
    sub_categories = ProductSubCategories.objects.filter(product_categories=categories).order_by("?").first()

    data = {
        "name": name,
        "quantity": quantity,
        "unit_cost": unit_cost,
        "unit_price": unit_price,
        "product_categories": categories.id,
        "product_sub_categories": sub_categories.id,
    }

    return data


def create_product(user_data):
    try:
        csrf_token = None
        session = requests.Session()
        response = session.get(product_url)

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
        response = session.post(product_url, data=user_data, headers=headers)

        if response.status_code == 200:
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    num_users_to_create = int(input("Enter a range:. "))  # Change this as needed
    for _ in range(num_users_to_create):
        data = products()
        create_product(data)
