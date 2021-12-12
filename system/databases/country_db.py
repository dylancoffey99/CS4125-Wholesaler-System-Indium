import csv
from typing import List, Union
from abc import ABC, abstractmethod

from system.models.payment import Country


class AbstractCustomerCountryDB(ABC):
    @abstractmethod
    def get_country(self, country_id: int) -> Country:
        pass


class AbstractAccessCountryDB(ABC):
    @abstractmethod
    def get_all_countries_id_name(self) -> List:
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

    def get_all_countries_id_name(self) -> List:
        with open(self.db_name + ".csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            countries = []
            for row in reader:
                country_id_name = (int(row[0]), row[1])
                countries.append(country_id_name)
            return countries
