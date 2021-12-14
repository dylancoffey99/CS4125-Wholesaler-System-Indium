"""
This module contains the Customer class. The module imports the classes
AbstractCustomerCountryDB, AbstractCustomerOrderDB, AbstractCustomerProductDB,
AbstractUserProductDB, CountryDB, OrderDB, and ProductDB from the systems database
package. It also imports the Country, DiscountCategory and Order classes from the
systems payment package, the Product class from the systems shopping package, and
the AbstractUser class from the systems users package.
"""
from typing import List, Union

from system.databases import AbstractCustomerCountryDB, AbstractCustomerOrderDB, \
    AbstractCustomerProductDB, AbstractUserProductDB, CountryDB, OrderDB, ProductDB
from system.models.payment import Country, DiscountCategory, Order
from system.models.shopping import Product
from system.models.users import AbstractUser


class Customer(AbstractUser, AbstractCustomerCountryDB, AbstractCustomerOrderDB,
               AbstractCustomerProductDB, AbstractUserProductDB):
    """
    This class represents a model of a customer and implements User,
    AbstractCustomerCountryDB, AbstractCustomerOrderDB. It also contains
    a constructor, the getter/setter methods for its parameters, and the
    implemented abstract methods.
    """

    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int,
                 discount_id: int = -1):
        """
        This constructor instantiates a customer object.

        :param user_name: Username of the user.
        :param password: Password of the user.
        :param is_admin: Admin flag of the user.
        :param country_id: Country ID of the user.
        :param discount_id: Discount ID of the user (optional).
        """
        self.variables = [user_name, password, is_admin, country_id, discount_id]
        self.order_db = OrderDB("system/databases/csv/order_db")
        self.country_db = CountryDB("system/databases/csv/country_db")
        self.product_db = ProductDB("system/databases/csv/product_db")

    def get_user_name(self) -> str:
        return self.variables[0]

    def get_password(self) -> str:
        return self.variables[1]

    def get_is_admin(self) -> int:
        return self.variables[2]

    def get_country_id(self) -> int:
        return self.variables[3]

    def get_discount_id(self) -> int:
        return self.variables[4]

    def get_country(self, country_id: int) -> Country:
        return self.country_db.get_country(country_id)

    def add_order(self, order: Order):
        self.order_db.add_order(order)

    def sub_product_quantity(self, product_name: str, quantity: int):
        self.product_db.sub_product_quantity(product_name, quantity)

    def get_product(self, product_name: str) -> Union[Product, bool]:
        return self.product_db.get_product(product_name)

    def get_all_products(self) -> List[Product]:
        return self.product_db.get_all_products()

    def set_discount_id(self, discount_id: int):
        """
        This method sets the discount ID.

        :param discount_id: Discount ID to be set to the customer.
        """
        self.variables[4] = discount_id

    def check_discount_category(self) -> DiscountCategory:
        """
        This method checks the customers discount ID to get the
        discount category they are in.

        :returns: Discount category of the customer.
        """
        if self.variables[4] == "0":
            discount = DiscountCategory(0, "Education", 0.10)
        elif self.variables[4] == "1":
            discount = DiscountCategory(1, "Small Business", 0.15)
        else:
            discount = DiscountCategory(2, "Start-up Business", 0.20)
        return discount
