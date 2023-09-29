import requests
import string
import random
from tools.project_path import *
from tools.urls import *
from django.utils.text import slugify


# Define choices for gender based on your Django model choices
GENDER_CHOICES = ["MALE", "FEMALE", "OTHERS"]

# Define the age groups


def calculate_age_group(age):
    if age <= 24:
        return "YOUTH"
    elif 25 <= age <= 39:
        return "YOUNG ADULTS"
    elif 40 <= age <= 69:
        return "ADULTS"
    else:
        return "SENIOR CITIZENS"


def generate_random_string():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))


def generate_random_number():
    return "".join(random.choices(string.digits, k=3))


def generate_random_user_data():
    random_string = generate_random_string()
    random_digit = generate_random_number()
    first_name = fake.first_name()
    last_name1 = fake.last_name()
    last_name2 = fake.last_name()
    last_name = f"{last_name1} {last_name2}"
    email = fake.email()
    age = random.randint(16, 195)
    gender = random.choice(GENDER_CHOICES)
    password = "your_password"
    username = f"{first_name[:3]}{last_name[-3:]}{random_digit}"
    slug = slugify(f"{first_name} {last_name} {random_string}")
    age_group = calculate_age_group(age)
    country = random_country = Country.objects.order_by("?").first()
    state = State.objects.filter(country=random_country).order_by("?").first()

    user = User.objects.filter(
        email=email.lower(), slug=slug.lower(), username=username.lower()
    ).exists()
    while user:
        email = fake.email()
        username = f"{first_name[:3]}{last_name[-3:]}{random_digit}"
        slug = slugify(f"{first_name} {last_name} {random_string}")

    user_data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "gender": gender,
        "username": username,
        "slug": slug,
        "age_group": age_group,
        "country": country,
        "state": state,
        "age": age,
        "password2": None,
    }
    return user_data


def create_user(user_data):
    csrf_token = None
    session = requests.Session()
    response = session.get(registration_url)

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
    response = session.post(registration_url, data=user_data, headers=headers)

    # Check if the registration was successful (you may need to adjust this based on your registration logic)
    if response.status_code == 200:
        print("User registered successfully!")
    else:
        print("User registration failed.")
