"""
This module contains the Basket class. The module imports the type List from the
typing module, the Product class from the product module, and the AbstractSubject
class from observer module, both in the systems shopping package.
"""
from typing import List, Tuple

from system.models.shopping import AbstractSubject, Product
from system.models.users.customer import Customer


class Basket(AbstractSubject):
    """
    This class represents a model of a basket and implements AbstractSubject.
    It contains a constructor, the getter/setter methods for its parameters,
    and the implemented abstract methods.
    """

    def __init__(self, basket_items: List[Product], basket_subtotal: float):
        """
        This constructor instantiates a basket object.

        :param basket_items: List of the basket items.
        :param basket_subtotal: Price subtotal of the baskets items.
        """
        self.basket_items = basket_items
        self.basket_subtotal = basket_subtotal
        self.observers = []

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
        self.notify()

    def sub_basket_subtotal(self, price: float):
        """
        This method subtracts a price from the basket subtotal.

        :param price: Price to be subtracted from the basket subtotal.
        """
        if self.basket_subtotal > 0 and price <= self.basket_subtotal:
            self.basket_subtotal -= price
            self.notify()

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

    def calc_subtotals(self, customer: Customer) -> Tuple:
        """
        This method calculates the order subtotal of a customers basket,
        including the basket subtotal, the VAT cost, and the shipping cost.
        A discount is then calculated and returned by Customer, and finally
        subtracted from the order subtotal.

        :param customer: Object of the customer.
        :returns: Subtotals of the customers order.
        """
        country = customer.get_country(customer.get_country_id())
        basket_subtotal = self.basket_subtotal
        vat_cost = basket_subtotal * country.get_vat_percentage()
        shipping_cost = country.get_shipping_cost()
        order_subtotal = (basket_subtotal + vat_cost + shipping_cost)
        discount = 0
        if customer.get_discount_id() != -1:
            discount_category = customer.check_discount_category()
            discount = discount_category.calc_discount(order_subtotal)
            order_subtotal -= discount
        return basket_subtotal, vat_cost, shipping_cost, discount, order_subtotal

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
