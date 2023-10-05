from datetime import timedelta

from dateutil import relativedelta
from django import forms
from django.forms import ModelForm, ValidationError

from .models import *

max_date = timezone.localdate() - timedelta(days=6574.5)


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


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ["slug"]


class SubsidiaryForm(ModelForm):
    class Meta:
        model = Subsidiaries
        exclude = ["slug"]


class StaffForm(ModelForm):
    class Meta:
        model = StaffDetails
        exclude = ["slug", "age", "retirement_date", "year_on_contract"]

        widgets = {
            "dob": forms.DateInput(attrs={"type": "date", "max": max_date}),
            "date_joined": forms.DateInput(
                attrs={"type": "date", "max": timezone.localdate()}
            ),
            "year_on_contract": forms.NumberInput(attrs={"max": 35}),
        }

    def clean_date_joined(self):
        date_joined = self.cleaned_data.get("date_joined")
        current_date = timezone.localdate()
        delta = relativedelta.relativedelta(current_date, date_joined)
        if date_joined > current_date or delta.years > 35:
            raise ValidationError(f"{date_joined} is not valid")

        return date_joined

    def clean(self):
        cleaned_data = super().clean()
        current_date = timezone.localdate()
        dob = cleaned_data.get("dob")
        date_joined = cleaned_data.get("date_joined")
        delta = relativedelta.relativedelta(date_joined, dob)

        if dob > current_date:
            raise ValidationError(f"{dob} is not valid")

        elif delta.years < 18:
            raise ValidationError("staff is not 18 years when they joined")

        elif delta.years > 40:
            raise ValidationError("staff is older than 40")

        return cleaned_data
