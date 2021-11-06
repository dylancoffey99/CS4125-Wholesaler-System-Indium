from typing import List
from system.models.shopping.observer import ISubject


class Product(ISubject):
    def __init__(self, product_name: str, product_quantity: int, product_price: float):
        self._product_name = product_name
        self._product_quantity = product_quantity
        self._product_price = product_price
        self._observers = []

    def get_product_name(self) -> str:
        return self._product_name

    def get_product_quantity(self) -> int:
        return self._product_quantity

    def get_product_price(self) -> float:
        return self._product_price

    def set_product_quantity(self, new_product_quantity: int):
        self._product_quantity = new_product_quantity
        self.notify()  # Notify observers when quantity changes, for low stock warnings etc

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
