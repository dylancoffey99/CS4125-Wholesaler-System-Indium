from typing import List
from system.models.authentication.register import Register


class User:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def get_user_id(self) -> int:
        return self._user_id

    def get_user_name(self) -> str:
        return self._user_name

    def get_password(self) -> str:
        return self._password

    def get_is_admin(self) -> bool:
        return self._is_admin

    def get_user_as_list(self) -> List[str]:
        return [str(self._user_id), self._user_name, self._password, str(self._is_admin)]

    def set_user(self, user_name: str, password: str, reg: Register):
        self._user_name = user_name
        self._password = self.get_hashed_password(password)
