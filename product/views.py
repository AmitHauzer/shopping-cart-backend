
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def all_products(request):
    """
    List all the products.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_product(request, pk):
    """
    single product.
    """
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['POST'])
def admin_add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search(request):
    if request.method == 'GET':
        product = Product.objects.filter(name__istartswith='test')
        serializer = ProductSerializer(product)
        return Response(serializer.data)
