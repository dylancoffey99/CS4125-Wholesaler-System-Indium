from typing import List
import hashlib
import os


class User:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin
        self._country = country

    def get_user_name(self) -> str:
        return self._user_name

    def get_password(self) -> str:
        return self._password

    def get_is_admin(self) -> bool:
        return self._is_admin

    def get_country_id(self) -> int:
        return self._country_id
