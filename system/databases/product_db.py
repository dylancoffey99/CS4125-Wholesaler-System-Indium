"""
This module contains the ProductDB, AbstractAdminProductDB and AbstractUserProductDB
classes. The module imports the modules csv and os, the type List and Union from the
typing module, the class Product from the product module in the systems shopping package,
and the class AbstractDB from the abstract_db module, in the systems databases package.
"""
import csv
import os
from abc import ABC, abstractmethod
from typing import List, Union

from system.databases.abstract_db import AbstractDB
from system.models.shopping import Product


class AbstractAdminProductDB(ABC):
    """
    This abstract class represents an interface for the admin and product database.
    It contains the abstract methods to be implemented into the admin and product
    database classes.
    """

    @abstractmethod
    def add_product(self, product: Product):
        """
        This method adds a product to the database.

        :param product: Product object to be added to the database.
        """

    @abstractmethod
    def remove_product(self, product: Product):
        """
        This method removes a product from the database.

        :param product: Product object to be removed to the database.
        """

    @abstractmethod
    def edit_product(self, product: Product, column: int, new_value: str):
        """
        This method edits a product in the database.

        :param product: Product object to be edited in the database.
        :param column: Column of the row in the database to edit.
        :param new_value: New value to replace the chosen column.
        """


class AbstractUserProductDB(ABC):
    """
    This abstract class represents an interface for the user and product database.
    It contains the abstract methods to be implemented into the user and product
    database classes.
    """

    @abstractmethod
    def get_product(self, product_name: str) -> Union[Product, bool]:
        """
        This method gets an object of product from the database.

        :param product_name: Name of the product object.
        :returns: Product object from the database.
        """

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        """
        This method gets a list of all product objects from the database.

        :returns: List of all product objects from the database.
        """

    @abstractmethod
    def sub_product_quantity(self, product_name: str, quantity: int):
        """
        This method subtracts the quantity of a product in the database.

        :param product_name: Name of the product.
        :param quantity: Quantity amount to subtract.
        """

    @abstractmethod
    def product_exists(self, product_name: str) -> bool:
        """
        This method checks if a product exists in the database.

        :param product_name: Name of the product.
        :returns: Boolean on whether or not the product exists.
        """


class ProductDB(AbstractDB, AbstractAdminProductDB, AbstractUserProductDB):
    """
    This class represents a product database and implements AbstractDB,
    AbstractAdminProductDB, and AbstractUserProductDB. It contains a constructor,
    and the implemented abstract methods.
    """

    def __init__(self, db_name: str):
        """
        This constructor instantiates a product database object.

        :param db_name: Name of the database and its file path.
        """
        self.db_name = db_name
        self.check_db()

    def check_db(self):
        if not os.path.exists(self.db_name + ".csv"):
            self.create_db()

    def create_db(self):
        with open(self.db_name + ".csv", "w", newline="",  encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["product_name", "product_quantity", "product_price"])

    def add_product(self, product: Product):
        with open(self.db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([product.get_product_name(), product.get_product_quantity(),
                             product.get_product_price()])

    def remove_product(self, product: Product):
        temp_rows = []
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] != product.get_product_name():
                    temp_rows.append(row)
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def edit_product(self, product: Product, column: int, new_value: str):
        temp_rows = []
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product.get_product_name():
                    row[column] = new_value
                temp_rows.append(row)
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def get_product(self, product_name: str) -> Union[Product, bool]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == product_name:
                    return Product(row[0], int(row[1]), float(row[2]))
            return False

    def get_all_products(self) -> List[Product]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            products = []
            for row in reader:
                product = Product(row[0], int(row[1]), float(row[2]))
                products.append(product)
            return products

    def sub_product_quantity(self, product_name: str, quantity: int):
        temp_rows = []
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    new_quantity = int(row[1]) - quantity
                    row[1] = str(new_quantity)
                temp_rows.append(row)
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def product_exists(self, product_name: str) -> bool:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == product_name:
                    return True
            return False
