from django.db import models
from users.models import *
from products.models import *
from django.utils.html import mark_safe


class Order(models.Model):
    order_receipt= models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=200)
    account_name = models.CharField(max_length=100)
    ship_to_name = models.CharField(max_length=100)
    ship_to_phonenumber = models.CharField(max_length=15)
    ship_to_street_address = models.CharField(max_length=100)
    ship_to_country = models.CharField(max_length=30)
    ship_to_state = models.CharField(max_length=30)
    ship_to_city = models.CharField(max_length=30)
    ship_to_zip = models.CharField(max_length=10)
    sub_total = models.CharField(max_length=6, default="0")
    tax = models.CharField(max_length=6, default="0")
    cnv_charges = models.CharField(max_length=6, default="0")
    discount_applied = models.CharField(max_length=6, default="0")
    total = models.CharField(max_length=6, default="0")

    def __str__(self):
        return self.razorpay_order_id


class OrderProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.order.razorpay_order_id

    @property
    def image(self):
        product_image = ProductImages.objects.filter(product=self.product).first()
        if product_image.img:
            return mark_safe('<img src="{}" width="100" />'.format(product_image.img.url))
        return ""

    @property
    def title(self):
        return self.product.title
