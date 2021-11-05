from system.models.authentication.register import Register


class User:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def get_user(self):
        return [self._user_id, self._user_name, self._password, self._is_admin]

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_password(self):
        return self._password

    def get_is_admin(self):
        return self._is_admin

    def set_user(self, user_name: str, password: str):
        self._user_name = user_name
        self._password = self.get_hashed_password(password)

    def hash_pass(self, password, user: Register):
        user.get_hashed_pasword(password)
