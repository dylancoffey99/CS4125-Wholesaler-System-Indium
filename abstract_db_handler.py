# abstract_db_handler.py
# Defines AbstractDBHandler methods
# Author: Dylan Coffey - 18251382

from abc import ABC, abstractmethod


class AbstractDBHandler(ABC):
    @abstractmethod
    def open_db(self, operation):
        pass

    @abstractmethod
    def read_db(self, operation):
        pass

    @abstractmethod
    def write_db(self, operation):
        pass

    @abstractmethod
    def add_row(self, row):
        pass

    @abstractmethod
    def remove_row(self, _id):
        pass

    @abstractmethod
    def get_row(self, _id):
        pass

    @abstractmethod
    def get_id(self, name):
        pass

    @abstractmethod
    def edit_row(self, _id, column, new_value):
        pass
