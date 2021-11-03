import hashlib
import os

class Register:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool, error: str):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def ask_user_credentials(self):
        print("Please Provide")
        user_name = str(input("Name: "))
        password = str(input("Password: "))
        return user_name, password