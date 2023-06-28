from ShoppingCart.apps.productCatalogue.models import Product
from decimal import Decimal
from django.conf import settings

class Basket:
    def __init__(self, request):
        self.session = request.session
        self.basket = self.session.get(settings.BASKET_SESSION_ID, {})

    def add(self, product, qty):
        pass

    