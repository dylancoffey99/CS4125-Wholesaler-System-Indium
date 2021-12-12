from system.models.shopping import DiscountCategory
from system.models.users.abstract_user import AbstractUser
from system.models.users.user import User


class Customer(User, AbstractUser):
    def __init__(self, user_name: str, password: str, country_id: int,
                 discount_id: int = -1):
        User.__init__(self, user_name, password, 0, country_id)
        self.discount_id = discount_id

    def get_discount_id(self):
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
