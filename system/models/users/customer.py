from system.models.users.user import User
from system.models.shopping.discount import DiscountCategory


class Customer(User):
    def __init__(self, user_name: str, password: str, country_id: int,
                 discount_category: DiscountCategory = None):
        User.__init__(self, user_name, password, 0, country_id)
        self._discount_category = discount_category

    def get_discount_category(self) -> DiscountCategory:
        return self._discount_category

    def set_discount_category(self, discount_category: DiscountCategory):
        self._discount_category = discount_category
