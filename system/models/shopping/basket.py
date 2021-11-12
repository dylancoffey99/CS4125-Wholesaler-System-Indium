from typing import List
from system.models.users.customer import Customer
from system.models.shopping.product import Product

class Basket:
    def __init__(self, basket_items: List[Product], basket_subtotal: int, customer: Customer):
        self._basket_items = basket_items
        self._basket_subtotal = basket_subtotal
        self._customer = customer

    def get_basket(self) -> List[Product]:
        return self._basket_items

    def get_basket_subtotal(self) -> int:
        return self._basket_subtotal

    def get_customer(self) -> Customer:
        return self._customer

    def add_item(self) -> List[Product]:
        self

    def remove_item(self) -> List[Product]:
        self
