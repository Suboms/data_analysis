from django.contrib import admin
from .models import *

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ("name", "country_code", "capital")


class StateAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    ordering = ("name",)
    list_display = ("name", "country")


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = (
        "id",
        "date",
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "country",
        "state",
        "gender",
        "age_group",
        "age",
    )


class ProductSubCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "product_categories",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(ProductCategories)
admin.site.register(ProductSubCategories, ProductSubCategoriesAdmin)
