import csv
from typing import List
from datetime import datetime
from system.database import abstract_db_handler as db
from system.models.users.user import User
from system.models.users.customer import Customer
from system.models.shopping.order import Order
from system.models.shopping.product import Product
from system.models.shopping.country import Country


class ProductDB(db.AbstractProductDB):
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


class UserDB(db.AbstractUserDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_customer(self, customer: Customer):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([customer.get_user_name(), customer.get_password(), customer.get_is_admin(),
                             customer.get_country_id(), customer.get_discount_id()])

    def get_user(self, user_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    return User(row[0], row[1], int(row[2]), int(row[3]))
            return False

    def get_customer(self, user_name: str):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    return Customer(row[0], row[1], int(row[2]), int(row[4]))
            return False

    def get_all_customers(self) -> List[Customer]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
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
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    row[4] = str(discount_id)
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def user_exists(self, user_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False


class OrderDB(db.AbstractOrderDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def add_order(self, order: Order):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            product_names = order.get_product_names()
            for product, _ in enumerate(product_names):
                writer.writerow([order.get_customer_name(), product_names[product],
                                 order.get_order_date(), order.get_order_subtotal()])

    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    subtotal = float(row[3])
                    discount = subtotal * discount_percentage
                    row[3] = str(subtotal - discount)
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def get_customer_orders(self, user_name: str) -> List:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            orders = []
            for row in reader:
                order = []
                if row[0] == user_name:
                    order.append(row[0])
                    order.append(row[1])
                    order.append(datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f'))
                    order.append(float(row[3]))
                    orders.append(order)
            return orders

    def orders_exist(self, user_name: str) -> bool:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False


class CountryDB(db.AbstractCountryDB):
    def __init__(self, db_name: str):
        self._db_name = db_name

    def get_country(self, country_id: int):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == str(country_id):
                    return Country(int(row[0]), row[1], float(row[2]), float(row[3]))
            return False

    def get_all_countries(self) -> List[Country]:
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            countries = []
            for row in reader:
                country = Country(int(row[0]), row[1], float(row[2]), float(row[3]))
                countries.append(country)
            return countries
