"""
From the package typing, we are importing List.

From the product model in the shipping folder, we
are importing the product class as it contains the
products to be in the basket.
"""
from typing import List
from system.models.shopping.product import Product


class Basket:
    """
    This is the basket class which includes a list of all the
    functions to be completed within the basket of the
    program.
    """
    def __init__(self, basket_items: List[Product], basket_subtotal: int):
        """
               Parameters
               ----------
               basket_items : List[Product]
                   The list of items in the basket
               basket_subtotal : int
                   The subtotal of all the items in the basket
               """
        self._basket_items = basket_items
        self._basket_subtotal = basket_subtotal

    def get_basket_items(self) -> List[Product]:
        """
        This gets the list of items within the basket.

        :returns: This returns a list of products
        """
        return self._basket_items

    def get_basket_subtotal(self) -> int:
        """
        This is gets the subtotal of all the items in the basket.

        :returns: this returns the basket subtotal value
        """
        return self._basket_subtotal

    def add_basket_subtotal(self, price: float):
        """
        This is adds a value to the the previously calculated
        basket subtotal

        :param price: float
        :returns: the basket subtotal with the added price
        """
        self._basket_subtotal += price

    def sub_basket_subtotal(self, price: float):
        """
        This is subtracts a value from the previously
        calculated busket subtotal. It also checks
        that the basket value is not at 0 as there
        cannot be a minus subtotal.

        :param price: float
        :returns: the basket subtotal less the price
        """
        if self._basket_subtotal > 0 and price < self._basket_subtotal:
            self._basket_subtotal -= price

    def add_item(self, product: Product):
        """
        This is where you add an item to the basket.

        :param product: Product(this is from the product class)
        """
        self._basket_items.append(product)

    def remove_item(self, product: Product):
        """
        This is where you remove an item to the basket.

        :param product: Product(this is from the product class)
        """
        self._basket_items.remove(product)
