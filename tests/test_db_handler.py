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
    mock_db_product1 = Product("product1", 25, 50)
    mock_db_product2 = Product("product2", 50, 75)

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["product_name", "product_quantity", "product_price"])
            writer.writerow([self.mock_db_product1.get_product_name(),
                             self.mock_db_product1.get_product_quantity(),
                             self.mock_db_product1.get_product_price()])
            writer.writerow([self.mock_db_product2.get_product_name(),
                             self.mock_db_product2.get_product_quantity(),
                             self.mock_db_product2.get_product_price()])
            writer.writerow([""])

    def tearDown(self):
        os.remove(self.mock_db_name)

    def test_add_product(self):
        new_product = Product("new_product", 75, 100)
        self.assertEqual(self.mock_db.add_product(new_product), True)

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
    mock_db_user1 = User("user1", "password1", 0, 1)
    mock_db_user2 = User("user2", "password2", 0, 2)

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "is_admin", "country_id"])
            writer.writerow([self.mock_db_user1.get_user_name(),
                             self.mock_db_user1.get_password(),
                             self.mock_db_user1.get_is_admin(),
                             self.mock_db_user1.get_country_id()])
            writer.writerow([self.mock_db_user2.get_user_name(),
                             self.mock_db_user2.get_password(),
                             self.mock_db_user2.get_is_admin(),
                             self.mock_db_user2.get_country_id()])
            writer.writerow([""])

    def tearDown(self):
        os.remove(self.mock_db_name)

    def test_add_user(self):
        new_user = User("new_user", "password", 0, 1)
        self.assertEqual(self.mock_db.add_user(new_user), True)

    def test_get_user(self):
        pass

    def test_get_all_users(self):
        pass

    def test_user_exists(self):
        pass
