# db_handler.py
# Defines ProductDB and UserDB classes implementing
# abstract methods to manipulate their respective CSV files
# Author: Dylan Coffey - 18251382

import csv
import abstract_db_handler as db
from stock_management import Product


class ProductDB(db.AbstractProductDB):
    def __init__(self, db_name):
        self._db_name = db_name
        self.csv = None
        self.reader = None
        self.writer = None

    def add_product(self, product: Product):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            prod_id = product.get_product_id()
            name = product.get_product_name()
            quantity = product.get_product_quantity()
            price = product.get_product_price()

            new_row = [prod_id, name, quantity, price]
            self.writer.writerow(new_row)

    def remove_product(self, product_id):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] != product_id:
                    temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def edit_product(self, product_id, column, new_value):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == product_id:
                    row[column] = new_value
                temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def get_product(self, product_id):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == product_id:
                    # return product with all elements
                    return Product(row[0], row[1], row[2], row[3])
            return "Error: that product ID doesn't exist"

    def get_product_id(self, product_name):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[1] == product_name:
                    return row[0]
            return "Error: that product name doesn't exist"

    def get_all_products(self):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            next(self.reader)
            product_list = []
            for row in self.reader:
                product = Product(row[0], row[1], row[2], row[3])
                product_list.append(product)
            return product_list


class UserDB(db.AbstractUserDB):
    def __init__(self, db_name):
        self._db_name = db_name
        self.csv = None
        self.reader = None
        self.writer = None

    def add_user(self, user):
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerow(user)

    def remove_user(self, user_id):
        temp_rows = []
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] != user_id:
                    temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def get_user(self, user_id):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == user_id:
                    return row
            return "Error: that user ID doesn't exist"

    def get_user_id(self, user_name):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[1] == user_name:
                    return row[0]
            return "Error: that user name doesn't exist"

    def get_all_users(self):
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            next(self.reader)
            temp_rows = []
            for row in self.reader:
                temp_rows.append(row)
            return temp_rows
