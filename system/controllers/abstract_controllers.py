from abc import ABC, abstractmethod


class AbstractAccessController(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login_user(self, user_name: str, password: str):
        pass

    @abstractmethod
    def register_user(self, user_name: str, password: str, country_id: int):
        pass

    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass
