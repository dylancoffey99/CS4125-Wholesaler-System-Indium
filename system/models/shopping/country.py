"""
This module holds the country class.
"""
class Country:
    """
    This class discusses all the functions revolving around the countries like
    getting the country name, getting the country id, getting the vat of a
    country and getting the shipping cost.
    """
    def __init__(self, country_name: str, country_id: int, vat: float, shipping_cost: float):
        """
        Parameters
        ----------
        country_name : str
            The list of items in the basket
        country_id : int
            The subtotal of all the items in the basket
        vat : float
            This the percentage of vat to be paid on the basket subtotal
        shipping_cost : float
            This is the cost of shipping
        """
        self._country_name = country_name
        self._country_id = country_id
        self._vat = vat
        self._shipping_cost = shipping_cost

    def get_country_name(self) -> str:
        """
        This is where you get the name of the country

        :returns: the country name
        """
        return self._country_name

    def get_country_id(self) -> int:
        """
        This is where you get the id belonging to a specific country

        :returns: the country id
        """
        return self._country_id

    def get_vat(self) -> float:
        """
        This is where you get the vat

        :returns: the vat percentage
        """
        return self._vat

    def get_shipping_cost(self) -> float:
        """
        This is where you get the shipping cost

        :returns: the shipping cost
        """
        return self._shipping_cost
