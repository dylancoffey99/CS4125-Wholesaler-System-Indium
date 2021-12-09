from system.models.users.user import User


class Customer(User):
    def __init__(self, user_name: str, password: str, country_id: int,
                 discount_id: int = -1):
        User.__init__(self, user_name, password, 0, country_id)
        self.discount_id = discount_id

    def get_discount_id(self):
        return self.discount_id

    def set_discount_id(self, discount_id: int):
        self.discount_id = discount_id
