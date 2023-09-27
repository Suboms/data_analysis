from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import *
from django.utils.text import slugify


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
