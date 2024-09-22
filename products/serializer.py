from rest_framework import serializers
from .models import Category, Product


# Category Serializer
def get_parent_category(obj):
    if obj.parent_category:
        return CategorySerializer(obj.parent_category).data
    return None


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent_category']


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Category Serializer

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url']
