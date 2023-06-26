from rest_framework import serializers

from .models import (Category, Product, ProductImage)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)
    
    class Meta:
        model = Product
        fields = "__all__"

