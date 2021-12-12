from system.models.users.abstract_user import AbstractUser


class User(AbstractUser):
    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        self.country_id = country_id

    def get_user_name(self) -> str:
        return self.user_name

    def get_password(self) -> str:
        return self.password

    def get_is_admin(self) -> int:
        return self.is_admin

    def get_country_id(self) -> int:
        return self.country_id
