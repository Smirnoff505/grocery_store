from rest_framework import serializers

from products.models import Category, Subcategory, Product


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ('category',)


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, source='category')

    class Meta:
        model = Category
        fields = ('title', 'slug', 'preview', 'subcategories',)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='subcategory.category.title')
    subcategory_info = serializers.CharField(source='subcategory.title')

    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('title', 'slug', 'price', 'category', 'subcategory_info', 'images')

    def get_images(self, obj):
        image_fields = ['preview_small', 'preview_middle', 'preview_big']
        urls = [getattr(obj, field).url for field in image_fields if getattr(obj, field)]
        return urls
