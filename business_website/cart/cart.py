from decimal import Decimal

import requests
from django.conf import settings
from shop import models


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, laptop, quantity=1, update_quantity=False):
        laptop_id = str(laptop.id)

        if laptop_id not in self.cart:
            self.cart[laptop_id] = {'quantity': 0,
                                    'price': str(laptop.price)}

        if update_quantity:
            self.cart[laptop_id]['quantity'] = quantity
        else:
            self.cart[laptop_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, laptop):
        laptop_id = str(laptop.id)
        if laptop_id in self.cart:
            del self.cart[laptop_id]
            self.save()

    def __iter__(self):
        laptops_ids = self.cart.keys()
        laptops = models.Laptops.objects.filter(id__in=laptops_ids)

        for laptop in laptops:
            self.cart[str(laptop.id)]['laptop'] = laptop

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
