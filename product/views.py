
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def all_products(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        product = Product.objects.filter(archive=False)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def single_product(request, pk):
    """
    GET - get a single product.
    PUT - update a product.
    DELETE - delete a producet.
    :return: JSON
    :request: {"id": id ,"name": "str", "description": "str", "price": "str", "image": PATH, "archive":false}

    """
    # Get the item.
    try:
        product = Product.objects.get(pk=pk, archive=False)
        print(f'Product: {product}')
    except Product.DoesNotExist:
        print('The product does not exist')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # Archive:
        product.archive = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get('name'):
                product.name = serializer.data.get('name')
            if serializer.validated_data.get('description'):
                product.description = serializer.data.get('description')
            if serializer.validated_data.get('price'):
                product.price = serializer.data.get('price')
            if serializer.validated_data.get('archive'):
                product.archive = serializer.data.get('archive')
            if serializer.validated_data.get('image'):
                product.image = serializer.data.get('image')
            product.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search(request):
    if request.method == 'GET':
        """
        search product by name.
        """
        query = request.GET.get('search')
        products = Product.objects.filter(
            name__istartswith=query, archive=False)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
