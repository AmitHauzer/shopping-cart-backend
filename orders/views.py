from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart, CartItem
from orders.models import Order
from orders.serializers import OrderSerializer


@api_view(['GET', 'POST'])
def order(request, cart_pk):
    """
    GET - gets all the orders, filter by cart ID.
    POST - Creates a new order with all current cart items.
    """
    if request.method == 'GET':
        orders = Order.objects.filter(cart=cart_pk)
        print(f'orders: {orders}')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            cart = Cart.objects.get(id=cart_pk)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = CartItem.objects.filter(cart=cart_pk, paid_status=False)

        # Check if the cart is empty
        if not cart_items.exists():
            return Response({'error': 'There are no items in the cart.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Orders object and add the relevant data
        order = Order.objects.create(
            cart=cart,
            total_price=sum([cart_item.product.price *
                            cart_item.quantity for cart_item in cart_items]),
        )

        # Add the products associated with the cart items to the order
        for cart_item in cart_items:
            order.products.add(cart_item.product)

        # Set the paid status to True for all cart items
        cart_items.update(paid_status=True)

        # Redirect to the order confirmation page
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
