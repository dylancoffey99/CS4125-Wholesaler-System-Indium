from system.models.users.user import User
from system.models.shopping.product import Product
from system.models.database.db_handler import ProductDB


class Admin:
    def __init__(self, _user: User):
        self._user_id = _user.get_user_id()
        self._user_name = _user.get_user_name()
        self._is_admin = _user.get_is_admin()
        self._db = ProductDB("productDB")

    def add_product(self, product: Product):
        self._db.add_product(product)

    def remove_product(self, product: Product):
        self._db.remove_product(product)

    def get_orders(self):  # return list
        pass  # print the products order
