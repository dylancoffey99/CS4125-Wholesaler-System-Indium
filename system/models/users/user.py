"""
This module contains the User class. The module imports the the AbstractUser
class from the systems users package.
"""

from system.models.users import AbstractUser


class User(AbstractUser):
    """
    This class represents a model of a user and implements AbstractUser.
    It also contains a constructor and the implemented abstract methods.
    """

    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int,
                 discount_id: int = -1):
        """
        This constructor instantiates a user object.

        :param user_name: Username of the user.
        :param password: Password of the user.
        :param is_admin: Admin flag of the user.
        :param country_id: Country ID of the user.
        :param discount_id: Discount ID of the user (optional).
        """
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        self.country_id = country_id
        self.discount_id = discount_id

    def get_user_name(self) -> str:
        return self.user_name

    def get_password(self) -> str:
        return self.password

    def get_is_admin(self) -> int:
        return self.is_admin

    def get_country_id(self) -> int:
        return self.country_id

    def get_discount_id(self) -> int:
        return self.discount_id
