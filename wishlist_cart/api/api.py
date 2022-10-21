from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ecommerce.permissions import *
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

class WishlistAPI(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Wishlist.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == "list":
            return WishlistDetailSerializer
        else:
            return WishlistSerializer


class CartAPI(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == "list":
            return CartDetailSerializer
        else:
            return CartSerializer

    def calcCartPrice(self,cart_items):
        subtotal = 0;
        for i in cart_items:
            subtotal += i.product.selling_price * i.qty
        tax = subtotal * 0.18
        cvn_charges = 150
        total = subtotal + tax + cvn_charges
        return {"subtotal":subtotal,"tax":tax,"cvn_charges":cvn_charges,"total":total}

    @action(methods=['get'], detail=False)
    def get_cart_details(self,request):
        cart_items= self.get_queryset()
        print(cart_items)
        cart_price = self.calcCartPrice(cart_items)
        serializer = CartDetailSerializer(cart_items,many=True)
        return Response({"cart_items":serializer.data,"cart_price":cart_price})
