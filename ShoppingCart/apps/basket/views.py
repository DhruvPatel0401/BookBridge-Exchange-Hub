from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from ShoppingCart.apps.productCatalogue.models import Product

from .basket import Basket


class BasketSummary(APIView):
    def get(self, request):
        basket = Basket(request)
        return render(request, "basket/summary.html", {"basket": basket})
