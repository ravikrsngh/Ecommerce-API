from products.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    def validate(self,data):
        if not data.get('level') == 'lvl1' and data.get('parent_category') is None:
            raise serializers.ValidationError("You must select a valid parent category")
        if data.get('level') == 'lvl1' and not data.get('parent_category') is None:
            raise serializers.ValidationError("Level 1 categories has no parent categories")
        return data

    class Meta:
        model = Category
        fields = '__all__'


class FilterOptionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterOptionItems
        fields = '__all__'


class FilterOptionsSerializer(serializers.ModelSerializer):
    filter_option_items = FilterOptionItemsSerializer(many=True,required=False)

    def create(self, validated_data):
        filter_option_items = validated_data.pop('filter_option_items')
        filter_options_obj = FilterOptions.objects.create(**validated_data)
        for filter_option_item in filter_option_items:
            filter_option_item.pop('filter')
            FilterOptionItems.objects.create(filter=filter_options_obj, **filter_option_item)
        return filter_options_obj

    class Meta:
        model = FilterOptions
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    class Meta:
        model = ProductImages
        fields = ['id','img']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, required=False)

    def validate(self,data):
        product_images = data.get('product_images')
        if len(product_images) < 4:
            raise serializers.ValidationError("You should add 4 images. You are adding only " + str(len(product_images)) + " images.")
        return data

    def create(self, validated_data):
        product_images = validated_data.pop('product_images')
        tags = validated_data.pop('tags')
        product_obj = Product.objects.create(**validated_data)
        for tag in tags:
            print(tag)
            product_obj.tags.add(tag)
        for product_image in product_images:
            ProductImages.objects.create(product=product_obj, **product_image)
        return product_obj

    def update(self,instance,validated_data):
        print(validated_data)
        product_images = list(instance.product_images.all())
        product_images_data = validated_data.pop('product_images')
        tags = validated_data.pop('tags')
        instance.title = validated_data.get('title')
        instance.mrp = validated_data.get('mrp')
        instance.selling_price = validated_data.get('selling_price')
        instance.category = validated_data.get('category')
        instance.short_description = validated_data.get('short_description')
        instance.long_description = validated_data.get('long_description')
        instance.shipping_details =validated_data.get('shipping_details')
        instance.return_details = validated_data.get('return_details')
        instance.avg_rating = validated_data.get('avg_rating')
        instance.total_reviews = validated_data.get('total_reviews')
        instance.on_discount = validated_data.get('on_discount')
        instance.discount_value = validated_data.get('discount_value')
        for tag in tags:
            instance.tags.add(tag)
        instance.save()
        for product_image_data in product_images_data:
            product_image = product_images.pop(0)
            product_image.link = product_image_data.get('link')
            product_image.save()
        return instance

    class Meta:
        model = Product
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        instance = Review.objects.create(user=request.user, **validated_data)
        all_reviews = Review.objects.filter(product=instance.product).count()
        instance.product.total_reviews = all_reviews
        instance.product.save()
        return instance

    class Meta:
        model = Review
        fields = ['product','name','review']


class GoldPuritySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldPurity
        fields = '__all__'

class DiamondPuritySerializer(serializers.ModelSerializer):

    class Meta:
        model = DiamondPurity
        fields = '__all__'

class ProductDetailsSerializer(serializers.ModelSerializer):

    product_images = ProductImageSerializer(many=True)

    reviews = serializers.SerializerMethodField()

    related_products = serializers.SerializerMethodField()

    category = CategorySerializer(many=False)

    gold_purity = GoldPuritySerializer(many=False)

    diamond_purity = DiamondPuritySerializer(many=False)

    material_prices = serializers.SerializerMethodField()

    def get_reviews(self,instance):
        all_reviews = Review.objects.filter(product = instance).order_by("-id")
        if len(all_reviews) > 4:
            all_reviews = all_reviews[:4]
        serializer = ReviewSerializer(all_reviews,many=True)
        return serializer.data

    def get_related_products(self, instance):
        all_related_products = list(set(Product.objects.filter(category = instance.category).filter(tags__in=instance.tags.all()).exclude(id=instance.id)))
        if len(all_related_products) > 6:
            all_reviews = all_related_products[:6]
        serializer = ProductSerializer(all_related_products,many=True)
        return serializer.data

    def get_material_prices(self,instance):
        gold_price = int(float(instance.gold_weight)*instance.gold_purity.price)
        diamond_price = int(float(instance.diamond_weight)*instance.diamond_purity.price)

        return {
            "gold_price":gold_price,
            "diamond_price":diamond_price
        }


    class Meta:
        model = Product
        fields = '__all__'


class ProductCardSerializer(serializers.ModelSerializer):

    product_images = ProductImageSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ['id','title','mrp','category','selling_price','total_reviews','product_images']
