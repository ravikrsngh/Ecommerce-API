import razorpay
import random
import string
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ecommerce.permissions import *
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters import rest_framework as filters
from orders.models import *
from wishlist_cart.models import *
from rest_framework.permissions import IsAuthenticated




def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return OrderSerializer
        else:
            return OrderSerializer

    @action(methods=['post'], detail=False)
    def create_razorpay_order(self,request):
        client = razorpay.Client(auth=("rzp_test_lYOMizShZ9dK1d", "FPZAwaMrz7DgYyvbPq1kOXSp"))
        amount = request.data['amount']
        order_receipt = random_string_generator()
        response = client.order.create(dict(amount=amount*100, currency="INR", receipt=order_receipt, payment_capture='1'))
        return Response({
        'order_id':response['id'],
        'order_receipt':order_receipt,
        'amount': response['amount'],
        'currency':response['currency']
        })

    @action(methods=['post'], detail=False)
    def verify_signature(self,request):
        client = razorpay.Client(auth=("rzp_test_lYOMizShZ9dK1d", "FPZAwaMrz7DgYyvbPq1kOXSp"))
        params_dict = {
        'razorpay_payment_id' : request.data['razorpay_paymentId'],
        'razorpay_order_id' : request.data['razorpay_orderId'],
        'razorpay_signature' : request.data['razorpay_signature']
        }
        status = client.utility.verify_payment_signature(params_dict)
        print(status)
        return Response({"status":status})

    @action(methods=['post'], detail=False)
    def create_order(self,request):
        print(request.data)
        order_obj = Order.objects.create(
            order_receipt = request.data['order_receipt'],
            order_id = request.data['order_id'],
            razorpay_payment_id = request.data['razorpay_paymentId'],
            razorpay_order_id = request.data['razorpay_orderId'],
            razorpay_signature = request.data['razorpay_signature'],
            account_name = request.user.first_name + " " + request.user.last_name,
            ship_to_name = request.data['selectedAddress']['first_name'] + " " + request.data['selectedAddress']['last_name'] ,
            ship_to_phonenumber = request.data['selectedAddress']['phone_number'],
            ship_to_street_address = request.data['selectedAddress']['address_line1'],
            ship_to_country = request.data['selectedAddress']['country'],
            ship_to_state = request.data['selectedAddress']['state'],
            ship_to_city = request.data['selectedAddress']['city'],
            ship_to_zip = request.data['selectedAddress']['zipcode'],
            sub_total = request.data['cartPrice']['subtotal'],
            tax = request.data['cartPrice']['tax'],
            cnv_charges = request.data['cartPrice']['cvn_charges'],
            total = request.data['cartPrice']['total'],
        )
        all_cart_items = Cart.objects.filter(user=request.user)
        for cart_item in all_cart_items:
            OrderProduct.objects.create(order=order_obj,product=cart_item.product)
        serializer = OrderDetailSerializer(order_obj,many=False)
        all_cart_items.delete()
        return Response(serializer.data)
