from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart, CartItems
from cart.serializers import CartSerializer, CartItemsSerializer

# Create your views here.
@api_view(['GET'])
def cart(request):
    """
    get a cart.
    """
    if request.method == 'GET':
        cart = Cart.objects.get(id=1)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cart_items(request, cart_pk):
    """
    get all the items in the cart.
    """
    if request.method == 'GET':
        cartitems = CartItems.objects.filter(cart=cart_pk)
        serializer = CartItemsSerializer(cartitems, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)