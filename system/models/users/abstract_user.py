"""
This module contains the AbstractUser class.
"""
from abc import ABC, abstractmethod


class AbstractUser(ABC):
    """
    This abstract user class represents an interface for the user. It contains the
    abstract methods to be implemented into the user access and user database classes.
    """

    @abstractmethod
    def get_user_name(self) -> str:
        """
        This method gets a users username.

        :returns: Username of the user.
        """
        pass

    @abstractmethod
    def get_password(self) -> str:
        """
        This method gets a users password.

        :returns: Password of the user.
        """
        pass

    @abstractmethod
    def get_is_admin(self) -> int:
        """
        This method gets whether a user is admin or customer.

        :returns: Identity of the User.
        """
        pass

    @abstractmethod
    def get_country_id(self) -> int:
        """
        This method gets a users country.

        :returns: Country of the user.
        """
        pass
