from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductAll(APIView):
    def get(self, request):
        products = Product.objects.prefetch_related("product_image").filter(
            is_active=True
        )
        product_serializer = ProductSerializer(products, many=True)
        return render(request, "base.html", {"products": product_serializer.data})


class CategoryList(APIView):
    def get(self, request, category_slug=None):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category__in=category.get_descendants(include_self=True)
        )
        category_serializer = CategorySerializer(category)
        product_serializer = ProductSerializer(products, many=True)
        return render(request, "base.html", {"category": category_serializer.data, "products": product_serializer.data})
