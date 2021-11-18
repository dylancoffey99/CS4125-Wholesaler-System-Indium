"""This module contains the Country class."""


class Country:
    """
    This class represents a model of a country, containing a constructor, and
    the getter methods for its parameters.
    """
    def __init__(self, country_name: str, country_id: int, vat_percentage: float,
                 shipping_cost: float):
        """
        This constructor instantiates a country object.

        :param country_name: Name of the country.
        :param country_id: ID of the country.
        :param vat_percentage: VAT percentage of the country.
        :param shipping_cost: Shipping cost of the country.
        """
        self.country_name = country_name
        self.country_id = country_id
        self.vat_percentage = vat_percentage
        self.shipping_cost = shipping_cost

    def get_country_name(self) -> str:
        """
        This method gets the country name.

        :returns: Name of the country.
        """
        return self.country_name

    def get_country_id(self) -> int:
        """
        This method gets the country ID.

        :returns: ID of the country.
        """
        return self.country_id

    def get_vat_percentage(self) -> float:
        """
        This method gets the country VAT percentage.

        :returns: VAT percentage of the country.
        """
        return self.vat_percentage

    def get_shipping_cost(self) -> float:
        """
        This method gets the country shipping cost.

        :returns: Shipping cost of the country.
        """
        return self.shipping_cost
