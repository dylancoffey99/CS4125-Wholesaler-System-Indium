"""
This module contains the CountryDB, AbstractCustomerCountryDB and AbstractAccessCountryDB
classes. The module imports the module csv, the ABC (Abstract Base Class) and abstractmethod
from the abc module, the type List and Union from the typing module, and the class Country
from the systems payment package.
"""
import csv
from abc import ABC, abstractmethod
from typing import List, Union

from system.models.payment import Country


class AbstractCustomerCountryDB(ABC):
    """
    This abstract class represents an interface for the customer and country database.
    It contains the abstract methods to be implemented into the customer and country
    database classes.
    """

    @abstractmethod
    def get_country(self, country_id: int) -> Country:
        """
        This method gets an object of country from the database.

        :param country_id: Country ID of the country object.
        :returns: Country object from the database.
        """


class AbstractAccessCountryDB(ABC):
    """
    This abstract class represents an interface for the user access and country
    database. It contains the abstract methods to be implemented into the user
    access and country database classes.
    """

    @abstractmethod
    def get_country_names(self) -> List[str]:
        """
        This method gets a list of country names from the database.

        :returns: List of country names from the database.
        """

    @abstractmethod
    def get_country_dict(self) -> dict:
        """
        This method gets a dictionary of country names and IDs from the database.

        :returns: Dictionary of country names and IDs from the database.
        """


class CountryDB(AbstractAccessCountryDB, AbstractCustomerCountryDB):
    """
    This class represents a country database and implements AbstractAccessCountryDB
    and AbstractCustomerCountryDB. It contains a constructor, and the implemented
    abstract methods.
    """

    def __init__(self, db_name: str):
        """
        This constructor instantiates a country database object.

        :param db_name: Name of the database and its file path.
        """
        self.db_name = db_name

    def get_country(self, country_id: int) -> Union[Country, bool]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == str(country_id):
                    return Country(int(row[0]), row[1], float(row[2]), float(row[3]))
            return False

    def get_country_names(self) -> List[str]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            country_names = []
            for row in reader:
                country_names.append(row[1])
            return country_names

    def get_country_dict(self) -> dict:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            country_dict = {}
            for row in reader:
                country_dict[row[1]] = (int(row[0]))
            return country_dict
