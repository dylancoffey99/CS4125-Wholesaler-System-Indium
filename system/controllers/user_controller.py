import hashlib
from system.database.db_handler import UserDB
from system.controllers.abstract_controllers import AbstractUserController


class UserController(AbstractUserController):
    def __init__(self):
        self.user_db = UserDB("../database/userDB")

    def login_user(self, user_name: str, password: str):
        if user_name != "" and password != "" is not None:
            user = User(user_name, password)
            self.user_db.get_user(user)
            print("Login successful!")
        else:
            print("Error: please enter all the fields")

    def register_user(self, user_name: str, password: str, country_id: int):
        pass

    def hash_password(self, password: str) -> str:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password

uc = UserController()
#uc.register_user("Nadine", "pass", 1)
uc.login_user("Nadine", "pass")