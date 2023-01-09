from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
