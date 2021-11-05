from system.models.database.db_handler import UserDB
from typing import List

class Register:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def check_username(self, user_name, user: UserDB):
        if user_name == user.get_user(user_name):
            print("Change username")
        else:
            print("Username available")
            user.add_user(user_name)


