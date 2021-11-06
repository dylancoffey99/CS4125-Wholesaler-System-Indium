from abc import ABC, abstractmethod
from typing import List
from system.models.users.user import User
from system.models.shopping.product import Product


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
    def sub_product_quantity(self, product: Product, amount: int):
        pass

    @abstractmethod
    def get_product(self, product_name: str) -> Product:
        pass

    @abstractmethod
    def get_product_id(self, product: Product) -> int:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def increment_product_id(self) -> int:
        pass


class AbstractUserDB(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, user_name: str) -> User:
        pass

    @abstractmethod
    def get_user_id(self, user: User) -> int:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def increment_user_id(self) -> int:
        pass
