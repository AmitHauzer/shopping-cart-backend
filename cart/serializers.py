from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


# GET:
class CartItemSerializer(serializers.ModelSerializer):
    """
    Get all the cartitems with specific cart_id
    """
    product = ProductSerializer()  # nested serializer

    class Meta:
        model = CartItem
        fields = "__all__"


# POST/PUT:
# Added value - you don't need to add all the product details. The product ID is enough.
class EditCartItemSerializer(serializers.ModelSerializer):
    """
    Create, update or delete item.
    """
    class Meta:
        model = CartItem
        fields = "__all__"
