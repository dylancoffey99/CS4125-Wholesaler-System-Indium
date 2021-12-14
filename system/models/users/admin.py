"""
This module contains the Admin class. The module imports the type List from the typing
module, the classes AbstractAdminOrderDB, AbstractAdminProductDB, AbstractAdminUserDB,
OrderDB, and UserDB from the systems database package, the Product class from the systems
shopping package, and the Customer and User classes from the systems users package.
"""
from typing import List

from system.databases import AbstractAdminOrderDB, AbstractAdminProductDB, OrderDB
from system.databases.user_db import AbstractAdminUserDB, UserDB
from system.models.shopping import Product
from system.models.users.customer import Customer
from system.models.users.user import User


class Admin(User, AbstractAdminProductDB, AbstractAdminUserDB, AbstractAdminOrderDB):
    """
    This class represents a model of an admin and implements User,
    AbstractAdminProductDB, AbstractAdminUserDB and AbstractAdminOrderDB.
    It also contains a constructor and the implemented abstract methods.
    """

    def __init__(self, user_name: str, password: str):
        """
        This constructor instantiates an admin object.

        :param user_name: Username of the admin.
        :param password: Password of the admin.
        """
        User.__init__(self, user_name, password, 1, -1)
        self.user_db = UserDB("system/databases/csv/user_db")
        self.order_db = OrderDB("system/databases/csv/order_db")

    def add_product(self, product: Product):
        self.product_db.add_product(product)

    def remove_product(self, product: Product):
        self.product_db.remove_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        self.product_db.edit_product(product, column, new_value)

    def get_customer(self, user_name: str) -> Customer:
        return self.user_db.get_customer(user_name)

    def get_all_customers(self) -> List[Customer]:
        return self.user_db.get_all_customers()

    def set_customer_discount(self, user_name: str, discount_id: int):
        self.user_db.set_customer_discount(user_name, discount_id)

    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        self.order_db.update_order_subtotals(user_name, discount_percentage)

    def get_customer_orders(self, user_name: str) -> List:
        return self.order_db.get_customer_orders(user_name)

    def orders_exist(self, user_name: str) -> bool:
        return bool(self.order_db.orders_exist(user_name))
