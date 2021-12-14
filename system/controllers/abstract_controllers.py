"""
This module contains the abstract classes AbstractUserController and
AbstractObserverController. The module imports ABC (Abstract Base Class)
and abstractmethod from the abc module.
"""
from abc import ABC, abstractmethod


class AbstractUserController(ABC):
    """
    This abstract class represents an interface user controller, containing the abstract
    methods to be implemented in user controller classes.
    """

    @abstractmethod
    def logout_user(self):
        """This method logs out the user and changes the view."""


class AbstractObserverController(ABC):
    """
    This abstract class represents an interface observer controller, containing the
    abstract methods to be implemented in observer controller classes.
    """

    @abstractmethod
    def attach_observers(self):
        """This method attaches observer methods to a subjects observers list."""
