from system.models.users.user import User
from system.models.shopping.discount import DiscountCategory


class Customer(User):
    def __init__(self, user_name: str, password: str, country_id: int):
        User.__init__(self, user_name, password, False, country_id)
        self.discount_category = None

    def get_discount_category(self) -> DiscountCategory:
        return self.discount_category

    def set_discount_category(self, discount_id: int):
        if discount_id == 0:
            self.discount_category = DiscountCategory(discount_id, "Education", 10)
        elif discount_id == 1:
            self.discount_category = DiscountCategory(discount_id, "Business", 15)
        elif discount_id == 2:
            self.discount_category = DiscountCategory(discount_id, "Startup", 20)
