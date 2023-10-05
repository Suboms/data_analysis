import requests

from project_path import *
from urls import *


def products():
    name = fake.job()
    quantity = random.randint(1, 1000)
    max_price_difference = 10000
    unit_cost = round(
        random.uniform(0.50, 99990.01), 2
    )  # Adjusted the upper bound for unit_cost
    max_unit_price = unit_cost + max_price_difference
    unit_price = round(random.uniform(unit_cost, max_unit_price), 2)
    product_category = ProductCategories.objects.order_by("?").first()
    product_sub_category = (
        ProductSubCategories.objects.filter(product_categories=product_category)
        .order_by("?")
        .first()
    )
    while product_sub_category is None:
        product_category = ProductCategories.objects.order_by("?").first()
        product_sub_category = (
            ProductSubCategories.objects.filter(product_categories=product_category)
            .order_by("?")
            .first()
        )

    while Product.objects.filter(name=name.lower()).exists():
        name = fake.job()

    data = {
        "name": name,
        "quantity": quantity,
        "unit_cost": unit_cost,
        "unit_price": unit_price,
        "product_categories": product_category.id,
        "product_sub_categories": product_sub_category.id,
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
            print("Product created successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
