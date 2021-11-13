from system.models.users.user import User
from system.models.shopping.product import Product
from system.database.db_handler import UserDB
from system.database.db_handler import ProductDB


class TestProductDB:
    mock_db = ProductDB("testProductDB")
    mock_product = Product("product", 100, 9.99)

    def test_add_product(self):
        pass

    def test_remove_product(self):
        pass

    def test_edit_product(self):
        pass

    def sub_product_quantity(self):
        pass

    def test_get_product(self):
        pass

    def test_get_all_products(self):
        pass

    def test_product_exists(self):
        pass


class TestUserDB:
    mock_db = UserDB("testUserDB")
    mock_user = User("username", "password", 0, 1)

    def test_add_user(self):
        pass

    def test_get_user(self):
        pass

    def test_get_all_users(self):
        pass

    def test_user_exists(self):
        pass
