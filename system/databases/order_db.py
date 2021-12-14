"""
This module contains the OrderDB, AbstractAdminOrderDB and AbstractCustomerOrderDB
classes. The module imports the modules csv and os, the type List from the typing
module, the class Order from the systems payment package, and the class AbstractDB
from the systems databases package.
"""
import csv
import os
from abc import ABC, abstractmethod
from typing import List

from system.databases.abstract_db import AbstractDB
from system.models.payment import Order


class AbstractAdminOrderDB(ABC):
    """
    This abstract class represents an interface for the admin and order database.
    It contains the abstract methods to be implemented into the admin and order
    database classes.
    """

    @abstractmethod
    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        """
        This method updates the order subtotals of a customer by discounting them
        using a discount percentage.

        :param user_name: Username of the customer.
        :param discount_percentage: Discount percentage to be used.
        """

    @abstractmethod
    def get_customer_orders(self, user_name: str) -> List:
        """
        This method gets a list of a customers orders from the database.

        :param user_name: Username of the customer.
        :returns: List of the customers orders from the database.
        """

    @abstractmethod
    def orders_exist(self, user_name: str) -> bool:
        """
        This method checks if a customers orders exist in the database.

        :param user_name: Username of the customer.
        :returns: Boolean on whether or not a customers orders exist.
        """


class AbstractCustomerOrderDB(ABC):
    """
    This abstract class represents an interface for the customer and order database.
    It contains the abstract methods to be implemented into the customer and order
    database classes.
    """

    @abstractmethod
    def add_order(self, order: Order):
        """
        This method adds an order to the database.

        :param order: Order object to be added to the database..
        """


class OrderDB(AbstractDB, AbstractAdminOrderDB, AbstractCustomerOrderDB):
    """
    This class represents a order database and implements AbstractDB,
    AbstractAdminOrderDB, and AbstractCustomerOrderDB. It contains a constructor,
    and the implemented abstract methods.
    """

    def __init__(self, db_name: str):
        """
        This constructor instantiates an order database object.

        :param db_name: Name of the database and its file path.
        """
        self.db_name = db_name
        self.order_separator = "================"
        self.check_db()

    def check_db(self):
        if not os.path.exists(self.db_name + ".csv"):
            self.create_db()

    def create_db(self):
        with open(self.db_name + ".csv", "w", newline="",  encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["customer_name", "product_name", "order_date",
                             "subtotal"])

    def add_order(self, order: Order):
        with open(self.db_name + ".csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            product_names = order.get_product_names()
            first_line = True
            for product, _ in enumerate(product_names):
                if first_line:
                    first_line = False
                    writer.writerow([order.get_customer_name(), self.order_separator,
                                     self.order_separator, self.order_separator])
                    writer.writerow([order.get_customer_name(), product_names[product],
                                     order.get_order_date().strftime("%d-%m-%Y %H:%M:%S"),
                                     order.get_order_subtotal()])
                else:
                    writer.writerow([order.get_customer_name(), product_names[product], "", ""])

    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        temp_rows = []
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    if row[1] == self.order_separator or row[2] == "":
                        temp_rows.append(row)
                        continue
                    subtotal = float(row[3])
                    discount = subtotal * discount_percentage
                    row[3] = str(subtotal - discount)
                temp_rows.append(row)
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(temp_rows)

    def get_customer_orders(self, user_name: str) -> List:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            orders = []
            for row in reader:
                order = []
                if row[0] == user_name:
                    order.append(row[0])
                    order.append(row[1])
                    order.append(row[2])
                    order.append(row[3])
                    orders.append(order)
            return orders

    def orders_exist(self, user_name: str) -> bool:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == user_name:
                    return True
            return False
