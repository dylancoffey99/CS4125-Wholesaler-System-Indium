import csv
from typing import List
from datetime import datetime
from system.models.users.user import User
from system.models.shopping.order import Order
from system.models.shopping.product import Product
from system.models.shopping.country import Country
from system.database.abstract_db_handler import AbstractUserDB
from system.database.abstract_db_handler import AbstractOrderDB
from system.database.abstract_db_handler import AbstractProductDB
from system.database.abstract_db_handler import AbstractCountryDB


class ProductDB(AbstractProductDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_product(self, product: Product):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([product.get_product_name(), product.get_product_quantity(),
                             product.get_product_price()])

    def remove_product(self, product: Product):
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
            next(reader)
            for row in reader:
                if row[0] == product_name:
                    return Product(row[0], int(row[1]), float(row[2]))
            return False

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
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([user.get_user_name(), user.get_password(),
                             user.get_is_admin(), user.get_country_id()])

    def get_user(self, user_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    return User(row[0], row[1], int(row[2]), int(row[3]))
            return False

    def get_all_users(self) -> List[User]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            users = []
            for row in reader:
                user = User(row[0], row[1], int(row[2]), int(row[3]))
                users.append(user)
            return users

    def user_exists(self, user_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False


class OrderDB(AbstractOrderDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_order(self, order: Order):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            product_names = order.get_product_names()
            for i in range(len(product_names)):
                writer.writerow([order.get_customer_name(), product_names[i],
                                 order.get_order_date(), order.get_subtotal()])

    def get_customer_orders(self, customer_name: str) -> List:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            orders = []
            for row in reader:
                order = []
                if row[0] == customer_name:
                    order.append(row[0])
                    order.append(row[1])
                    order.append(datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f'))
                    order.append(float(row[3]))
                orders.append(order)
            return orders

class CountryDB(AbstractCountryDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def get_country(self, country_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[1] == country_name:
                    return Country(row[0], row[1], int(row[2]), int(row[3]))
            return False

    def get_all_countries(self) -> List[Country]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            countries = []
            for row in reader:
                country = Country(row[0], row[1], int(row[2]), int(row[3]))
                countries.append(country)
            return countries

