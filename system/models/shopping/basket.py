from typing import List
from system.models.users.customer import Customer
from system.models.shopping.product import Product

class Basket:
    def __init__(self, basket_items: List[Product], customer: Customer):
        self._basket_items = basket_items
        self._customer = customer

    def set_order_id(self) -> int:
        return self._order_id

    def get_basket(self) -> List[Product]:
        return self._basket_items

    def get_customer(self) -> Customer:
        return self._customer

    def get_basket_as_list(self) -> List:
        return [self._order_id, self._basket_items, self._customer]