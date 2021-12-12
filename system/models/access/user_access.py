import hashlib

from system.databases.user_db import AbstractAccessUserDB, UserDB
from system.models.users.customer import Customer
from system.models.users.user import User


class UserAccess(AbstractAccessUserDB):
    def __init__(self):
        self.user_db = UserDB("system/databases/csv/user_db")

    def add_customer(self, customer: Customer):
        self.user_db.add_customer(customer)

    def get_user(self, user_name) -> User:
        return self.user_db.get_user(user_name)

    def user_exists(self, user_name) -> bool:
        return self.user_db.user_exists(user_name)

    def verify_password(self, password: str) -> bool:
        return bool(password == self.hash_password(password))

    def is_admin(self, user_name) -> bool:
        user = self.get_user(user_name)
        return bool(user.get_is_admin() == 1)

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
