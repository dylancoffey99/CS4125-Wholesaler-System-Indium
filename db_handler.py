# db_handler.py
# Defines ProductDB and UserDB classes implementing
# abstract methods to manipulate their respective CSV files
# Author: Dylan Coffey - 18251382

from typing import List
import csv
from stock_management import Product
from abstract_db_handler import AbstractProductDB


class ProductDB(AbstractProductDB):
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.csv = None
        self.reader = None
        self.writer = None

    def add_product(self, product: Product):
        product = product.get_product_as_list()
        with open(self._db_name + ".csv", "a", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerow(product)

    def remove_product(self, product: Product):
        temp_rows = []
        product_id = product.get_product_id()
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] != str(product_id):
                    temp_rows.append(row)
        with open(self._db_name + ".csv", "w", newline="", encoding="utf-8") as self.csv:
            self.writer = csv.writer(self.csv, delimiter=",")
            self.writer.writerows(temp_rows)

    def edit_product(self, product: Product, column: int, new_value: str):
        temp_rows = []
        product_id = product.get_product_id()
        with open(self._db_name + ".csv", "r", newline="", encoding="utf-8") as self.csv:
            self.reader = csv.reader(self.csv, delimiter=",")
            for row in self.reader:
                if row[0] == str(product_id):
                    row[column] = new_value
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
