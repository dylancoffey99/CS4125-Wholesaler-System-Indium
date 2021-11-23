import tkinter as tk
from tkinter import ttk
from system import views
from system.database.db_handler import ProductDB
from system.models.shopping.basket import Basket
from system.controllers.abstract_controllers import AbstractCustomerController


class CustomerController(AbstractCustomerController):
    def __init__(self, root, access_controller):
        self.root = root
        self.user = access_controller.user
        self.access_controller = access_controller
        self.product_db = ProductDB("system/database/productDB")
        self.input = {"product_name": tk.StringVar(),
                      "product_quantity": tk.StringVar()}
        self.view = views.CustomerView(self.root, self)
        self.basket = Basket([], 0)
        self.fill_products()

    def fill_products(self):
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

    def checkout(self):
        pass

    def logout_user(self, root: tk.Tk, frame: tk.Frame):
        self.destroy_frame(frame)
        for child in root.winfo_children():
            child.destroy()
        self.view = views.LoginView(self.root, self.access_controller)
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
