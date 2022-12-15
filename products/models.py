from django.db import models
from users.models import *
from django.utils.html import mark_safe
from django.db.models.signals import pre_delete, post_delete, post_save, pre_save

category_level_choices = [
        ("lvl1", "Level 1"),
        ("lvl2", "Level 2"),
        ("lvl3", "Level 3"),
        ("lvl4", "Level 4"),
]


class Category(models.Model):
    name = models.CharField(max_length=50)
    img=models.TextField(default="")
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=10,choices=category_level_choices,default='lvl1')

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return 'name',


class FilterOptions(models.Model):
    title = models.CharField(max_length=50)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def filtericon_directory_path(instance,filename):
    return 'media/FilterIcons/{0}'.format(filename)

class FilterOptionItems(models.Model):
    icon = models.ImageField(upload_to = filtericon_directory_path,null=True,blank=True)
    name = models.CharField(max_length=50)
    filter = models.ForeignKey(FilterOptions,on_delete=models.CASCADE, related_name="filter_option_items")

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    class Meta:
        unique_together = ('name', 'filter')


class GoldPurity(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField(default=0)
    making_charges = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        all_items = Product.objects.filter(gold_purity=self)
        for item in all_items:
            item.making_charges = int(float(item.net_weight)*item.diamond_purity.making_charges) if item.diamond_purity else int(float(item.gold_weight)*self.making_charges) +  item.making_charges
            item.mrp = int(float(item.gold_weight)*self.price) + (  int(float(item.diamond_weight)*item.diamond_purity.price) if item.diamond_purity else 0 )
            item.selling_price = item.mrp * (100- item.discount_value) / 100

            item.save()

    def __str__(self):
        return self.name

class DiamondPurity(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField(default=0)
    making_charges = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        all_items = Product.objects.filter(diamond_purity=self)
        for item in all_items:
            item.making_charges = int(float(item.net_weight)*item.diamond_purity.making_charges)
            item.mrp = int(float(item.diamond_weight)*self.price) + (  int(float(item.gold_weight)*item.gold_purity.price) if item.gold_purity else 0 ) + item.making_charges
            item.selling_price = item.mrp * (100- item.discount_value) / 100
            item.save()


    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50)
    mrp = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    short_description = models.TextField()
    long_description = models.TextField()
    shipping_details = models.TextField()
    return_details = models.TextField()
    avg_rating = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    on_discount = models.BooleanField(default=False)
    discount_value = models.IntegerField(default=0)
    stock_number = models.CharField(max_length=8,null=True,blank=True,unique=True)
    gold_purity = models.ForeignKey(GoldPurity,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Gold Purity")
    diamond_purity = models.ForeignKey(DiamondPurity,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Diamond Purity")
    gross_weight = models.CharField(max_length=5,default="",verbose_name="Gross Weight (g)")
    net_weight = models.CharField(max_length=5,default="",verbose_name="Net Weight (g)")
    gold_weight = models.CharField(max_length=5,default="",verbose_name="Gold Weight (g)")
    diamond_weight = models.CharField(max_length=5,default="",verbose_name="Diamond Weight (ct)")
    making_charges = models.CharField(max_length=5, default="0")
    height = models.CharField(max_length=5,default="")
    width = models.CharField(max_length=5,default="")
    tags = models.ManyToManyField(FilterOptionItems)


    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return 'title',




def productimage_directory_path(instance,filename):
    return 'media/ProductImages/{0}/{1}'.format(instance.product.title, filename)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')
    img = models.ImageField(upload_to = productimage_directory_path,null=True,blank=True)

    def __str__(self):
        return self.product.title

    @property
    def img_preview(self):
        if self.img:
            return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
        return ""


class Review(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.CharField(max_length=150)

    def __str__(self):
        return self.name
