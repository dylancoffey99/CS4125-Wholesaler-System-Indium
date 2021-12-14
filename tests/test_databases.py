"""
This module contains the unit testing for the database classes. The module imports
the modules csv and os, the class datetime from the datetime module, the type List
from the typing module, and the class TestCase from the unittest module. The module
also imports all the database classes and their respective model classes.
"""
import csv
import os
from datetime import datetime
from typing import List
from unittest import TestCase

from system.databases import ProductDB, OrderDB, CountryDB
from system.databases.user_db import UserDB
from system.models.payment import Order, Country
from system.models.shopping import Product
from system.models.users.customer import Customer
from system.models.users.user import User


class TestProductDB(TestCase):
    """
    This class represents a test case for ProductDB and implements TestCase.
    It contains the implemented abstract methods for setting up/tearing down
    a mock CSV file, and the various test methods for the database methods.
    """
    mock_db_name = "test_product_db"
    mock_db = ProductDB(mock_db_name)
    mock_product = Product("product", 25, 50)
    mock_product_name = mock_product.get_product_name()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["product_name", "product_quantity", "product_price"])
            writer.writerow([self.mock_product_name, self.mock_product.get_product_quantity(),
                             self.mock_product.get_product_price()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_add_product(self):
        """This method tests the add_product method of the ProductDB class."""
        new_product = Product("new_product", 75, 100)
        self.mock_db.add_product(new_product)
        self.assertTrue(self.mock_db.product_exists(new_product.get_product_name()))

    def test_remove_product(self):
        """This method tests the remove_product method of the ProductDB class."""
        self.mock_db.remove_product(self.mock_product)
        self.assertFalse(self.mock_db.product_exists(self.mock_product_name))

    def test_edit_product(self):
        """This method tests the edit_product method of the ProductDB class."""
        edited_product_name = "edited_product"
        self.mock_db.edit_product(self.mock_product, 0, edited_product_name)
        edited_product = self.mock_db.get_product(edited_product_name)
        self.assertEqual(edited_product.get_product_name(), edited_product_name)

    def test_sub_product_quantity(self):
        """This method tests the sub_product_quantity method of the ProductDB class."""
        self.mock_db.sub_product_quantity(self.mock_product_name, 25)
        subtract_product = self.mock_db.get_product(self.mock_product_name)
        self.assertEqual(subtract_product.get_product_quantity(), 0)

    def test_get_product(self):
        """This method tests the get_product method of the ProductDB class."""
        product = self.mock_db.get_product(self.mock_product_name)
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.get_product_name(), self.mock_product_name)

    def test_get_all_products(self):
        """This method tests the get_all_products method of the ProductDB class."""
        products = self.mock_db.get_all_products()
        self.assertTrue(isinstance(products, List))
        self.assertEqual(products[0].get_product_name(), self.mock_product_name)

    def test_product_exists(self):
        """This method tests the product_exists method of the ProductDB class."""
        self.assertTrue(self.mock_db.product_exists(self.mock_product_name))


class TestUserDB(TestCase):
    """
    This class represents a test case for UserDB and implements TestCase.
    It contains the implemented abstract methods for setting up/tearing down
    a mock CSV file, and the various test methods for the database methods.
    """
    mock_db_name = "test_user_db"
    mock_db = UserDB(mock_db_name)
    mock_user = User("user", "password", 0, 1)
    mock_user_name = mock_user.get_user_name()
    mock_customer = Customer("customer", "password", 1)
    mock_customer_name = mock_customer.get_user_name()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "is_admin", "country_id", "discount_id"])
            writer.writerow([self.mock_user_name, self.mock_user.get_password(),
                             self.mock_user.get_is_admin(), self.mock_user.get_country_id(), -1])
            writer.writerow([self.mock_customer_name, self.mock_customer.get_password(),
                             self.mock_customer.get_is_admin(), self.mock_customer.get_country_id(),
                             self.mock_customer.get_discount_id()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_add_customer(self):
        """This method tests the add_customer method of the UserDB class."""
        new_customer = Customer("new_user", "password", 1)
        self.mock_db.add_customer(new_customer)
        self.assertTrue(self.mock_db.user_exists(new_customer.get_user_name()))

    def test_get_user(self):
        """This method tests the get_user method of the UserDB class."""
        user = self.mock_db.get_user(self.mock_user_name)
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.get_user_name(), self.mock_user_name)

    def test_get_customer(self):
        """This method tests the get_customer method of the UserDB class."""
        customer = self.mock_db.get_customer(self.mock_user_name)
        self.assertTrue(isinstance(customer, Customer))
        self.assertEqual(customer.get_user_name(), self.mock_user_name)

    def test_get_all_customers(self):
        """This method tests the get_all_customers method of the UserDB class."""
        customers = self.mock_db.get_all_customers()
        self.assertTrue(isinstance(customers, List))
        self.assertEqual(customers[0].get_user_name(), self.mock_user_name)

    def test_set_customer_discount(self):
        """This method tests the set_customer_discount method of the UserDB class."""
        discount_id = 0
        self.mock_db.set_customer_discount(self.mock_user_name, discount_id)
        self.assertEqual(self.mock_db.get_customer(self.mock_user_name).get_discount_id(),
                         discount_id)

    def test_user_exists(self):
        """This method tests the user_exists method of the UserDB class."""
        self.assertTrue(self.mock_db.user_exists(self.mock_user_name))


class TestOrderDB(TestCase):
    """
    This class represents a test case for OrderDB and implements TestCase.
    It contains the implemented abstract methods for setting up/tearing down
    a mock CSV file, and the various test methods for the database methods.
    """
    mock_db_name = "test_order_db"
    mock_db = OrderDB(mock_db_name)
    mock_products = ["product1"]
    mock_order = Order("user", mock_products, datetime.now(), 100.0)
    mock_customer_name = mock_order.get_customer_name()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["customer_name", "product_name", "order_date", "subtotal"])
            order_separator = "================"
            writer.writerow([self.mock_customer_name, order_separator, order_separator,
                             order_separator])
            writer.writerow([self.mock_customer_name, self.mock_products[0],
                             self.mock_order.get_order_date(),
                             self.mock_order.get_order_subtotal()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_add_order(self):
        """This method tests the add_order method of the OrderDB class."""
        new_order = Order("new_user", self.mock_products, datetime.now(), 50)
        self.mock_db.add_order(new_order)
        self.assertTrue(self.mock_db.orders_exist(new_order.get_customer_name()))

    def test_update_order_subtotals(self):
        """This method tests the update_order_subtotals method of the OrderDB class."""
        self.mock_db.update_order_subtotals(self.mock_customer_name, 0.10)
        self.assertEqual(self.mock_db.get_customer_orders(self.mock_customer_name)[1][3],
                         str(90.0))

    def test_get_customer_orders(self):
        """This method tests the get_customer_orders method of the OrderDB class."""
        orders = self.mock_db.get_customer_orders(self.mock_customer_name)
        self.assertTrue(isinstance(orders, List))
        self.assertEqual(orders[1][3], str(self.mock_order.get_order_subtotal()))

    def test_orders_exist(self):
        """This method tests the orders_exist method of the OrderDB class."""
        self.assertTrue(self.mock_db.orders_exist(self.mock_customer_name))


class TestCountryDB(TestCase):
    """
    This class represents a test case for CountryDB and implements TestCase.
    It contains the implemented abstract methods for setting up/tearing down
    a mock CSV file, and the various test methods for the database methods.
    """
    mock_db_name = "test_country_db"
    mock_db = CountryDB(mock_db_name)
    mock_country = Country(1, "Austria", 0.2, 16.0)
    mock_country_id = mock_country.get_country_id()

    def setUp(self):
        with open(self.mock_db_name + ".csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["country_id", "country_name", "vat_percentage", "shipping_cost"])
            writer.writerow([self.mock_country_id, self.mock_country.get_country_name(),
                             self.mock_country.get_vat_percentage(),
                             self.mock_country.get_shipping_cost()])

    def tearDown(self):
        os.remove(self.mock_db_name + ".csv")

    def test_get_country(self):
        """This method tests the get_country method of the CountryDB class."""
        country = self.mock_db.get_country(self.mock_country_id)
        self.assertTrue(isinstance(country, Country))
        self.assertEqual(country.get_country_id(), self.mock_country_id)

    def test_get_all_countries_id_name(self):
        """This method tests the get_all_countries_id_name method of the CountryDB class."""
        countries_id_name = self.mock_db.get_all_countries_id_name()
        self.assertTrue(isinstance(countries_id_name, List))
        self.assertEqual(countries_id_name[0][0], self.mock_country_id)
