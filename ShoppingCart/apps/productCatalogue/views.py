from django.shortcuts import render
from rest_framework import mixins, viewsets, generics
from .models import Category, ProductType, ProductSpecification, Product, ProductSpecificationValue, ProductImage
from .serializers import CategorySerializer, ProductTypeSerializer, ProductSpecificationSerializer, ProductSerializer, ProductSpecificationValueSerializer, ProductImageSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    template_name = 'base.html'

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    template_name = 'product_list.html'


class ProductSpecificationValueViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecificationValue.objects.all()
    serializer_class = ProductSpecificationValueSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
