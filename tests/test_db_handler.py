import csv
import os
from unittest import TestCase

from system.databases import UserDB, ProductDB
from system.models.shopping import Product
from system.models.users import User


class TestProductDB(TestCase):
    mock_db_name = "test_product_db"
    mock_db = ProductDB(mock_db_name)
    mock_product = Product("product", 25, 50)
    mock_product_name = mock_product.get_product_name()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["product_name", "product_quantity", "product_price"])
            writer.writerow([self.mock_product.get_product_name(),
                             self.mock_product.get_product_quantity(),
                             self.mock_product.get_product_price()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_add_product(self):
        new_product = Product("new_product", 75, 100)
        self.mock_db.add_product(new_product)
        self.assertEqual(self.mock_db.product_exists(new_product.get_product_name()), True)

    def test_remove_product(self):
        self.mock_db.remove_product(self.mock_product)
        self.assertEqual(self.mock_db.product_exists(self.mock_product_name), False)

    def test_edit_product(self):
        edited_product_name = "edited_product"
        self.mock_db.edit_product(self.mock_product, 0, edited_product_name)
        self.assertEqual(self.mock_db.get_product(edited_product_name).get_product_name(),
                         edited_product_name)

    def test_sub_product_quantity(self):
        self.mock_db.sub_product_quantity(self.mock_product, 25)
        self.assertEqual(self.mock_db.get_product(self.mock_product_name).get_product_quantity(), 0)

    def test_get_product(self):
        self.assertEqual(self.mock_db.get_product(self.mock_product_name).get_product_name(),
                         self.mock_product_name)

    def test_get_all_products(self):
        self.assertEqual(self.mock_db.get_all_products()[0].get_product_name(),
                         self.mock_product_name)

    def test_product_exists(self):
        self.assertEqual(self.mock_db.product_exists(self.mock_product_name), True)


class TestUserDB(TestCase):
    mock_db_name = "test_user_db"
    mock_db = UserDB(mock_db_name)
    mock_user = User("username", "password", 0, 1)
    mock_user_name = mock_user.get_user_name()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "is_admin", "country_id"])
            writer.writerow([self.mock_user.get_user_name(),
                             self.mock_user.get_password(),
                             self.mock_user.get_is_admin(),
                             self.mock_user.get_country_id()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_add_user(self):
        new_user = User("new_user", "password", 0, 1)
        self.mock_db.add_user(new_user)
        self.assertEqual(self.mock_db.user_exists(new_user.get_user_name()), True)

    def test_get_user(self):
        self.assertEqual(self.mock_db.get_user(self.mock_user_name).get_user_name(),
                         self.mock_user_name)

    def test_get_all_users(self):
        self.assertEqual(self.mock_db.get_all_users()[0].get_user_name(), self.mock_user_name)

    def test_user_exists(self):
        self.assertEqual(self.mock_db.user_exists(self.mock_user_name), True)
