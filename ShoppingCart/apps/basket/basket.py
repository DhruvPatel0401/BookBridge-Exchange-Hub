from decimal import Decimal

from django.conf import settings

from ShoppingCart.apps.productCatalogue.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        else:
            self.basket[product_id] = {"price": str(product.regular_price), "qty": qty}

        self.save()

    def __len__(self):
        return sum(item["qty"] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["total_price"] = Decimal(item["price"]) * item["qty"]
            yield item

    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product, qty):
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        self.save()

    def get_subtotal_price(self):
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )

    def get_delivery_price(self):
        pass

    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )
        if "purchase" in self.session:
            newprice = self.session["purchase"]["delivery_price"]
        total = subtotal + Decimal(newprice)

        return total

    def save(self):
        self.session.modified = True
