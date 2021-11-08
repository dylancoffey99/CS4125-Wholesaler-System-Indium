import hashlib
from system.controllers.abstract_controllers import AbstractUserController


class UserController(AbstractUserController):
    def login_user(self, user_name: str, password: str):
        pass

    def register_user(self, user_name: str, password: str, country_id: int):
        pass

    def hash_password(self, password: str) -> str:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password
