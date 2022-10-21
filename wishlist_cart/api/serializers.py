from wishlist_cart.models import *
from rest_framework import serializers
from products.models import *
from products.api.serializers import *

class WishlistSerializer(serializers.ModelSerializer):

    def validate(self,data):
        user = self.context.get('request').user
        if Wishlist.objects.filter(user=user).filter(product=data.get('product')).exists():
            raise serializers.ValidationError("Item already added to the wishlist")
        else:
            return data

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        instance = Wishlist.objects.create(user=request.user,product=validated_data.get('product'))
        return instance

    class Meta:
        model = Wishlist
        fields = ['product']


class WishlistDetailSerializer(serializers.ModelSerializer):
    product = ProductCardSerializer(many=False)
    class Meta:
        model = Wishlist
        fields = ['product', 'id']


class CartSerializer(serializers.ModelSerializer):

    def validate(self,data):
        user = self.context.get('request').user
        if Cart.objects.filter(user=user).filter(product=data.get('product')).exists():
            raise serializers.ValidationError("Item already added to the cart")
        else:
            return data

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        instance = Cart.objects.create(user=request.user,product=validated_data.get('product'),qty=validated_data.get('qty'))
        return instance

    class Meta:
        model = Cart
        fields = ['product','qty']

class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductCardSerializer(many=False)
    class Meta:
        model = Cart
        fields = ['product','qty','id']
