from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def get_user_name(self) -> str:
        pass

    @abstractmethod
    def get_password(self) -> str:
        pass

    @abstractmethod
    def get_is_admin(self) -> int:
        pass

    @abstractmethod
    def get_country_id(self) -> int:
        pass


class Customer(User):
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


class Admin(User):
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


class UserFactory:
    def create_user(self, is_admin):
        if is_admin == '1':
            return Circle(float(radius))

        elif is_admin == '0':
            user_name = input("Enter username: ")
            password = input("Enter password: ")
            country_id = input("Enter country:")
            return Customer(str(user_name), str(password), int(country_id))
