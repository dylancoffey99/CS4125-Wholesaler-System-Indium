"""
This module contains the UserAccess class. The module imports hashlib and
the type List from the typing module. It also imports the Abstract Access
Country database and the Country Database from the systems database package.
This module also imports the Abstract Access User database class and the User
database class from the user_db module from the systems database package.
This module also imports the Customer class from the Customer module and
the User class from the User module, all which are in the systems user package.
"""
import hashlib
from typing import List

from system.databases import AbstractAccessCountryDB, CountryDB
from system.databases.user_db import AbstractAccessUserDB, UserDB
from system.models.users.customer import Customer
from system.models.users.user import User


class UserAccess(AbstractAccessCountryDB, AbstractAccessUserDB):
    """
    This class represents a model of user access and implements AbstractAccessCountryDB,
    AbstractAccessUserDB. It also contains a constructor and the getter methods for its
    parameters.
    """
    def __init__(self):
        """
        This constructor instantiates the access user object.
        """
        self.user_db = UserDB("system/databases/csv/user_db")
        self.country_db = CountryDB("system/databases/csv/country_db")

    def add_customer(self, customer: Customer):
        """
        This method adds a customer to the database.

        :param customer: Customer object to be added to the database.
        """
        self.user_db.add_customer(customer)

    def get_user(self, user_name) -> User:
        """
        This method gets an object of user from the database.

        :param user_name: Username of the user.
        :returns: User object from the database.
        """
        return self.user_db.get_user(user_name)

    def user_exists(self, user_name) -> bool:
        """
        This method checks if a user exists in the database.

        :param user_name: Username of the user.
        :returns: Boolean on whether or not the user exists.
        """
        return self.user_db.user_exists(user_name)

    def get_country_names(self) -> List:
        """
        This method gets a list of country names from the database.

        :returns: List of country names from the database.
        """
        return self.country_db.get_country_names()

    def get_country_dict(self) -> dict:
        """
        This method gets a dictionary of country names and IDs from the database.

        :returns: Dictionary of country names and IDs from the database.
        """
        return self.country_db.get_country_dict()

    def verify_password(self, password: str) -> bool:
        """
        This method verifies the password of a user.

        :param password: Password of the user.
        :returns: True or false depending if password matches hashed password.
        """
        return bool(password == self.hash_password(password))

    def is_admin(self, user_name) -> bool:
        """
        This method verifies if a user is admin or not.

        :param user_name: Username of the user.
        :returns: True or false depending if the user is admin or not.
        """
        user = self.get_user(user_name)
        return bool(user.get_is_admin() == 1)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        This method hashes the password of a user.

        :param password: Password of the user.
        :returns: The hashed password of the user.
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
