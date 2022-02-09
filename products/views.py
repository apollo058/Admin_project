from rest_framework            import status
from rest_framework.viewsets   import ModelViewSet
from rest_framework.response   import Response
from rest_framework.pagination import PageNumberPagination

from .models import Product, HashTag
from .serializers import ProductSerializer, HashTagSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductViewSet(ModelViewSet):
    '''
    Product_API
    [GET] (list) /product (제품 리스트 조회)
    [GET] (retrieve) /product/<int:pk> (제품 상세 조회)
    [POST] (create) /product (제품 정보 생성)
    [PATCH] (partial_update) /product/<int:pk> (제품 정보 수정)
    [DELETE] (destroy) /product/<int:pk> (제품 정보 삭제)
    '''
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def create(self, request):
        product = request.data
        serializer = ProductSerializer(data=product)

        try:
            tag_set = [HashTag.objects.get_or_create(content=tag)[0].id for tag in product['hashtag']]
            product['hashtag'] = tag_set
        except KeyError:
            pass

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        update_product = request.data
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, update_product, partial=True)

        try:
            tag_set = [HashTag.objects.get_or_create(content=tag)[0].id for tag in update_product['hashtag']]
            update_product['hashtag'] = tag_set
        except KeyError:
            pass

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HashTagViewSet(ModelViewSet):
    serializer_class = HashTagSerializer
    queryset = HashTag.objects.all()
