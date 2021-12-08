import tkinter as tk
from tkinter import ttk
from typing import List
from system.views import HomeView, AdminView
from system.models.users.customer import Customer
from system.models.shopping.discount import DiscountCategory
from system.database.db_handler import UserDB, OrderDB, ProductDB
from system.controllers.abstract_controllers import AbstractAdminController


class AdminController(AbstractAdminController):
    def __init__(self, access_controller):
        self.access_controller = access_controller
        self.user_db = UserDB("system/database/csv/userDB")
        self.order_db = OrderDB("system/database/csv/orderDB")
        self.product_db = ProductDB("system/database/csv/productDB")
        self.order_input = {"user_name": tk.StringVar(),
                            "discount_category": tk.StringVar()}
        self.view = AdminView(self.access_controller.root, self)
        self.customer = None

    def fill_users(self) -> List[str]:
        users = self.user_db.get_all_users()
        user_names = []
        for user, _ in enumerate(users):
            if users[user].get_is_admin() == 0:
                user_names.append(users[user].get_user_name())
        return user_names

    def fill_products(self):
        products = self.product_db.get_all_products()
        product_names = []
        for product, _ in enumerate(products):
            product_names.append(products[product].get_product_name())
        return product_names

    def view_order(self, tree_view: ttk.Treeview):
        user_name = self.order_input["user_name"].get()
        orders = self.order_db.get_customer_orders(user_name)
        if not orders:
            print("Error: this user does not have any orders!")
        else:
            self.clear_orders(tree_view)
            self.insert_order(tree_view, orders)

    def add_discount(self, tree_view: ttk.Treeview):
        user_name = self.order_input["user_name"].get()
        discount_category = self.order_input["discount_category"].get()
        if user_name == "":
            print("Error: please select a user!")
        elif discount_category == "":
            print("Error: please select a discount category!")
        else:
            if self.customer is None:
                user = self.user_db.get_user(user_name)
                self.customer = Customer(user.get_user_name(), user.get_password(),
                                         user.get_is_admin(), user.get_country_id())
            if user_name != self.customer.get_user_name():
                self.customer = None
            elif isinstance(self.customer.get_discount_category(), DiscountCategory):
                print("Error: customer already has a discount category!")
            else:
                discount = self.check_discount(discount_category)
                self.customer.set_discount_category(discount)
                self.update_orders(tree_view, discount)
                self.order_db.update_order_subtotals(user_name, discount.get_discount_percentage())

    def add_product(self, tree_view: ttk.Treeview):
        product_name = self.input["product_name"].get()
        quantity = self.input["product_quantity"].get()
        product = self.product_db.get_product(product_name)
        price = float(quantity) * product.get_product_price()
        self.product_db.add_product(product)
        self.product_db.get_product_price(price)
        self.insert_data(tree_view, product_name, quantity, price)

    def edit_product(self, tree_view: ttk.Treeview):
        product_name = self.input["product_name"].get()
        quantity = self.input["product_quantity"].get()
        product = self.product_db.get_product(product_name)
        price = float(quantity) * product.get_product_price()
        self.product_db.add_product(product)
        self.product_db.get_product_price(price)
        self.insert_data(tree_view, product_name, quantity, price)

    def remove_product(self, tree_view: ttk.Treeview):
        pass

    def logout_user(self, frame: tk.Frame):
        self.destroy_frame(frame)
        self.view = HomeView(self.access_controller.root, self.access_controller)
        print("Logout successful!")

    def destroy_frame(self, frame: tk.Frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()

    @staticmethod
    def insert_order(tree_view: ttk.Treeview, orders: List):
        for order in orders:
            product_name = order[1]
            date_time = order[2]
            subtotal = order[3]
            tree_view.insert("", "end", text="Order", values=(product_name, date_time, subtotal))

    @staticmethod
    def update_orders(tree_view: ttk.Treeview, discount_category: DiscountCategory):
        tree_list = list(tree_view.get_children(""))
        for order in tree_list:
            product_name = tree_view.item(order, "values")[0]
            date_time = tree_view.item(order, "values")[1]
            subtotal = float(tree_view.item(order, "values")[2])
            discount = subtotal * discount_category.get_discount_percentage()
            subtotal -= discount
            tree_view.item(order, text="Order", values=(product_name, date_time, subtotal))

    @staticmethod
    def clear_orders(tree_view: ttk.Treeview):
        for order in tree_view.get_children():
            tree_view.delete(order)

    @staticmethod
    def check_discount(discount_category):
        if discount_category == "Education":
            discount = DiscountCategory(0, "Education", 0.10)
        elif discount_category == "Small Business":
            discount = DiscountCategory(0, "Small Business", 0.15)
        else:
            discount = DiscountCategory(0, "Start-up Business", 0.20)
        return discount
