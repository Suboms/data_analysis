from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "gender",
            "age",
            "age_group",
            "country",
            "state",
            "password",
            "password2",
        ]


class ProductCategoriesForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ["name"]


class ProductSubCategoriesForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategories
        exclude = ["slug"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["slug"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["slug", "user", "date", "price", "total_price"]
