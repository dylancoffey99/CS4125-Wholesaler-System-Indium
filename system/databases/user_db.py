"""
This module contains the UserDB, AbstractAccessUserDB and AbstractAdminUserDB
classes. The module imports the modules csv and os, the type List and Union from the
typing module, the class AbstractDB from the systems databases package, the classes
Customer and User from the systems users package.
"""
import csv
import os
from abc import ABC, abstractmethod
from typing import List, Union

from system.databases.abstract_db import AbstractDB
from system.models.users.customer import Customer
from system.models.users.user import User


class AbstractAccessUserDB(ABC):
    """
    This abstract class represents an interface for the user access and user database.
    It contains the abstract methods to be implemented into the user access and user
    database classes.
    """

    @abstractmethod
    def add_customer(self, customer: Customer):
        """
        This method adds a customer to the database.

        :param customer: Customer object to be added to the database.
        """

    @abstractmethod
    def get_user(self, user_name: str) -> User:
        """
        This method gets an object of user from the database.

        :param user_name: Username of the user.
        :returns: User object from the database.
        """

    @abstractmethod
    def user_exists(self, user_name: str) -> bool:
        """
        This method checks if a user exists in the database.

        :param user_name: Username of the user.
        :returns: Boolean on whether or not the user exists.
        """


class AbstractAdminUserDB(ABC):
    """
    This abstract class represents an interface for the admin and user database.
    It contains the abstract methods to be implemented into the admin and user
    database classes.
    """

    @abstractmethod
    def get_customer(self, user_name: str) -> Customer:
        """
        This method gets an object of customer from the database.

        :param user_name: Username of the customer.
        :returns: Customer object from the database.
        """

    @abstractmethod
    def get_all_customers(self) -> List[Customer]:
        """
        This method gets a list of all customer objects from the database.

        :returns: List of all customer objects from the database.
        """

    @abstractmethod
    def set_customer_discount(self, user_name: str, discount_id: int):
        """
        This method sets the discount ID of a customer in the database.

        :param user_name: Username of the customer.
        :param discount_id: Discount ID to be set to the customer.
        """


class UserDB(AbstractDB, AbstractAccessUserDB, AbstractAdminUserDB):
    """
    This class represents a user database and implements AbstractDB,
    AbstractAccessUserDB, and AbstractAdminUserDB. It contains a constructor,
    and the implemented abstract methods.
    """

    def __init__(self, db_name: str):
        """
        This constructor instantiates a user database object.

        :param db_name: Name of the database and its file path.
        """
        self.db_name = db_name
        self.check_db()

    def check_db(self):
        if not os.path.exists(self.db_name + ".csv"):
            self.create_db()

    def create_db(self):
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["user_name", "password", "is_admin",
                             "country_id", "discount_id"])

    def add_customer(self, customer: Customer):
        with open(self.db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([customer.get_user_name(), customer.get_password(),
                             customer.get_is_admin(), customer.get_country_id(),
                             customer.get_discount_id()])

    def get_user(self, user_name: str) -> Union[User, bool]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    return User(row[0], row[1], int(row[2]), int(row[3]))
            return False

    def get_customer(self, user_name: str) -> Union[Customer, bool]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    return Customer(row[0], row[1], int(row[2]), int(row[4]))
            return False

    def get_all_customers(self) -> List[Customer]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            customers = []
            for row in reader:
                if row[2] == str(0):
                    customer = Customer(row[0], row[1], int(row[2]), int(row[4]))
                    customers.append(customer)
            return customers

    def set_customer_discount(self, user_name: str, discount_id: int):
        temp_rows = []
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    row[4] = str(discount_id)
                temp_rows.append(row)
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def user_exists(self, user_name: str) -> bool:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False
