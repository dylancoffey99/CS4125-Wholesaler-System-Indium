import csv
from typing import List
from system.models.users.user import User
from system.models.shopping.product import Product
from system.models.database.abstract_db_handler import AbstractUserDB
from system.models.database.abstract_db_handler import AbstractProductDB


class ProductDB(AbstractProductDB):
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.csv = None
        self.reader = None
        self.writer = None

    def add_product(self, product: Product):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerow(product.get_product_as_list())

    def remove_product(self, product: Product):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] != str(product.get_product_id()):
                    temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def edit_product(self, product: Product, column: int, new_value: str):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == str(product.get_product_id()):
                    row[column] = new_value
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def edit_product_quantity(self, product: Product, operation: bool, value: int):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == str(product.get_product_id()):
                    if operation:
                        row[2] += value
                    else:
                        row[2] -= value
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def get_product(self, product_id: int) -> Product:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == str(product_id):
                    product = Product(int(row[0]), row[1], int(row[2]), float(row[3]))
                return product

    def get_all_products(self) -> List[Product]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            next(self.reader)
            products = []
            for row in self.reader:
                product = Product(int(row[0]), row[1], int(row[2]), float(row[3]))
                products.append(product)
            return products


class UserDB(AbstractUserDB):
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.csv = None
        self.reader = None
        self.writer = None

    def add_user(self, user: User):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerow(user.get_user_as_list())

    def get_user(self, user_id: int) -> User:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == str(user_id):
                    user = User(int(row[0]), row[1], row[2], bool(row[3]))
                return user

    def get_all_users(self) -> List[User]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            next(self.reader)
            users = []
            for row in self.reader:
                user = User(int(row[0]), row[1], row[2], bool(row[3]))
                users.append(user)
            return users
