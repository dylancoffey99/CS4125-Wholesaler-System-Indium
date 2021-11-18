"""
This module contains the Product class. The module imports the AbstractSubject
class from observer module, in the systems shopping package.
"""
from system.models.shopping.observer import AbstractSubject


class Product(AbstractSubject):
    """
    This class represents a model of a product and implements AbstractSubject.
    The class contains a constructor, getter/setter methods for its parameters,
    and the implemented abstract methods.
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
        self.observers = []

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

    def set_product_quantity(self, product_quantity: int):
        """
        This method sets the product quantity, and notifies the observers.

        :param product_quantity: Product quantity to be set to the product.
        """
        self.product_quantity = product_quantity
        self.notify()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()
