import csv
from typing import List
from system.models.users.user import User
from system.models.shopping.product import Product
from system.models.database.abstract_db_handler import AbstractUserDB
from system.models.database.abstract_db_handler import AbstractProductDB


class ProductDB(AbstractProductDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_product(self, product: Product):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([self.get_next_id(),
                             product.get_product_name(),
                             product.get_product_quantity(),
                             product.get_product_price()])

    def remove_product(self, product: Product):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] != str(self.get_product_id(product)):
                    temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def edit_product(self, product: Product, column: int, new_value: str):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == str(self.get_product_id(product)):
                    row[column] = new_value
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def subtract_product_quantity(self, product: Product, amount: int):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == str(self.get_product_id(product)):
                    quantity = int(row[2]) - amount
                    row[2] = str(quantity)
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def get_product(self, product_name: int) -> Product:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    product = Product(row[1], int(row[2]), float(row[3]))
                return product

    def get_product_id(self, product: Product) -> int:
        pass

    def get_next_id(self) -> int:
        pass

    def get_all_products(self) -> List[Product]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            products = []
            for row in reader:
                product = Product(row[1], int(row[2]), float(row[3]))
                products.append(product)
            return products


class UserDB(AbstractUserDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_user(self, user: User):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([self.get_next_id(),
                             user.get_user_name(),
                             user.get_password(),
                             user.get_is_admin()])

    def get_user(self, user_name: int) -> User:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == user_name:
                    user = User(row[1], row[2], bool(row[3]), row[4])
                return user

    def get_user_id(self, user: User) -> int:
        pass

    def get_next_id(self) -> int:
        pass

    def get_all_users(self) -> List[User]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            users = []
            for row in reader:
                user = User(row[1], row[2], bool(row[3]), row[4])
                users.append(user)
            return users
