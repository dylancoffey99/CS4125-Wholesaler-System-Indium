from typing import List
from system.models.users.user import User
from system.models.shopping.product import Product
from system.database.db_handler import ProductDB


class Admin(User):
    def __init__(self, user_name: str, password: str, product_db: ProductDB = None):
        User.__init__(self, user_name, password, 1, -1)
        self._product_db = product_db

    def get_orders(self) -> List:
        pass  # needs to be implemented when order is finished

    def add_product(self, product: Product):
        self._product_db.add_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        self._product_db.edit_product(product, column, new_value)

    def remove_product(self, product: Product):
        self._product_db.remove_product(product)
