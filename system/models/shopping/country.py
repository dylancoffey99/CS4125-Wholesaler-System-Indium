class Country:
    def __init__(self, country_name: str, country_id: int, vat: float, shipping_cost: float):
        self._country_name = country_name
        self._country_id = country_id
        self._vat = vat
        self._shipping_cost = shipping_cost

    def get_country_name(self) -> str:
        return self._country_name

    def get_country_id(self) -> int:
        return self._country_id

    def get_vat(self) -> float:
        return self._vat

    def get_shipping_cost(self) -> float:
        return self._shipping_cost
