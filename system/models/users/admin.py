"""
This module contains the Admin class. The module imports the type List and
Union from the typing module, the classes AbstractAdminOrderDB, AbstractAdminProductDB,
AbstractUserProductDB, AbstractAdminUserDB, OrderDB, ProductDB, and UserDB from the
systems database package. It also imports the Product class from the systems shopping
package, and the AbstractUser and Customer classes from the systems users package.
"""
from typing import List, Union

from system.databases import AbstractAdminOrderDB, AbstractAdminProductDB, AbstractUserProductDB, \
    OrderDB, ProductDB
from system.databases.user_db import AbstractAdminUserDB, UserDB
from system.models.shopping import Product
from system.models.users import AbstractUser
from system.models.users.customer import Customer


class Admin(AbstractUser, AbstractAdminOrderDB, AbstractAdminProductDB, AbstractUserProductDB,
            AbstractAdminUserDB):
    """
    This class represents a model of an admin and implements User,
    AbstractAdminOrderDB, AbstractAdminProductDB, AbstractUserProductDB,
    and AbstractAdminUserDB. It also contains a constructor and the
    implemented abstract methods.
    """

    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int,
                 discount_id: int = -1):
        """
        This constructor instantiates an admin object.

        :param user_name: Username of the user.
        :param password: Password of the user.
        :param is_admin: Admin flag of the user.
        :param country_id: Country ID of the user.
        :param discount_id: Discount ID of the user (optional).
        """
        self.variables = [user_name, password, is_admin, country_id, discount_id]
        self.user_db = UserDB("system/databases/csv/user_db")
        self.order_db = OrderDB("system/databases/csv/order_db")
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

    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        self.order_db.update_order_subtotals(user_name, discount_percentage)

    def get_customer_orders(self, user_name: str) -> List:
        return self.order_db.get_customer_orders(user_name)

    def orders_exist(self, user_name: str) -> bool:
        return bool(self.order_db.orders_exist(user_name))

    def add_product(self, product: Product):
        self.product_db.add_product(product)

    def remove_product(self, product: Product):
        self.product_db.remove_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        self.product_db.edit_product(product, column, new_value)

    def product_exists(self, product_name: str) -> bool:
        return self.product_db.product_exists(product_name)

    def get_product(self, product_name: str) -> Union[Product, bool]:
        return self.product_db.get_product(product_name)

    def get_all_products(self) -> List[Product]:
        return self.product_db.get_all_products()

    def get_customer(self, user_name: str) -> Customer:
        return self.user_db.get_customer(user_name)

    def get_all_customers(self) -> List[Customer]:
        return self.user_db.get_all_customers()

    def set_customer_discount(self, user_name: str, discount_id: int):
        self.user_db.set_customer_discount(user_name, discount_id)
