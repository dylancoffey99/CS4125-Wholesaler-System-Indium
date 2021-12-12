from system.databases.product_db import AbstractAdminProductDB
from system.models.shopping.product import Product
from system.models.users.abstract_user import AbstractUser
from system.models.users.user import User


class Admin(User, AbstractUser, AbstractAdminProductDB):
    def __init__(self, user_name: str, password: str):
        User.__init__(self, user_name, password, 1, -1)

    def add_product(self, product: Product):
        self.product_db.add_product(product)

    def remove_product(self, product: Product):
        self.product_db.remove_product(product)

    def edit_product(self, product: Product, column: int, new_value: str):
        self.product_db.edit_product(product, column, new_value)
