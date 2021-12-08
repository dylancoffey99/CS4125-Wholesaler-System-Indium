import tkinter as tk
from tkinter import ttk
from typing import List
from datetime import datetime
from system.views import HomeView, CustomerView
from system.models.shopping.order import Order
from system.models.shopping.basket import Basket
from system.database.db_handler import OrderDB, ProductDB, CountryDB
from system.controllers.abstract_controllers import AbstractCustomerController


class CustomerController(AbstractCustomerController):
    def __init__(self, access_controller):
        self.access_controller = access_controller
        self.order_db = OrderDB("system/database/csv/orderDB")
        self.product_db = ProductDB("system/database/csv/productDB")
        self.country_db = CountryDB("system/database/csv/countryDB")
        self.input = {"product_name": tk.StringVar(),
                      "product_quantity": tk.StringVar()}
        self.view = CustomerView(self.access_controller.root, self)
        self.basket = Basket([], 0)

    def fill_products(self) -> List[str]:
        products = self.product_db.get_all_products()
        product_names = []
        for product, _ in enumerate(products):
            product_names.append(products[product].get_product_name())
        return product_names

    def add_product(self, tree_view: ttk.Treeview):
        product_name = self.input["product_name"].get()
        quantity = self.input["product_quantity"].get()
        if product_name == "":
            print("Error: please select a product!")
        elif quantity == "":
            print("Error: please enter the quantity!")
        else:
            product = self.product_db.get_product(product_name)
            price = float(quantity) * product.get_product_price()
            self.basket.add_item(product)
            self.basket.add_basket_subtotal(price)
            self.insert_item(tree_view, product_name, quantity, price)

    def remove_product(self, tree_view: ttk.Treeview):
        selected_item = tree_view.focus()
        if not selected_item:
            print("Error: please select from the basket items!")
        else:
            item_dict = tree_view.item(selected_item)
            values = list(item_dict.values())
            product_name = values[2][0]
            quantity = values[2][1]
            products = self.basket.get_basket_items()
            for product in products:
                if product.get_product_name() == product_name:
                    price = float(quantity) * product.get_product_price()
                    self.basket.remove_item(product)
                    self.basket.sub_basket_subtotal(price)
                    self.remove_item(tree_view)

    def checkout(self, tree_view: ttk.Treeview):
        if len(tree_view.get_children("")) == 0:
            print("Error: the basket is empty, please add some products!")
        else:
            customer_name = self.access_controller.user.get_user_name()
            tree_list = list(tree_view.get_children(''))
            products = self.basket.get_basket_items()
            product_names = []
            for row in tree_list:
                product_name = tree_view.item(row, 'values')[0]
                quantity = int(tree_view.item(row, 'values')[1])
                for product in products:
                    if product_name == product.get_product_name():
                        self.product_db.sub_product_quantity(product, quantity)
                        product_names.append(product.get_product_name())
            self.create_order(customer_name, product_names)
            self.clear_items(tree_view)
            self.basket = Basket([], 0)
            print("Checkout successful, your order has been created!")

    def create_order(self, customer_name, product_names):
        country_id = self.access_controller.user.get_country_id()
        country = self.country_db.get_country(country_id)
        basket_subtotal = self.basket.get_basket_subtotal()
        order_subtotal = (basket_subtotal * (1 + country.get_vat_percentage())
                          + country.get_shipping_cost())
        order = Order(customer_name, product_names, datetime.now(), order_subtotal)
        self.order_db.add_order(order)

    def logout_user(self, root: tk.Tk, frame: tk.Frame):
        self.destroy_frame(frame)
        for child in root.winfo_children():
            child.destroy()
        self.view = HomeView(self.access_controller.root, self.access_controller)
        print("Logout successful!")

    def destroy_frame(self, frame: tk.Frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()

    @staticmethod
    def insert_item(tree_view: ttk.Treeview, product_name: str, quantity: int, price: float):
        tree_view.insert('', 'end', text="Item", values=(product_name, quantity, price))

    @staticmethod
    def remove_item(tree_view: ttk.Treeview):
        selected_item = tree_view.selection()[0]
        tree_view.delete(selected_item)

    @staticmethod
    def clear_items(tree_view: ttk.Treeview):
        for item in tree_view.get_children():
            tree_view.delete(item)
