import tkinter as tk
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
        self.view = views.CustomerView(self.root, self)
        self.basket = None
        self.fill_products()
        self.create_basket()

    def fill_products(self):
        products = self.product_db.get_all_products()
        product_names = []
        for product, _ in enumerate(products):
            product_names.append(products[product].get_product_name())
        return product_names

    def create_basket(self):
        basket_items = []
        basket_subtotal = 0
        self.basket = Basket(basket_items, basket_subtotal)

    def add_product(self, tree_view: ttk.Treeview):
        product_name = self.input["product_name"].get()
        quantity = self.input["product_quantity"].get()
        product = self.product_db.get_product(product_name)
        price = float(quantity) * product.get_product_price()
        self.basket.add_item(product)
        self.basket.add_basket_subtotal(price)
        self.insert_data(tree_view, product_name, quantity, price)

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
    def insert_data(tree_view: ttk.Treeview, product_name: str, quantity: int, price: float):
        tree_view.insert('', 'end', text="Item", values=(product_name, quantity, price))
