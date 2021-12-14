import csv
import os
from abc import ABC, abstractmethod
from typing import List, Union

from system.databases.abstract_db import AbstractDB
from system.models.users.customer import Customer
from system.models.users.user import User


class AbstractAccessUserDB(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_user(self, user_name: str) -> User:
        pass

    @abstractmethod
    def user_exists(self, user_name: str) -> bool:
        pass


class AbstractAdminUserDB(ABC):
    @abstractmethod
    def get_customer(self, user_name: str) -> Customer:
        pass

    @abstractmethod
    def get_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def set_customer_discount(self, user_name: str, discount_id: int):
        pass


class UserDB(AbstractDB, AbstractAccessUserDB, AbstractAdminUserDB):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.check_db()

    def check_db(self):
        if not os.path.exists(self.db_name + ".csv"):
            self.create_db()

    def create_db(self):
        with open(self.db_name + ".csv", "w", newline="",  encoding="utf-8") as file:
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
