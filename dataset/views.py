import random
import string

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils.text import slugify
from django.views import View

from .forms import *

User = get_user_model()


def generate_random_string():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))


def generate_random_number():
    return "".join(random.choices(string.digits, k=3))


# Create your views here.


def index(request):
    return render(request, "index.html", {})


def register(request):
    if request.method == "POST":
        random_string = generate_random_string()
        random_digit = generate_random_number()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.lower()
            user.last_name = user.last_name.lower()
            user.username = f"{user.first_name[:3]}{user.last_name[-3:]}{random_digit}"
            user.slug = slugify(f"{user.first_name} {user.last_name} {random_string}")
            user.email = user.email.lower()
            user.set_password(user.password)
            user.password2 = None
            user.save()
            # return redirect(index)
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def product_categories(request):
    if request.method == "POST":
        form = ProductCategoriesForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.name = category.name.lower()
            category.slug = slugify(f"{category.name} {'category'}")
            category.save()
            # return redirect(index)
    else:
        form = ProductCategoriesForm()
    return render(request, "product_categories.html", {"form": form})


def sub_categories(request):
    if request.method == "POST":
        form = ProductSubCategoriesForm(request.POST)
        if form.is_valid():
            sub_category = form.save(commit=False)
            sub_category.product_categories = sub_category.product_categories
            sub_category.name = sub_category.name.lower()
            sub_category.slug = slugify(
                f"{sub_category.name} {sub_category.product_categories}"
            )
            sub_category.save()
            # return redirect(index)
    else:
        form = ProductSubCategoriesForm()
    return render(request, "sub_categories.html", {"form": form})


def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_categories = product.product_categories
            product.product_sub_categories = product.product_sub_categories
            product.name = product.name.lower()
            product.slug = slugify(f"{product.name}{product.product_sub_categories}")
            product.save()
    else:
        form = ProductForm(
            initial={
                "unit_cost": None,
                "unit_price": None,
                "quantity": None,
            }
        )
    return render(request, "product.html", {"form": form})


def product_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = User.objects.order_by("?").first()
            # order.date = str(timezone.localtime)
            # order.slug = slugify(f"{order}")
            order.save()
    else:
        form = OrderForm(initial={"quantity": None})
    return render(request, "checkout.html", {"form": form})


class StaffView(View):
    template_name = "staff.html"

    def get(self, request):
        form = StaffForm(initial={"dob": None, "date_joined": None})
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        random_string = generate_random_string()
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.surname = staff.surname.lower() if staff.surname else None
            staff.first_name = staff.first_name.lower() if staff.first_name else None
            staff.other_names = staff.other_names.lower() if staff.other_names else None
            staff.role = staff.role.lower() if staff.role else None
            slug = slugify(
                f"{staff.surname} {staff.first_name} {staff.other_names if staff.other_names else ''} {random_string}"
            )
            while StaffDetails.objects.filter(slug=slug):
                random_string = generate_random_string()
                slug = slugify(
                    f"{staff.surname} {staff.first_name} {staff.other_names if staff.other_names else ''} {random_string}"
                )
            staff.slug = slug
            staff.save()
        return render(request, self.template_name, {"form": form})


class CompanyView(View):
    template_name = "company.html"

    def get(self, request):
        form = CompanyForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.name = company.name.lower() if company.name else ""
            slug = slugify(f"{company.name if company.name else ''}")
            company.slug = slug
            company.save()
        return render(request, self.template_name, {"form": form})


class SubsidiaryView(View):
    template_name = "subsidiary.html"

    def get(self, request):
        form = SubsidiaryForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SubsidiaryForm(request.POST)
        if form.is_valid():
            subsidiary = form.save(commit=False)
            subsidiary.name = subsidiary.name.lower() if subsidiary.name else ""
            slug = slugify(
                f"{subsidiary.name if subsidiary.name else ''} {subsidiary.company if subsidiary.company else ''}"
            )
            subsidiary.slug = slug
            subsidiary.save()
        return render(request, self.template_name, {"form": form})
