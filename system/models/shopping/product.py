"""This module contains the Product class."""


class Product:
    """
    This class represents a model of a product, containing a constructor, the
    getter methods for its parameters, and a calculation method for the price
    of a quantity of products.
    """

    def __init__(self, product_name: str, product_quantity: int, product_price: float):
        """
        This constructor instantiates a product object.

        :param product_name: Name of the product.
        :param product_quantity: Quantity of the product.
        :param product_price: Price of the product.
        """
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price

    def get_product_name(self) -> str:
        """
        This method gets the product name.

        :returns: Name of the product.
        """
        return self.product_name

    def get_product_quantity(self) -> int:
        """
        This method gets the product quantity.

        :returns: Quantity of the product.
        """
        return self.product_quantity

    def get_product_price(self) -> float:
        """
        This method gets the product price.

        :returns: Price of the product.
        """
        return self.product_price

    def calc_price(self, quantity: int) -> float:
        """
        This method calculates the price of certain quantity
        of products.

        :param quantity: Quantity of products.
        :returns: Price of a quantity of products.
        """
        return float(quantity) * self.product_price
