# stock_management.py
# Defines the Product class implementing its methods
# for the stock management aspect of the system
# Author: Nikita Basovs - 18233244
# Edited: Dylan Coffey - 18251382

from typing import List
import observer as ob


# Implements the subject interface
class Product(ob.ISubject):
    def __init__(self, product_id: int, product_name: str,
                 product_quantity: int, product_price: float):
        self._product_id = product_id
        self._product_name = product_name
        self._product_quantity = product_quantity
        self._product_price = product_price
        self._observers = []

    def get_product_id(self) -> int:
        return self._product_id

    def get_product_name(self) -> str:
        return self._product_name

    def get_product_quantity(self) -> int:
        return self._product_quantity

    def get_product_price(self) -> float:
        return self._product_price

    def get_product_as_list(self) -> List[str]:
        return [str(self._product_id), self._product_name,
                str(self._product_quantity), str(self._product_price)]

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
