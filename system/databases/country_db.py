"""
This module contains the CountryDB, AbstractCustomerCountryDB and AbstractAccessCountryDB
classes. The module imports the modules csv and os, the type List and Union from the typing
module, the class Country from the systems payment package, and the class AbstractDB from
the systems databases package.
"""
import csv
import os
from abc import ABC, abstractmethod
from typing import List, Union

from system.databases.abstract_db import AbstractDB
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
    def get_country_names(self) -> List:
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


class CountryDB(AbstractDB, AbstractAccessCountryDB, AbstractCustomerCountryDB):
    """
    This class represents a country database and implements AbstractDB,
    AbstractAccessCountryDB, and AbstractCustomerCountryDB. It contains a
    constructor, and the implemented abstract methods.
    """

    def __init__(self, db_name: str):
        """
        This constructor instantiates a country database object.

        :param db_name: Name of the database and its file path.
        """
        self.db_name = db_name
        self.check_db()

    def check_db(self):
        if not os.path.exists(self.db_name + ".csv"):
            self.create_db()

    def create_db(self):
        with open(self.db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["country_id", "country_name", "vat_percentage",
                             "shipping_cost"])

    def get_country(self, country_id: int) -> Union[Country, bool]:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                if row[0] == str(country_id):
                    return Country(int(row[0]), row[1], float(row[2]), float(row[3]))
            return False

    def get_country_names(self) -> List:
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
