from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from product.models import Product 

# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)





class CartItems(models.Model):
    cart = models.ForeignKey(Cart ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50)])
    paid_status = models.BooleanField(default=False)


    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)