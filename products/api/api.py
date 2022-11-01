from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ecommerce.permissions import *
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters import rest_framework as filters


class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [SafeMethodsRequestPermission]

    @action(methods=['post','get'], detail=False)
    def test(self,request):
        print(request.user)
        print(request.method)
        return Response('Worked')



class ProductFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__name',
        to_field_name='name',
        queryset=FilterOptionItems.objects.all(),
        conjoined=False
    )
    category = filters.ModelMultipleChoiceFilter(
        field_name='category__name',
        to_field_name='name',
        queryset=Category.objects.all(),
    )
    selling_price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['category', 'tags','selling_price']



class ProductAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [SafeMethodsRequestPermission]
    filter_backends = [filters.DjangoFilterBackend,SearchFilter,OrderingFilter]
    #filterset_fields = ['category', 'tags']
    filterset_class = ProductFilter
    search_fields = ['$category__name', '$title','$tags__name']
    ordering_fields = ['id', 'price']
    ordering = ['-id']

    @action(methods=['get'], detail=True)
    def get_product_details(self,request,pk=None):
        product = self.get_object()
        print(product)
        serializer = ProductDetailsSerializer(product,many=False)
        return Response(serializer.data)



class FilterOptionAPI(viewsets.ModelViewSet):
    queryset = FilterOptions.objects.all()
    serializer_class = FilterOptionsSerializer
    permission_classes = [SafeMethodsRequestPermission]
    filter_backends = [filters.DjangoFilterBackend,SearchFilter]
    filterset_fields = ['display']

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



class ReviewAPI(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [SafeMethodsRequestPermission]
