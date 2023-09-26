import requests
import random
from faker import Faker  # You'll need to install the 'Faker' library
import os
import sys
import django
import string
import random
from django.utils.text import slugify



DJANGO_PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "data_analysis.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_analysis.settings")
django.setup()
from dataset.models import *

# Define the URL for user registration
registration_url = "http://localhost:8002/register/"

# Initialize the Faker library for generating random data
fake = Faker()


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
    last_name1 = fake.last_name()
    last_name2 = fake.last_name()
    user_data = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": f"{last_name1} {last_name2}",
        "password": "your_password",  # Replace with the desired password
        "gender": random.choice(GENDER_CHOICES),
        "age": random.randint(16, 195),  # Adjust the age range as needed
        "password2": None,
    }
    # user_data["last_name"]=f"{las_name1} {last_name2}",
    user_data["slug"] = (
        slugify(f"{user_data['first_name']} {user_data['last_name']} {random_string}"),
    )
    user_data["username"] = (
        f"{user_data['first_name'][:3]}{user_data['last_name'][-3:]}{random_digit}",
    )
    user_data["age_group"] = calculate_age_group(user_data["age"])

    # Choose a random country from your Django models
    random_country = Country.objects.order_by("?").first()
    user_data["country"] = random_country.name

    # Choose a random state associated with the chosen country
    random_state = State.objects.filter(country=random_country).order_by("?").first()
    user_data["state"] = random_state.name

    email = user_data["email"]
    slug = user_data["slug"]
    username = user_data["username"]
    while User.objects.filter(email=email, slug=slug, username=username).exists():
        random_string = generate_random_string()
        user_data["first_name"] = fake.first_name()
        user_data["last_name"] = f"{last_name1} {last_name2}"
        user_data["username"] = (
            f"{user_data['first_name'][:3]}{user_data['last_name'][-3:]}{random_digit}",
        )
        user_data["slug"] = (
            slugify(
                f"{user_data['first_name']} {user_data['last_name']} {random_string}"
            ),
        )
    user_data["email"] = fake.email()
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
        # for i in range(num_users_to_create):
        #     output_file = open("content.html"+str(i), "w")
        #     output_file.write(response.text)
        # print(response.text)
        print("User registered successfully!")
    else:
        print("User registration failed.")


if __name__ == "__main__":
    # Define the number of users you want to create
    num_users_to_create = int(input("Enter a range:. "))  # Change this as needed

    for _ in range(num_users_to_create):
        user_data = generate_random_user_data()
        create_user(user_data)
