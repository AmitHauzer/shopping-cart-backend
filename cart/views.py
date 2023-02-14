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
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#############################################


# CartItems:
# Get items.
@api_view(['GET', 'POST'])
def all_cart_items(request, cart_pk):
    """
    GET - :return: all the items in the cart.
    Post - add an item into CartItems.
    :request: {"product": id, "quantity": id, "cart": id}
    """
    if request.method == 'GET':
        cartitems = CartItems.objects.filter(cart=cart_pk, paid_status=False)
        serializer = CartItemsSerializer(cartitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
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


@api_view(['GET', 'PUT', 'DELETE'])
def single_cartitem(request, cart_pk, product_id):
    """
    GET: single item. 
    PUT - Updates quantity and paid status. Works only on paid_status=false items.
    :request: PUT - {"quantity": id, "paid_status": true/false}
    DELETE - Delete cart item by id.
    :request:
    """

    # Get an item:
    try:
        cartitem = CartItems.objects.get(
            product=product_id, cart=cart_pk,  paid_status=False)
        print(f'CartItem: {cartitem}')
    except:
        print('CartItem does not exist')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemsSerializer(cartitem)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EditCartItemSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get('paid_status'):
                cartitem.paid_status = serializer.data.get('paid_status')
            if serializer.validated_data.get('quantity'):
                cartitem.quantity = serializer.data.get('quantity')
            cartitem.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        print(f"DELETE cartitem: {cartitem}")
        cartitem.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
