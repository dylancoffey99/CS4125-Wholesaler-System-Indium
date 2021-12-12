from abc import ABC, abstractmethod


class AbstractUser(ABC):
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
