import requests

from project_path import *
from urls import *


def order():
    # user = User.objects.order_by("?").first()
    product_category = ProductCategories.objects.order_by("?").first()
    product_sub_category = (
        ProductSubCategories.objects.filter(product_categories=product_category)
        .order_by("?")
        .first()
    )
    product = (
        Product.objects.filter(
            product_categories=product_category,
            product_sub_categories=product_sub_category,
        )
        .order_by("?")
        .first()
    )
    while (
        product
        and product_sub_category is None
        or product is None
        or product_sub_category is None
    ):
        product_category = ProductCategories.objects.order_by("?").first()
        product_sub_category = (
            ProductSubCategories.objects.filter(product_categories=product_category)
            .order_by("?")
            .first()
        )
        product = (
            Product.objects.filter(
                product_categories=product_category,
                product_sub_categories=product_sub_category,
            )
            .order_by("?")
            .first()
        )
    quantity = random.randint(5, 500)
    data = {
        "product_categories": product_category.id,
        "product_sub_categories": product_sub_category.id,
        "product": product.id,
        "quantity": quantity,
    }

    return data


def create_order(data):
    try:
        csrf_token = None
        session = requests.Session()
        response = session.get(order_url)

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
        response = session.post(order_url, data=data, headers=headers)

        if response.status_code == 200:
            print("Order Created Successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
