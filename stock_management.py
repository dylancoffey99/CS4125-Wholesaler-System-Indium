# stock_management.py
# various classes for the stock management aspect of the system
# Author: Nikita Basovs - 18233244
from abc import ABC

import observer as ob


# implements the subject interface
class Product(ob.ISubject):
    def __init__(self, product_id, name, quantity):
        self._product_id = product_id
        self._name = name
        self._quantity = quantity
        self._observers = []

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, new_quantity):
        self._quantity = new_quantity
        # notify observers when quantity changes, for low stock warnings etc
        self.notify()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
