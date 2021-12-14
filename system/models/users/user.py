"""
This module contains the User class. The module imports the type List and Union
from the typing module, the classes AbstractUserProductDB and ProductDB from the
systems database package, the Product class from the systems shopping package,
and the AbstractUser class from the systems user package.
"""
from typing import List, Union

from system.databases import AbstractUserProductDB, ProductDB
from system.models.shopping import Product
from system.models.users import AbstractUser


class User(AbstractUser, AbstractUserProductDB):
    """
    This class represents a model of a User and implements
    AbstractUser and AbstractUserProductDB. It also contains
    a constructor, the getter methods for its parameters, and
    the implemented abstract methods.
    """

    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        """
        This constructor instantiates a user object.

        :param user_name: Username of the user.
        :param password: Password of the user.
        :param is_admin: Admin flag of the user.
        :param country_id: Country ID of the User
        """
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        self.country_id = country_id
        self.product_db = ProductDB("system/databases/csv/product_db")

    def get_user_name(self) -> str:
        return self.user_name

    def get_password(self) -> str:
        return self.password

    def get_is_admin(self) -> int:
        return self.is_admin

    def get_country_id(self) -> int:
        return self.country_id

    def get_product(self, product_name: str) -> Union[Product, bool]:
        return self.product_db.get_product(product_name)

    def get_all_products(self) -> List[Product]:
        return self.product_db.get_all_products()

    def sub_product_quantity(self, product_name: str, quantity: int):
        self.product_db.sub_product_quantity(product_name, quantity)

    def product_exists(self, product_name: str) -> bool:
        return self.product_db.product_exists(product_name)
