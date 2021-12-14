import csv
from abc import ABC, abstractmethod
from typing import List, Union

from system.models.payment import Country


class AbstractCustomerCountryDB(ABC):
    @abstractmethod
    def get_country(self, country_id: int) -> Country:
        pass


class AbstractAccessCountryDB(ABC):
    @abstractmethod
    def get_country_names(self) -> List:
        pass

    @abstractmethod
    def get_country_dict(self) -> dict:
        pass


class CountryDB(AbstractAccessCountryDB, AbstractCustomerCountryDB):
    def __init__(self, db_name: str):
        self.db_name = db_name

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
