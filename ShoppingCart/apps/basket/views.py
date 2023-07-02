from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ShoppingCart.apps.productCatalogue.models import Product

from .basket import Basket


class BasketSummary(APIView):
    def get(self, request):
        basket = Basket(request)
        return render(request, "basket/summary.html", {"basket": basket})


class BaseketAdd(APIView):
    def post(self, request):
        basket = Basket(request)
        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))
            product_qty = int(request.data.get("productqty"))
            product = get_object_or_404(Product, id=product_id)
            basket.add(product=product, qty=product_qty)

            basketqty = basket.__len__()
            data = {"qty": basketqty}
            return Response(data)

class BasketDelete(APIView):
    def post(self, request):
        basket = Basket(request)
        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))
            basket.delete(product=product_id)

            basketqty = basket.__len__()
            baskettotal = basket.get_total_price()
            data = {"subtotal": baskettotal, "qty": basketqty}
            return Response(data)

class BasketUpdate(APIView):
    pass
