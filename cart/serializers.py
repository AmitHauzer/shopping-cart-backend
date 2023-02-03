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
    """
    Get all the cartitems with specific cart_id
    """
    product = ProductSerializer()  # nested serializer

    class Meta:
        model = CartItems
        fields = "__all__"


# POST:
class EditCartItemSerializer(serializers.ModelSerializer):
    """
    Create or delete item.
    """
    class Meta:
        model = CartItems
        fields = "__all__"
