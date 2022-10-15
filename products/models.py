from django.db import models
from django.contrib.auth.models import User


category_level_choices = [
        ("lvl1", "Level 1"),
        ("lvl2", "Level 2"),
        ("lvl3", "Level 3"),
        ("lvl4", "Level 4"),
]


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=10,choices=category_level_choices,default='lvl1')

    def __str__(self):
        return self.name


class FilterOptions(models.Model):
    title = models.CharField(max_length=50)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FilterOptionItems(models.Model):
    icon = models.TextField()
    name = models.CharField(max_length=50)
    filter = models.ForeignKey(FilterOptions,on_delete=models.CASCADE, related_name="filter_option_items")

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
    tags = models.ManyToManyField(FilterOptionItems)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    link = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')

    def __str__(self):
        return self.product.title



class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
