from system.databases import AbstractCustomerCountryDB, AbstractCustomerOrderDB, CountryDB, OrderDB
from system.models.payment import Country, DiscountCategory, Order
from system.models.users import AbstractUser
from system.models.users.user import User


class Customer(User, AbstractUser, AbstractCustomerCountryDB, AbstractCustomerOrderDB):
    def __init__(self, user_name: str, password: str, country_id: int, discount_id: int = -1):
        User.__init__(self, user_name, password, 0, country_id)
        self.discount_id = discount_id
        self.country_db = CountryDB("system/databases/csv/country_db")
        self.order_db = OrderDB("system/databases/csv/order_db")

    def get_discount_id(self) -> int:
        return self.discount_id

    def set_discount_id(self, discount_id: int):
        self.discount_id = discount_id

    def check_discount_category(self) -> DiscountCategory:
        if self.discount_id == "0":
            discount = DiscountCategory(0, "Education", 0.10)
        elif self.discount_id == "1":
            discount = DiscountCategory(1, "Small Business", 0.15)
        else:
            discount = DiscountCategory(2, "Start-up Business", 0.20)
        return discount

    def get_country(self, country_id: int) -> Country:
        return self.country_db.get_country(country_id)

    def add_order(self, order: Order):
        self.order_db.add_order(order)
