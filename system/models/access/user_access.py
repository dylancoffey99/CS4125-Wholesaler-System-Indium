"""
This module contains the UserAccess class. The module imports the module hashlib,
the type List from the typing module, the classes AbstractAccessCountryDB,
AbstractAccessUserDB, CountryDB and UserDB from the systems database package, and
the classes Admin, Customer, and User from the systems users package.
"""
import hashlib
from typing import List

from system.databases import AbstractAccessCountryDB, CountryDB
from system.databases.user_db import AbstractAccessUserDB, UserDB
from system.models.users.admin import Admin
from system.models.users.customer import Customer
from system.models.users.user import User


class UserAccess(AbstractAccessCountryDB, AbstractAccessUserDB):
    """
    This class represents a model of user access and implements
    AbstractAccessCountryDB and AbstractAccessUserDB. It also contains
    a constructor, password verifying and user creating methods, and the
    implemented abstract methods.
    """

    def __init__(self):
        """This constructor instantiates a user access object."""
        self.user_db = UserDB("system/databases/csv/user_db")
        self.country_db = CountryDB("system/databases/csv/country_db")

    def add_customer(self, customer: Customer):
        self.user_db.add_customer(customer)

    def get_user(self, user_name) -> User:
        return self.user_db.get_user(user_name)

    def user_exists(self, user_name) -> bool:
        return self.user_db.user_exists(user_name)

    def get_country_names(self) -> List:
        return self.country_db.get_country_names()

    def get_country_dict(self) -> dict:
        return self.country_db.get_country_dict()

    def create_user(self, user_name: str, password: str, is_admin: int, country_id: int,
                    discount_id: int = -1):
        """
        This method acts as a factory method for the user classes. It creates an
        admin/customer object depending on the value of the users admin flag.

        :param user_name: Username of the user.
        :param password: Password of the user.
        :param is_admin: Admin flag of the user.
        :param country_id: Country ID of the user.
        :param discount_id: Discount ID of the user (optional).
        :returns: Customer/Admin object of the user.
        """
        if is_admin == 1:
            user = Admin(user_name, self.hash_password(password), is_admin, -1)
        else:
            user = Customer(user_name, self.hash_password(password), is_admin,
                            country_id, discount_id)
        return user

    def verify_password(self, password: str, db_password: str) -> bool:
        """
        This method verifies that when the password entered is hashed,
        it equals the password in the database.

        :param password: Password to be hashed.
        :param db_password: Database password to be compared against.
        :returns: Boolean value on whether or not the passwords equal.
        """
        return bool(self.hash_password(password) == db_password)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        This method hashes a password using SHA-256.

        :returns: SHA-256 Hashed password.
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
