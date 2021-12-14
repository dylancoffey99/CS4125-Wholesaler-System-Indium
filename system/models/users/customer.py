"""
This module contains the Customer class. The module imports the Abstract
Customer Category database, Abstract Customer Order database, the Country
Database and the Order database from the systems database package. This
module also imports the Country, Discount Category and Order modules from the
systems payment package. This module also imports the Abstract User Module, and
the User class from the User module, both which are in the systems user package.
"""
from system.databases import AbstractCustomerCountryDB, AbstractCustomerOrderDB, CountryDB, OrderDB
from system.models.payment import Country, DiscountCategory, Order
from system.models.users import AbstractUser
from system.models.users.user import User


class Customer(User, AbstractUser, AbstractCustomerCountryDB, AbstractCustomerOrderDB):
    """
    This class represents a model of a Customer and implements User,
    AbstractUser, AbstractCustomerCountryDB, AbstractCustomerOrderDB.
    It also contains a constructor and the getter methods for its
    parameters.
    """
    def __init__(self, user_name: str, password: str, country_id: int, discount_id: int = -1):
        """
        This constructor instantiates a Customer object.

        :param user_name: Username of the Customer
        :param password: Password of the Customer
        :param country_id Country of the Customer
        :param discount_id: Discount Available to the Customer
        """
        User.__init__(self, user_name, password, 0, country_id)
        self.discount_id = discount_id
        self.country_db = CountryDB("system/databases/csv/country_db")
        self.order_db = OrderDB("system/databases/csv/order_db")

    def get_discount_id(self) -> int:
        """
        This method gets the discount ID of a customer.

        :returns: The discount ID.
        """
        return self.discount_id

    def set_discount_id(self, discount_id: int):
        """
        This method sets the discount ID of a customer.

        :param discount_id: Discount ID to be set to the customer.
        """
        self.discount_id = discount_id

    def check_discount_category(self) -> DiscountCategory:
        """
        This method check the discount ID of a customer to see what
        discount category the are in.

        :returns: The discount category
        """
        if self.discount_id == "0":
            discount = DiscountCategory(0, "Education", 0.10)
        elif self.discount_id == "1":
            discount = DiscountCategory(1, "Small Business", 0.15)
        else:
            discount = DiscountCategory(2, "Start-up Business", 0.20)
        return discount

    def get_country(self, country_id: int) -> Country:
        """
        This method gets an object of country from the database.

        :param country_id: Country ID of the country object.
        :returns: Country object from the database.
        """
        return self.country_db.get_country(country_id)

    def add_order(self, order: Order):
        """
        This method adds an order to the database.

        :param order: Order object to be added to the database..
        """
        self.order_db.add_order(order)
