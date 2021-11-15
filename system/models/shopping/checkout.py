from typing import List
from system.models.users.customer import Customer
from system.models.shopping.product import Product

class Checkout:
    def __init__(self, order_id: int, order_items: List[Product], order_total: int, customer: Customer):
        self._order_id = order_id
        self._order_items = order_items
        self._order_total = order_total
        self._customer = customer

    def set_order_id(self) -> int:
        return self._order_id

    def get_order_items(self) -> List[Product]:
        return self._order_items

    def get_order_total(self) -> int: #We can just add the basket total from
        return self._order_total    #basket class, and the vat and shipping from the country class

    def get_customer(self) -> Customer:
        return self._customer

    def place_order(self):
        self #I'm not sure what to get it do here exactly