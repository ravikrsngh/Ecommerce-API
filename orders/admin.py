from django.contrib import admin
from .models import *
from .views import *
from django.urls import path,include
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    fields = ('title','image')
    readonly_fields = ('title','image')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    readonly_fields = ('account_name', 'order_id','order_receipt','razorpay_order_id','razorpay_payment_id','razorpay_signature','sub_total', 'tax', 'cnv_charges', 'discount_applied','total')
    search_fields = ['account_name', 'order_id','order_receipt','razorpay_order_id','razorpay_payment_id','razorpay_signature']
    list_display = ['account_name','razorpay_order_id','total']
    fieldsets = (
        ('Order Details', {
            'fields': ('account_name', 'order_id','order_receipt','razorpay_order_id','razorpay_payment_id','razorpay_signature')
        }),
        ('Shiping Details', {
            'fields': ('ship_to_name', 'ship_to_phonenumber', 'ship_to_street_address','ship_to_country','ship_to_state','ship_to_city','ship_to_zip')
        }),
        ('Price Details', {
            'fields': (
                'sub_total', 'tax', 'cnv_charges', 'discount_applied','total'
                )
        }),
    )

    def get_urls(self):
        urls = super().get_urls()
        return urls + [path("order-tracking", CustomView.as_view(), name="custom_view")]

admin.site.register(Order, OrderAdmin)
