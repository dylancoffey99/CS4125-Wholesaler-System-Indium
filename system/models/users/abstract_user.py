"""
This module contains the abstract class AbstractUser. The module imports
ABC (Abstract Base Class) and abstractmethod from the abc module.
"""
from abc import ABC, abstractmethod


class AbstractUser(ABC):
    """
    This abstract user class represents an interface user. It contains the
    abstract methods to be implemented in user classes.
    """

    @abstractmethod
    def get_user_name(self) -> str:
        """
        This method gets the username.

        :returns: Username of the user.
        """

    @abstractmethod
    def get_password(self) -> str:
        """
        This method gets the password.

        :returns: Password of the user.
        """

    @abstractmethod
    def get_is_admin(self) -> int:
        """
        This method gets the admin flag.

        :returns: Admin flag of the user.
        """

    @abstractmethod
    def get_country_id(self) -> int:
        """
        This method gets the country ID.

        :returns: Country ID of the user.
        """

    @abstractmethod
    def get_discount_id(self) -> int:
        """
        This method gets the discount ID.

        :returns: Discount ID of the user.
        """
