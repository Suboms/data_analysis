import requests
from tools.project_path import *
from tools.urls import *


def sub_category_data():
    name = fake.job()
    product_categories = ProductCategories.objects.order_by("?").first()
    while ProductSubCategories.objects.filter(name=name.lower()).exists():
        name = fake.job()
    data = {"name": name, "product_categories": product_categories.id}

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

        if response.status_code == 200:
            print("Sub Category created successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
