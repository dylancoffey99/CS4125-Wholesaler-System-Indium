from typing import List
from abc import ABC, abstractmethod
from system.models.users.user import User
from system.models.shopping.order import Order
from system.models.shopping.product import Product
from system.models.shopping.country import Country


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
    def get_product(self, product_name: str):
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def product_exists(self, product_name: str) -> bool:
        pass


class AbstractUserDB(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, user_name: str):
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def user_exists(self, user_name: str) -> bool:
        pass


class AbstractOrderDB(ABC):
    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def update_order_subtotals(self, customer_name: str, discount_percentage: float):
        pass

    @abstractmethod
    def get_customer_orders(self, customer_name: str) -> List:
        pass


class AbstractCountryDB(ABC):
    @abstractmethod
    def get_country(self, country_name: str):
        pass

    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass
