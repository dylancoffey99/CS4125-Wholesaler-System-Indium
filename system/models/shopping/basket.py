from typing import List
from system.models.shopping.product import Product


class Basket:
    def __init__(self, basket_items: List[Product], basket_subtotal: int):
        self._basket_items = basket_items
        self._basket_subtotal = basket_subtotal

    def get_basket_items(self) -> List[Product]:
        return self._basket_items

    def get_basket_subtotal(self) -> int:
        return self._basket_subtotal

    def add_basket_subtotal(self, price: float):
        self._basket_subtotal += price

    def sub_basket_subtotal(self, price: float):
        if self._basket_subtotal > 0 and price < self._basket_subtotal:
            self._basket_subtotal -= price

    def add_item(self, product: Product):
        self._basket_items.append(product)

    def remove_item(self, product: Product):
        self._basket_items.remove(product)
