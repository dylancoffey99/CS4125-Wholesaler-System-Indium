"""
This module contains the abstract class AbstractDB. The module imports
ABC (Abstract Base Class) and abstractmethod from the abc module.
"""
from abc import ABC, abstractmethod


class AbstractDB(ABC):
    """
    This abstract class represents an interface database, containing the abstract
    methods to be implemented in database classes.
    """

    @abstractmethod
    def check_db(self):
        """This method checks if the file path of the database exists."""

    @abstractmethod
    def create_db(self):
        """This method creates a database CSV file if it doesn't exist."""
