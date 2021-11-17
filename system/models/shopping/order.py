"""
This module imports List from typing.
It also imports datetime from datetime.

This module contains the order class.
"""
from typing import List
from datetime import datetime


class Order:
    """
    This class deals with everything to do with the order. This includes getting
    the customer name, getting a list of the products they intend to order,
    getting the date they have ordered on and getting the subtotal of their
    order.
    """
    def __init__(self, customer_name: str, product_names: List[str], order_date: datetime, subtotal: float):

        self._customer_name = customer_name
        self._product_names = product_names
        self._order_date = order_date
        self._subtotal = subtotal

    def get_customer_name(self) -> str:
        """
        This gets the name of the customer linked to the order

        :returns: the customer name
        """
        return self._customer_name

    def get_product_names(self) -> List[str]:
        """
        This gets the the list of products the
        customer intends to order.

        :returns: the list of products
        """
        return self._product_names

    def get_order_date(self) -> datetime:
        """
        This gets the date the customer placed the order on.

        :returns: the order date
        """
        return self._order_date

    def get_subtotal(self) -> float:
        """
        This gets the subtotal of the list of items in the order

        :returns: the subtotal
        """
        return self._subtotal
