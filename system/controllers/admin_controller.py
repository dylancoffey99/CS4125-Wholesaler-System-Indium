import tkinter as tk
from tkinter import ttk
from typing import List
from system import views
from system.database.db_handler import UserDB
from system.database.db_handler import OrderDB
from system.database.db_handler import ProductDB
from system.models.users.customer import Customer
from system.models.shopping.discount import DiscountCategory
from system.controllers.abstract_controllers import AbstractAdminController


class AdminController(AbstractAdminController):
    def __init__(self, access_controller):
        self.root = access_controller.root
        self.access_controller = access_controller
        self.user_db = UserDB("system/database/userDB")
        self.order_db = OrderDB("system/database/orderDB")
        self.product_db = ProductDB("system/database/productDB")
        self.order_input = {"user_name": tk.StringVar(),
                            "discount_category": tk.StringVar()}
        self.view = views.AdminView(self.root, self)

    def fill_users(self):
        users = self.user_db.get_all_users()
        user_names = []
        for user, _ in enumerate(users):
            if users[user].get_is_admin() == 0:
                user_names.append(users[user].get_user_name())
        return user_names

    def view_order(self, tree_view: ttk.Treeview):
        user_name = self.order_input["user_name"].get()
        orders = self.order_db.get_customer_orders(user_name)
        print(orders)
        if not orders:
            print("Error: this user does not have any orders!")
        else:
            self.clear_orders(tree_view)
            self.insert_order(tree_view, orders)

    def add_discount(self, tree_view: ttk.Treeview):
        user_name = self.order_input["user_name"].get()
        discount_category = self.order_input["discount_category"].get()
        if discount_category == "Education":
            discount = DiscountCategory(0, "Education", 0.10)
        elif discount_category == "Small Business":
            discount = DiscountCategory(0, "Small Business", 0.15)
        else:
            discount = DiscountCategory(0, "Start-up Business", 0.20)
        user = self.user_db.get_user(user_name)
        customer = Customer(user.get_user_name(), user.get_password(),
                            user.get_is_admin(), user.get_country_id())
        customer.set_discount_category(discount)

        self.update_orders(tree_view, discount)

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
    def insert_order(tree_view: ttk.Treeview, orders: List):
        for product in orders:
            product_name = product[1]
            date = product[2]
            subtotal = product[3]
            if product != orders[-1]:
                tree_view.insert("", "end", text="Order", values=(product_name, "", ""))
            else:
                tree_view.insert("", "end", text="Order", values=(product_name, date, subtotal))

    @staticmethod
    def clear_orders(tree_view: ttk.Treeview):
        for order in tree_view.get_children():
            tree_view.delete(order)

    @staticmethod
    def update_orders(tree_view: ttk.Treeview, discount_category: DiscountCategory):
        tree_list = list(tree_view.get_children(""))
        for order in tree_list:
            if order == tree_list[-1]:
                product_name = tree_view.item(order, "values")[0]
                date = tree_view.item(order, "values")[1]
                subtotal = float(tree_view.item(order, "values")[2])
                discount = subtotal * discount_category.get_discount_percentage()
                subtotal -= discount
                tree_view.item(order, text="Order", values=(product_name, date, subtotal))
