from system.models.shopping.discount import DiscountCategory
from system.models.users.user import User


class Customer(User):
    def __init__(self, user_name, password, country):
        User.__init__(self, user_name, password, False, country)

    def set_category(self, name: str, desc: str, discount_percentage: int) -> DiscountCategory:
        return DiscountCategory(name, desc, discount_percentage)

    def set_country(self, country: str) -> DiscountCategory:
        _country = country
        return DiscountCategory(_country)

    def set_discount_category(self, discount_id: int):
        if discount_id == 0:
            self.discount_category = DiscountCategory(discount_id, "Education", 10)
        elif discount_id == 1:
            self.discount_category = DiscountCategory(discount_id, "Business", 15)
        elif discount_id == 2:
            self.discount_category = DiscountCategory(discount_id, "Startup", 20)
