import csv
from typing import List
from system.models.users.user import User
from system.models.shopping.product import Product
from system.database.abstract_db_handler import AbstractUserDB
from system.database.abstract_db_handler import AbstractProductDB


class ProductDB(AbstractProductDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_product(self, product: Product):
        if self.product_exists(product.get_product_name()):
            print("Error: product name already exists")
        else:
            with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow([product.get_product_name(), product.get_product_quantity(),
                                 product.get_product_price()])

    def remove_product(self, product: Product):
        if not self.product_exists(product.get_product_name()):
            print("Error: product does not exist")
        else:
            temp_rows = []
            with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    if row[0] != product.get_product_name():
                        temp_rows.append(row)
            with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerows(temp_rows)

    def edit_product(self, product: Product, column: int, new_value: str):
        if not self.product_exists(product.get_product_name()):
            print("Error: product does not exist")
        else:
            if column == 0 and self.product_exists(new_value):
                print("Error: product name already exists")
            else:
                temp_rows = []
                with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file, delimiter=",")
                    for row in reader:
                        if row[0] == product.get_product_name():
                            row[column] = new_value
                        temp_rows.append(row)
                with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file, delimiter=",")
                    writer.writerows(temp_rows)

    def sub_product_quantity(self, product: Product, amount: int):
        if not self.product_exists(product.get_product_name()):
            print("Error: product does not exist")
        else:
            temp_rows = []
            with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    if row[0] == product.get_product_name():
                        quantity = int(row[1]) - amount
                        row[1] = str(quantity)
                    temp_rows.append(row)
            with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerows(temp_rows)

    def get_product(self, product_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    product = Product(row[0], int(row[1]), float(row[2]))
                    return product
            return print("Error: product does not exist")

    def get_all_products(self) -> List[Product]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            products = []
            for row in reader:
                product = Product(row[0], int(row[1]), float(row[2]))
                products.append(product)
            return products

    def product_exists(self, product_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    return True
            return False


class UserDB(AbstractUserDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_user(self, user: User):
        if self.user_exists(user.get_user_name()):
            print("Error: username already exists")
        else:
            with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow([user.get_user_name(), user.get_password(),
                                 user.get_is_admin(), user.get_country_id()])

    def get_user(self, user_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    user = User(row[0], row[1], bool(row[2]), int(row[3]))
                    return user
            return print("Error: user does not exist")

    def get_all_users(self) -> List[User]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            users = []
            for row in reader:
                user = User(row[0], row[1], bool(row[2]), int(row[3]))
                users.append(user)
            return users

    def user_exists(self, user_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False
