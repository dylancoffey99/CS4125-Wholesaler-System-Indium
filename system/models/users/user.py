from typing import List, Union

from system.databases.product_db import AbstractUserProductDB, AbstractProductDB, ProductDB
from system.models.shopping import Product
from system.models.users.abstract_user import AbstractUser


class User(AbstractUser, AbstractUserProductDB, AbstractProductDB):
    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        self.country_id = country_id
        self.product_db = ProductDB("system/databases/csv/product_db")

    def get_user_name(self) -> str:
        return self.user_name

    def get_password(self) -> str:
        return self.password

    def get_is_admin(self) -> int:
        return self.is_admin

    def get_country_id(self) -> int:
        return self.country_id

    def get_product(self, product_name: str) -> Union[Product, bool]:
        return self.product_db.get_product(product_name)

    def get_all_products(self) -> List[Product]:
        return self.product_db.get_all_products()

    def sub_product_quantity(self, product_name: str, quantity: int):
        self.product_db.sub_product_quantity(product_name, quantity)

    def product_exists(self, product_name: str) -> bool:
        return self.product_db.product_exists(product_name)
