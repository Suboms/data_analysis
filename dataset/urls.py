from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("product/", product, name="product"),
    path("product/category/", product_categories, name="categories"),
    path("product/sub-category/", sub_categories, name="sub-categories"),
    path("checkout/", product_order, name="checkout"),
]
