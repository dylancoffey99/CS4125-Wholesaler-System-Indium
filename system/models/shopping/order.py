from typing import List
from system.models.users.customer import Customer
from system.models.shopping.product import Product


class Order:
    def __init__(self, order_id: int, order_items: List[Product], customer: Customer):
        self._order_id = order_id
        self._order_items = order_items
        self._customer = customer

    def get_order_id(self) -> int:
        return self._order_id

    def get_order_items(self) -> List[Product]:
        return self._order_items

    def get_customer(self) -> Customer:
        return self._customer

    def get_order_as_list(self) -> List:
        return [self._order_id, self._order_items, self._customer]