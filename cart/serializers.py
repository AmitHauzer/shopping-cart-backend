from rest_framework import serializers
from product.models import Product

from product.serializers import ProductSerializer
from .models import Cart, CartItems


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


# GET:
class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # nested serializer

    class Meta:
        model = CartItems
        fields = "__all__"


# POST:
class EditCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItems
        fields = "__all__"
