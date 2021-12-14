"""
This module contains the Customer class. The module imports the classes
AbstractCustomerCountryDB, AbstractCustomerOrderDB, CountryDB, and OrderDB from
the systems database package, the Country, DiscountCategory and Order classes
from the systems payment package, and the User class from the systems users package.
"""
from system.databases import AbstractCustomerCountryDB, AbstractCustomerOrderDB, CountryDB, OrderDB
from system.models.payment import Country, DiscountCategory, Order
from system.models.users.user import User


class Customer(User, AbstractCustomerCountryDB, AbstractCustomerOrderDB):
    """
    This class represents a model of a customer and implements User,
    AbstractCustomerCountryDB, AbstractCustomerOrderDB. It also contains
    a constructor, the getter/setter methods for its parameters, and the
    implemented abstract methods.
    """
    def __init__(self, user_name: str, password: str, country_id: int, discount_id: int = -1):
        """
        This constructor instantiates a customer object.

        :param user_name: Username of the customer.
        :param password: Password of the customer.
        :param country_id Country ID of the customer.
        :param discount_id: Discount ID of the customer.
        """
        User.__init__(self, user_name, password, 0, country_id)
        self.discount_id = discount_id
        self.country_db = CountryDB("system/databases/csv/country_db")
        self.order_db = OrderDB("system/databases/csv/order_db")

    def get_discount_id(self) -> int:
        """
        This method gets the discount ID.

        :returns: Discount ID of the customer.
        """
        return self.discount_id

    def set_discount_id(self, discount_id: int):
        """
        This method sets the discount ID.

        :param discount_id: Discount ID to be set to the customer.
        """
        self.discount_id = discount_id

    def check_discount_category(self) -> DiscountCategory:
        """
        This method checks the customers discount ID to get the
        discount category they are in.

        :returns: Discount category of the customer.
        """
        if self.discount_id == "0":
            discount = DiscountCategory(0, "Education", 0.10)
        elif self.discount_id == "1":
            discount = DiscountCategory(1, "Small Business", 0.15)
        else:
            discount = DiscountCategory(2, "Start-up Business", 0.20)
        return discount

    def get_country(self, country_id: int) -> Country:
        return self.country_db.get_country(country_id)

    def add_order(self, order: Order):
        self.order_db.add_order(order)
