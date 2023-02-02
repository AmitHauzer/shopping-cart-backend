from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import Cart, CartItems


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # nested serializer

    class Meta:
        model = CartItems
        fields = "__all__"
