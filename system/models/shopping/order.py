"""
This module contains the Order class. The module imports the type List from the
typing module, and the datetime class from the datetime module.
"""
from typing import List
from datetime import datetime


class Order:
    """
    This class represents a model of an order, containing a constructor, and
    the getter methods for its parameters.
    """
    def __init__(self, customer_name: str, product_names: List[str], order_date: datetime,
                 order_subtotal: float):
        """
        This constructor instantiates an order object.

        :param customer_name: Name of the orders customer.
        :param product_names: List of the orders product names.
        :param order_date: Date/time of the order.
        :param order_subtotal: Price subtotal of the orders products.
        """
        self.customer_name = customer_name
        self.product_names = product_names
        self.order_date = order_date
        self.order_subtotal = order_subtotal

    def get_customer_name(self) -> str:
        """
        This method gets the order customer name.

        :returns: Name of the orders customer.
        """
        return self.customer_name

    def get_product_names(self) -> List[str]:
        """
        This method gets the order product names.

        :returns: List of the orders product names.
        """
        return self.product_names

    def get_order_date(self) -> datetime:
        """
        This method gets the order date/time.

        :returns: Date/time of the order.
        """
        return self.order_date

    def get_order_subtotal(self) -> float:
        """
        This method gets the order subtotal.

        :returns: Price subtotal of the orders products.
        """
        return self.order_subtotal
