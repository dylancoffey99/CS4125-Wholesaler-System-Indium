class User:
    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin
        self._country_id = country_id
        self._logged_in = False

    def get_user_name(self) -> str:
        return self._user_name

    def get_password(self) -> str:
        return self._password

    def get_is_admin(self) -> int:
        return self._is_admin

    def get_country_id(self) -> int:
        return self._country_id

    def get_status(self) -> bool:
        return self._logged_in

    def set_status(self, status: bool):
        self._logged_in = status
