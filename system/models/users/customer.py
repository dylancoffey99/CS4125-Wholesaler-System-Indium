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

    def set_discount_category(self, name: str, desc: str) -> DiscountCategory:
        if name == "Education":
            discount_percentage = 10
        elif name == "Business":
            discount_percentage = 15
        elif name == "Startup":
            discount_percentage = 20
        return DiscountCategory(name, desc, discount_percentage)


customer = Customer("user", "12345", "ireland")
print(customer)
print(customer.get_user_as_list())