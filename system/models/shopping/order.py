from typing import List
from datetime import date


class Order:
    def __init__(self, customer_name: str, product_names: List[str], order_date: date, subtotal: float):
        self._customer_name = customer_name
        self._product_names = product_names
        self._order_date = order_date
        self._subtotal = subtotal

    def get_customer_name(self) -> str:
        return self._customer_name

    def get_product_names(self) -> List[str]:
        return self._product_names

    def get_order_date(self) -> date:
        return self._order_date

    def get_subtotal(self) -> float:
        return self._subtotal
