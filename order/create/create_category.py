import requests

from project_path import *
from urls import *

CATEGORIES = ["ACESSORIES", "CLOTHES", "HOUSEHOLD ITEMS", "BOOKS", "TOOLS"]


def random_category():
    name = fake.job()
    while ProductCategories.objects.filter(name=name.lower()).exists():
        name = fake.job()
    category_data = {"name": name}
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

    if response.status_code == 200:
        print("Category Created Successfully")
