from typing import List
from datetime import datetime
from tkinter import messagebox as mb
from system.views import HomeView, CustomerView
from system.database.db_handler import OrderDB, ProductDB, CountryDB
from system.models.shopping.order import Order
from system.models.shopping.basket import Basket
from system.controllers.abstract_controllers import AbstractController, AbstractObserverController


class CustomerController(AbstractController, AbstractObserverController):
    def __init__(self, access_controller):
        self.access_controller = access_controller
        self.order_db = OrderDB("system/database/csv/orderDB")
        self.product_db = ProductDB("system/database/csv/productDB")
        self.country_db = CountryDB("system/database/csv/countryDB")
        self.view = CustomerView(self.access_controller.root, self.access_controller.frame,
                                 self.access_controller.user)
        self.view.set_combobox(self.fill_products())
        self.tree_view = self.view.get_tree_view()
        self.attach_observers()
        self.basket = Basket([], 0)

    def fill_products(self) -> List[str]:
        products = self.product_db.get_all_products()
        product_names = []
        for product in products:
            product_names.append(product.get_product_name())
        return product_names

    def add_product(self):
        product_name = self.view.get_input_value("product_name")
        quantity = self.view.get_input_value("product_quantity")
        if product_name == "" or quantity == "":
            mb.showwarning("Error", "Please enter all fields!")
        elif not quantity.isdigit() or quantity == str(0):
            mb.showwarning("Error", "The quantity entered is not a valid number!")
        else:
            product = self.product_db.get_product(product_name)
            if self.basket.item_exists(product_name):
                mb.showwarning("Error", "That product is already in the basket!")
            elif product.get_product_quantity() == 0:
                mb.showwarning("Error", "Product out of stock!")
            elif int(quantity) > product.get_product_quantity():
                mb.showwarning("Error", "The quantity entered is too high,"
                                        " not enough left in stock!")
            else:
                price = float(quantity) * product.get_product_price()
                self.basket.add_item(product)
                self.basket.add_basket_subtotal(price)
                self.view.insert_item(self.tree_view, product_name, int(quantity), price)

    def remove_product(self):
        selected_item = self.tree_view.focus()
        if len(self.tree_view.get_children("")) == 0:
            mb.showwarning("Error", "The basket is empty, there aren't any products to remove!")
        elif not selected_item:
            mb.showwarning("Error", "Please select a product from the basket!")
        else:
            item_dict = self.tree_view.item(selected_item)
            values = list(item_dict.values())
            product_name = values[2][0]
            quantity = values[2][1]
            products = self.basket.get_basket_items()
            for product in products:
                if product.get_product_name() == product_name:
                    price = float(quantity) * product.get_product_price()
                    self.basket.remove_item(product)
                    self.basket.sub_basket_subtotal(price)
                    self.view.remove_item(self.tree_view)

    def checkout(self):
        if len(self.tree_view.get_children("")) == 0:
            mb.showwarning("Error", "The basket is empty, please add some products to the basket!")
        else:
            customer_name = self.access_controller.user.get_user_name()
            tree_list = list(self.tree_view.get_children(""))
            products = self.basket.get_basket_items()
            product_names = []
            for row in tree_list:
                product_name = self.tree_view.item(row, "values")[0]
                quantity = int(self.tree_view.item(row, "values")[1])
                for product in products:
                    if product_name == product.get_product_name():
                        self.product_db.sub_product_quantity(product, quantity)
                        product_names.append(product.get_product_name())
            self.create_order(customer_name, product_names)
            self.basket.clear_items()
            self.view.clear_tree_view(self.tree_view)
            mb.showwarning("Success", "Checkout successful, your order has been created!")

    def create_order(self, customer_name: str, product_names: List[str]):
        country_id = self.access_controller.user.get_country_id()
        country = self.country_db.get_country(country_id)
        basket_subtotal = self.basket.get_basket_subtotal()
        order_subtotal = (basket_subtotal * (1 + country.get_vat_percentage())
                          + country.get_shipping_cost())
        order = Order(customer_name, product_names, datetime.now(), order_subtotal)
        self.order_db.add_order(order)

    def logout_user(self):
        self.view.clear_frame()
        self.view = HomeView(self.access_controller.root, self.access_controller.frame,
                             self.access_controller.observers)
        self.access_controller.user = None

    def attach_observers(self):
        self.view.attach((1, self.add_product))
        self.view.attach((2, self.remove_product))
        self.view.attach((3, self.checkout))
        self.view.attach((4, self.logout_user))
