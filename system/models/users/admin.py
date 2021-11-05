from system.models.users.user import User
from system.models.shopping.product import Product
from system.models.database.db_handler import ProductDB


class Admin(User):
    def __init__(self, user_name: str, password: str, is_admin: bool, country: str):
        User.__init__(self, user_name, password, is_admin, country)
        self._db = ProductDB("productDB")

    def add_product(self, product: Product):
        self._db.add_product(product)

    def remove_product(self, product: Product):
        self._db.remove_product(product)
