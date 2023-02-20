from django.db import models

from cart.models import Cart, CartItem
from product.models import Product


class Order(models.Model):
    products = models.ManyToManyField(Product)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
