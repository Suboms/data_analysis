import datetime
import random

from dateutil.relativedelta import relativedelta
from django.db.models import F
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import *


@receiver(post_save, sender=Order)
def update_order(sender, instance, **kwargs):
    order_count = Order.objects.filter(user=instance.user).count()
    formatted_order_count = str(order_count).zfill(3)
    if instance.price is None and instance.total_price is None:
        product_ordered = instance.product.unit_price
        instance.price = product_ordered
        instance.total_price = product_ordered * instance.quantity
        if not instance.slug:
            slug = slugify(f"order {instance.user.username} {formatted_order_count}")
            instance.slug = slug

        instance.save()


@receiver(post_save, sender=StaffDetails)
def update_staff_details(sender, instance, **kwargs):
    if instance.age is None and instance.retirement_date is None:
        current_date = timezone.localdate()
        dob = instance.dob
        date_joined = instance.date_joined
        age = relativedelta(date_joined, dob)
        year_on_contract = random.randint(5, 35)
        while year_on_contract + age.years > 70:
            year_on_contract = random.randint(5, 35)
            instance.year_on_contract = year_on_contract
            break
        retirement_date = instance.date_joined + relativedelta(years=year_on_contract)
        StaffDetails.objects.filter(pk=instance.pk).update(
            age=age.years,
            retirement_date=retirement_date,
            year_on_contract=year_on_contract,
        )
