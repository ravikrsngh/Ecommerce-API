from orders.models import *
from products.api.serializers import *
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductCardSerializer()
    class Meta:
        model = OrderProduct
        fields = ['product']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    def get_order_items(self,instance):
        all_items = OrderProduct.objects.filter(order = instance).order_by("-id")
        serializer = OrderProductSerializer(all_items,many=True)
        return serializer.data


    class Meta:
        model = Order
        fields = '__all__'
