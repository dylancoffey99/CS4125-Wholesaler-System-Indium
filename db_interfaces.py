# db_interfaces.py
# Defines database/productDB interfaces
# Author: Dylan Coffey - 18251382

from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def open_db(self, db_name, operation):
        pass

    @abstractmethod
    def read_db(self, db_name):
        pass

    @abstractmethod
    def write_db(self, db_name):
        pass


class IProductDB(ABC):
    @abstractmethod
    def add_product(self, product_id, product_name, product_quantity, product_price):
        pass

    @abstractmethod
    def remove_product(self, product_id):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass

    @abstractmethod
    def get_product_id(self, product_name):
        pass

    @abstractmethod
    def edit_product_name(self, product_id, product_name):
        pass

    @abstractmethod
    def edit_product_quantity(self, product_id, product_quantity):
        pass

    @abstractmethod
    def edit_product_price(self, product_id, product_price):
        pass
