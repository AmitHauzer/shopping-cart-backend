from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart, CartItems
from cart.serializers import CartSerializer, CartItemsSerializer, EditCartItemSerializer

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


@api_view(['GET', 'POST'])
def get_cart_items(request, cart_pk):
    """
    GET - :return: all the items in the cart.
    Post - add an item into CartItems.
    """
    if request.method == 'GET':
        cartitems = CartItems.objects.filter(cart=cart_pk, paid_status=False)
        serializer = CartItemsSerializer(cartitems, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete Item
@api_view(['POST'])
def delete_item_from_cart(request, cart_pk):
    """
    delete cart item by id.
    request: {"product": id, "cart": id}
    """
    if request.method == 'POST':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            print(
                f"DELETE: product={serializer.data.get('product')}, cart={serializer.data.get('cart')}")
            cartitem = CartItems.objects.get(
                product=serializer.data.get('product'), cart=serializer.data.get('cart'), paid_status=False)
            cartitem.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
