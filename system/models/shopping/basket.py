"""
This module contains the Basket class. The module imports the type List from the typing
module, and the Product class from the product module, in the systems shopping package.
"""
from typing import List
from system.models.shopping.product import Product


class Basket:
    """
    This class represents a model of a basket, containing a constructor, and
    the getter/setter methods for its parameters.
    """
    def __init__(self, basket_items: List[Product], basket_subtotal: float):
        """
        This constructor instantiates a basket object.

        :param basket_items: List of the basket items.
        :param basket_subtotal: Price subtotal of the baskets items.
        """
        self.basket_items = basket_items
        self.basket_subtotal = basket_subtotal

    def get_basket_items(self) -> List[Product]:
        """
        This method gets the basket items.

        :returns: List of the basket items.
        """
        return self.basket_items

    def get_basket_subtotal(self) -> float:
        """
        This method gets the basket subtotal.

        :returns: Price subtotal of the baskets items.
        """
        return self.basket_subtotal

    def add_basket_subtotal(self, price: float):
        """
        This method adds a price to the basket subtotal.

        :param price: Price to be added to the basket subtotal.
        """
        self.basket_subtotal += price

    def sub_basket_subtotal(self, price: float):
        """
        This method subtracts a price from the basket subtotal.

        :param price: Price to be subtracted from the basket subtotal.
        """
        if self.basket_subtotal > 0 and price <= self.basket_subtotal:
            self.basket_subtotal -= price

    def add_item(self, product: Product):
        """
        This method adds an item to the basket.

        :param product: Product to be added to the basket items.
        """
        self.basket_items.append(product)

    def remove_item(self, product: Product):
        """
        This method removes an item from the basket.

        :param product: Product to be removed from the basket items.
        """
        self.basket_items.remove(product)

    def clear_items(self):
        """
        This method clears all items from the basket, and resets
        the basket subtotal to zero.
        """
        self.basket_items.clear()
        self.basket_subtotal = 0

    def item_exists(self, product_name: str) -> bool:
        """
        This method checks if a product already exists in the
        basket.

        :param product_name: Product name of product to be checked.
        :returns: Boolean on whether or not a product exists.
        """
        for product in self.basket_items:
            if product_name == product.get_product_name():
                return True
        return False
