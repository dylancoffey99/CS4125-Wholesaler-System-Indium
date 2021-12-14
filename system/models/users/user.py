"""
This module contains the User class. The module imports the type List and Union
from the typing module. It also imports the Abstract User Product Database and
the Product database from the systems database package. This module also
imports the Product class from the product module in the systems shopping
package. This module also imports the Abstract User class from the Abstract
User Module.
"""
from typing import List, Union

from system.databases import AbstractUserProductDB, ProductDB
from system.models.shopping import Product
from system.models.users import AbstractUser


class User(AbstractUser, AbstractUserProductDB):
    """
    This class represents a model of a User and implements
    AbstractUser and AbstractUserProductDB. It also contains
    a constructor and the getter methods for its parameters.
    """
    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        """
        This constructor instantiates a User object.

        :param user_name: Username of the User
        :param password: Password of the User
        :param is_admin: Identity of the User
        :param country_id: The Country of the User
        """
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        self.country_id = country_id
        self.product_db = ProductDB("system/databases/csv/product_db")

    def get_user_name(self) -> str:
        """
        This method gets a users username.

        :returns: Username of the user.
        """
        return self.user_name

    def get_password(self) -> str:
        """
        This method gets a users password.

        :returns: Password of the user.
        """
        return self.password

    def get_is_admin(self) -> int:
        """
        This method gets whether a user is admin or customer.

        :returns: Identity of the User.
        """
        return self.is_admin

    def get_country_id(self) -> int:
        """
        This method gets a users country.

        :returns: Country of the user.
        """
        return self.country_id

    def get_product(self, product_name: str) -> Union[Product, bool]:
        """
        This method gets an object of product from the database.

        :param product_name: Name of the product object.
        :returns: Product object from the database.
        """
        return self.product_db.get_product(product_name)

    def get_all_products(self) -> List[Product]:
        """
        This method gets a list of all product objects from the database.

        :returns: List of all product objects from the database.
        """
        return self.product_db.get_all_products()

    def sub_product_quantity(self, product_name: str, quantity: int):
        """
        This method subtracts the quantity of a product in the database.

        :param product_name: Name of the product.
        :param quantity: Quantity amount to subtract.
        """
        self.product_db.sub_product_quantity(product_name, quantity)

    def product_exists(self, product_name: str) -> bool:
        """
        This method checks if a product exists in the database.

        :param product_name: Name of the product.
        :returns: Boolean on whether or not the product exists.
        """
        return self.product_db.product_exists(product_name)
