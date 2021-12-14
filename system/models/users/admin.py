"""
This module contains the Admin class. The module imports the type List from
the typing module, the Abstract Admin Order database, Abstract Admin Product
Database and the Order database from the systems database package. This
module also imports the Abstract Admin User database class and the User
database class from the user_db module from the systems database package.
This module also imports the Product class from the product module in the
systems shopping package. This module also imports the Abstract User class
from the Abstract User Module, the Customer class from the Customer module and
the User class from the User module, all which are in the systems user package.
"""
from typing import List

from system.databases import AbstractAdminOrderDB, AbstractAdminProductDB, OrderDB
from system.databases.user_db import AbstractAdminUserDB, UserDB
from system.models.shopping import Product
from system.models.users import AbstractUser
from system.models.users.customer import Customer
from system.models.users.user import User


class Admin(User, AbstractUser, AbstractAdminProductDB, AbstractAdminUserDB, AbstractAdminOrderDB):
    """
    This class represents a model of a Admin and implements User,
    AbstractUser, AbstractAdminProductDB, AbstractAdminUserDB,
    AbstractAdminOrderDB. It also contains a constructor and
    the getter methods for its parameters.
    """
    def __init__(self, user_name: str, password: str):
        """
        This constructor instantiates a Admin object.

        :param user_name: Username of the Admin
        :param password: Password of the Admin
        """
        User.__init__(self, user_name, password, 1, -1)
        self.user_db = UserDB("system/databases/csv/user_db")
        self.order_db = OrderDB("system/databases/csv/order_db")

    def add_product(self, product: Product):
        """
        This method adds a product to the database.

        :param product: Product object to be added to the database.
        """
        self.product_db.add_product(product)

    def remove_product(self, product: Product):
        """
        This method removes a product from the database.

        :param product: Product object to be removed to the database.
        """
        self.product_db.remove_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        """
        This method edits a product in the database.

        :param product: Product object to be edited in the database.
        :param column: Column of the row in the database to edit.
        :param new_value: New value to replace the chosen column.
        """
        self.product_db.edit_product(product, column, new_value)

    def get_customer(self, user_name: str) -> Customer:
        """
        This method gets an object of customer from the database.

        :param user_name: Username of the customer.
        :returns: Customer object from the database.
        """
        return self.user_db.get_customer(user_name)

    def get_all_customers(self) -> List[Customer]:
        """
        This method gets a list of all customer objects from the database.

        :returns: List of all customer objects from the database.
        """
        return self.user_db.get_all_customers()

    def set_customer_discount(self, user_name: str, discount_id: int):
        """
        This method sets the discount ID of a customer in the database.

        :param user_name: Username of the customer.
        :param discount_id: Discount ID to be set to the customer.
        """
        self.user_db.set_customer_discount(user_name, discount_id)

    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        """
        This method updates the order subtotals of a customer by discounting them
        using a discount percentage.

        :param user_name: Username of the customer.
        :param discount_percentage: Discount percentage to be used.
        """
        self.order_db.update_order_subtotals(user_name, discount_percentage)

    def get_customer_orders(self, user_name: str) -> List:
        """
        This method gets a list of a customers orders from the database.

        :param user_name: Username of the customer.
        :returns: List of the customers orders from the database.
        """
        return self.order_db.get_customer_orders(user_name)

    def orders_exist(self, user_name: str) -> bool:
        """
        This method checks if a customers orders exist in the database.

        :param user_name: Username of the customer.
        :returns: Boolean on whether or not a customers orders exist.
        """
        return bool(self.order_db.orders_exist(user_name))
