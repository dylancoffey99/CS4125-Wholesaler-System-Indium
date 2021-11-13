import os
import csv
from unittest import TestCase
from system.models.users.user import User
from system.models.shopping.product import Product
from system.database.db_handler import UserDB
from system.database.db_handler import ProductDB


class TestProductDB(TestCase):
    mock_db_name = "testProductDB"
    mock_db = ProductDB(mock_db_name)
    mock_product = Product("mock_product", 75, 100)

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["product_name", "product_quantity", "product_price"])
            writer.writerow(["product1", "25", "50"])
            writer.writerow(["product2", "50", "75"])
            writer.writerow([""])

    def tearDown(self):
        os.remove(self.mock_db_name)

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


class TestUserDB(TestCase):
    mock_db_name = "testUserDB"
    mock_db = UserDB(mock_db_name)
    mock_user = User("mock_user", "password", 0, 1)

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "is_admin", "country_id"])
            writer.writerow(["user1", "password1", "0", "1"])
            writer.writerow(["user2", "password2", "0", "2"])
            writer.writerow([""])

    def tearDown(self):
        os.remove(self.mock_db_name)

    def test_add_user(self):
        pass

    def test_get_user(self):
        pass

    def test_get_all_users(self):
        pass

    def test_user_exists(self):
        pass
