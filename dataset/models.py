from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


GENDER = (("MALE", "Male"), ("FEMALE", "Female"), ("OTHERS", "Others"))
AGE_GROUP = (
    ("YOUTH", "16-24"),
    ("YOUNG ADULTS", "25-39"),
    ("ADULTS", "40-69"),
    ("SENIOR CITIZENS", "70 and above"),
)


class Country(models.Model):
    """
    This is the model that handels the creaion of a country
    """

    name = models.CharField(max_length=5000, default="", unique=True, primary_key=True)
    country_code = models.CharField(max_length=20, default=None, unique=True, null=True)
    capital = models.CharField(max_length=5000, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"


class State(models.Model):
    """
    This is the model that handels the creaion of a state
    """

    country = models.ForeignKey(Country, on_delete=models.PROTECT, default="")
    name = models.CharField(max_length=6000, default="", unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "State"


class User(AbstractUser):
    """
    This is the model that handels the creation of users
    """

    email = models.EmailField(max_length=255, default=None, null=True, unique=True)
    first_name = models.CharField(
        max_length=255, default=None, blank=True, null=True, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=255, default=None, blank=True, null=True, verbose_name="Other Names"
    )
    password2 = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
        verbose_name="Confirm Password",
    )
    gender = models.CharField(max_length=255, choices=GENDER, default=None, null=True)
    age = models.PositiveIntegerField(default=None, null=True)
    age_group = models.CharField(
        max_length=255, choices=AGE_GROUP, default=None, null=True
    )
    slug = models.SlugField(
        max_length=255, default=None, unique=True, null=True, blank=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, default=None, null=True
    )
    state = models.ForeignKey(State, models.PROTECT, default=None, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class ProductCategories(models.Model):
    name = models.CharField(max_length=1000, default="", unique=True)
    slug = models.SlugField(max_length=255, default=None, unique=True, null=True)

    def __str__(self):
        return self.name


class ProductSubCategories(models.Model):
    product_categories = models.ForeignKey(
        ProductCategories, on_delete=models.PROTECT, default=None, null=True
    )
    name = models.CharField(max_length=1000, default="", unique=True)
    slug = models.SlugField(max_length=255, default=None, unique=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_categories = models.ForeignKey(
        ProductCategories, on_delete=models.PROTECT, default=None, null=True
    )
    product_sub_categories = models.ForeignKey(
        ProductSubCategories, on_delete=models.PROTECT, default=None, null=True
    )
    name = models.CharField(max_length=1000, default="")
    quantity = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=14, default=0.00, decimal_places=3)
    unit_price = models.DecimalField(max_digits=14, default=0.00, decimal_places=3)
    slug = models.SlugField(max_length=255, default=None, unique=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)
    date = models.DateField(default=timezone.now, null=True)
    product_categories = models.ForeignKey(
        ProductCategories, on_delete=models.PROTECT, default=None, null=True
    )
    product_sub_categories = models.ForeignKey(
        ProductSubCategories, on_delete=models.PROTECT, default=None, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, default=None, null=True
    )
    price = models.DecimalField(
        max_digits=14, default=None, decimal_places=3, null=True
    )
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(
        max_digits=14, default=None, decimal_places=3, null=True
    )
    slug = models.SlugField(max_length=255, default=None, unique=True, null=True)

    def __str__(self):
        return f"{self.user} {self.product}"
