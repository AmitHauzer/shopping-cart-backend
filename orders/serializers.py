from rest_framework import serializers
from orders.models import Order

from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
