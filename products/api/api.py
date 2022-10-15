from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ecommerce.permissions import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [SafeMethodsRequestPermission]

    @action(methods=['post','get'], detail=False)
    def test(self,request):
        print(request.user)
        print(request.method)
        return Response('Worked')


class ProductAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [SafeMethodsRequestPermission]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['^category__name', '^title']


class FilterOptionAPI(viewsets.ModelViewSet):
    queryset = FilterOptions.objects.all()
    serializer_class = FilterOptionsSerializer
    permission_classes = [SafeMethodsRequestPermission]

    # def get_serializer_class(self):
    #
    #
    #
    # @action(detail=False, name="filter_options_readonly")
    # def filter_options_readonly(self,request):


class FilterOptionItemsAPI(viewsets.ModelViewSet):
    queryset = FilterOptionItems.objects.all()
    serializer_class = FilterOptionItemsSerializer
    permission_classes = [SafeMethodsRequestPermission]


class WishlistAPI(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Wishlist.objects.filter(user=user)
    serializer_class = WishlistSerializer
    permission_classes = [SafeMethodsRequestPermission]
