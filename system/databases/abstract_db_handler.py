from typing import List
from abc import ABC, abstractmethod

from system.models.shopping import Country, Order


class AbstractOrderDB(ABC):
    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def update_order_subtotals(self, user_name: str, discount_percentage: float):
        pass

    @abstractmethod
    def get_customer_orders(self, user_name: str) -> List:
        pass

    @abstractmethod
    def orders_exist(self, user_name: str) -> bool:
        pass


class AbstractCountryDB(ABC):
    @abstractmethod
    def get_country(self, country_id: int):
        pass

    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass
