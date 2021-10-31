# abstract_db_handler.py
# Defines AbstractProductDB and AbstractUserDB
# classes and their abstract methods
# Author: Dylan Coffey - 18251382

from abc import ABC, abstractmethod


class AbstractProductDB(ABC):
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def remove_product(self, product_id):
        pass

    @abstractmethod
    def edit_product(self, product_id, column, new_value):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass

    @abstractmethod
    def get_product_id(self, product_name):
        pass

    @abstractmethod
    def get_all_products(self):
        pass


class AbstractUserDB(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def remove_user(self, user_id):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def get_user_id(self, user_name):
        pass

    @abstractmethod
    def get_all_users(self):
        pass
