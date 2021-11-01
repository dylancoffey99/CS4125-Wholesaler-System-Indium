# abstract_db_handler.py
# Defines the AbstractProductDB class and its abstract methods
# Author: Dylan Coffey - 18251382

from abc import ABC, abstractmethod
from typing import List
from stock_management import Product


class AbstractProductDB(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def remove_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product: Product, column: int, new_value: str):
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass
