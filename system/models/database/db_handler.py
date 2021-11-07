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
            writer.writerow([self.increment_product_id(),
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

    def sub_product_quantity(self, product: Product, amount: int):
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

    def get_product(self, product_name: str) -> Product:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    product = Product(row[1], int(row[2]), float(row[3]))
                return product

    def get_product_id(self, product: Product) -> int:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == product.get_product_name():
                    product_id = int(row[0])
                return product_id

    def get_all_products(self) -> List[Product]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            products = []
            for row in reader:
                product = Product(row[1], int(row[2]), float(row[3]))
                products.append(product)
            return products

    def product_name_exists(self, product_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == product_name:
                    return True
            return False

    def increment_product_id(self) -> int:
        products = self.get_all_products()
        last_product = products[-1]
        next_id = int(self.get_product_id(last_product)) + 1
        return next_id


class UserDB(AbstractUserDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_user(self, user: User):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([self.increment_user_id(),
                             user.get_user_name(),
                             user.get_password(),
                             user.get_is_admin(),
                             user.get_country_id()])

    def get_user(self, user_name: str) -> User:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == user_name:
                    user = User(row[1], row[2], bool(row[3]), int(row[4]))
                return user

    def get_user_id(self, user: User) -> int:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == user.get_user_name():
                    user_id = int(row[0])
                return user_id

    def get_all_users(self) -> List[User]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            users = []
            for row in reader:
                user = User(row[1], row[2], bool(row[3]), int(row[4]))
                users.append(user)
            return users

    def user_name_exists(self, user_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[1] == user_name:
                    return True
            return False

    def increment_user_id(self) -> int:
        users = self.get_all_users()
        last_user = users[-1]
        next_id = int(self.get_user_id(last_user)) + 1
        return next_id
