import csv
from abc import ABC, abstractmethod
from typing import List

from system.models.payment import Order


class AbstractAdminOrderDB(ABC):
    @abstractmethod
    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        pass

    @abstractmethod
    def get_customer_orders(self, user_name: str) -> List:
        pass

    @abstractmethod
    def orders_exist(self, user_name: str) -> bool:
        pass


class AbstractCustomerOrderDB(ABC):
    @abstractmethod
    def add_order(self, order: Order):
        pass


class OrderDB(AbstractAdminOrderDB, AbstractCustomerOrderDB):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.order_separator = "================"

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
