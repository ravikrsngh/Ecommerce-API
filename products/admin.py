from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import mark_safe
from django.template.loader import render_to_string
from django.shortcuts import redirect


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 0
    readonly_fields = ('img_preview',)

class ProductReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('user','review','name')

    def has_add_permission(self, request, obj=None):
        return False

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImageInline, ProductReviewInline]
    list_display = ('title', 'mrp', 'selling_price', 'category_name','tag')
    search_fields = ['title', 'category__name','tags__name',]
    summernote_fields = ('short_description', 'long_description','shipping_details','return_details',)
    filter_horizontal = ('tags',)
    list_filter = ('category','tags',)


    fieldsets = (
        ('Product Info', {
            'fields': ('stock_number','title', 'mrp','selling_price','category')
        }),
        ('Product Descriptions', {
            'fields': ('gold_purity','diamond_purity','height','width','gross_weight','net_weight','gold_weight','diamond_weight','making_charges','short_description', 'long_description', 'shipping_details','return_details',)
        }),
        ('Additional Details', {
            'fields': (
                'avg_rating', 'total_reviews', 'on_discount','discount_value', 'tags'
                )
        }),
    )

    def gold_purity(self,instance):
        return instance.gold_purity.name

    def diamond_purity(self,instance):
        return instance.diamond_purity.name

    def category_name(self,instance):
        return instance.category.name

    def tag(self,instance):
        str = """"""
        for i in instance.tags.all():
            str += "<span style=\"background:#6c757d;color:white;padding:5px 10px;margin:5px 0px;border-radius:5px;\">"+i.name+"</span>"
        return mark_safe("<div style=\"display:flex;gap:5px;flex-wrap:wrap;\">"+str+"</div>")

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['name', 'user','product']
    readonly_fields= ['user','product','name','review']


class GoldPurityAdmin(admin.ModelAdmin):
    list_display = ('name','price','making_charges')

class DiamondPurityAdmin(admin.ModelAdmin):
    list_display = ('name','price','making_charges')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(FilterOptions)
admin.site.register(FilterOptionItems)
admin.site.register(Review,ReviewAdmin)
admin.site.register(GoldPurity,GoldPurityAdmin)
admin.site.register(DiamondPurity,DiamondPurityAdmin)
