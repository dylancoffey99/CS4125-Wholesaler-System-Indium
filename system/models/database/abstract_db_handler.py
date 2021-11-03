from abc import ABC, abstractmethod
from typing import List
from system.models.shopping.stock_management import Product


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
    def edit_product_quantity(self, product: Product, operation: bool, value: int):
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass
