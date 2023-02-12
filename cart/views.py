from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart, CartItems
from cart.serializers import CartSerializer, CartItemsSerializer, EditCartItemSerializer


# Cart:
# Get cart.
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


# CartItems:
# Get items.
@api_view(['GET'])
def get_cart_items(request, cart_pk):
    """
    GET - :return: all the items in the cart.
    """
    if request.method == 'GET':
        cartitems = CartItems.objects.filter(cart=cart_pk, paid_status=False)
        serializer = CartItemsSerializer(cartitems, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add an Item:
@api_view(['POST'])
def add_item_to_cart(request):
    """
    Post - add an item into CartItems.
    :request: {"product": id, "quantity": id, "cart": id}
    """
    if request.method == 'POST':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            # Checks if the Item already exists.
            cartitem = CartItems.objects.filter(product=serializer.validated_data.get(
                'product'), cart=serializer.validated_data.get('cart'), paid_status=False)
            if not cartitem:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                Exception(f"Item {cartitem} already exists.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete an Item.
@api_view(['DELETE'])
def delete_item_from_cart(request):
    """
    Delete cart item by id.
    request: {"product": id, "cart": id}
    """
    if request.method == 'DELETE':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            print(
                f"DELETE: product={serializer.data.get('product')}, cart={serializer.data.get('cart')}")
            cartitem = CartItems.objects.filter(
                product=serializer.data.get('product'), cart=serializer.data.get('cart'), paid_status=False)
            cartitem.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update an Item.
@api_view(['PUT'])
def update_item_in_cart(request):
    """
    Updates quantity and paid status. 
    Works only on paid_status=false items.
    :request: PUT - {"product": 1, "quantity": 1, "paid_status": false, "cart": 1}
    """
    if request.method == 'PUT':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            cartitem = CartItems.objects.get(product=serializer.data.get(
                'product'), cart=serializer.data.get('cart'), paid_status=False)
            if serializer.validated_data.get('paid_status'):
                cartitem.paid_status = serializer.data.get('paid_status')
            if serializer.validated_data.get('quantity'):
                cartitem.quantity = serializer.data.get('quantity')
            cartitem.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
