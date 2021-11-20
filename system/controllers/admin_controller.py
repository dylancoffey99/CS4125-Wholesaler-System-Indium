import tkinter as tk
from tkinter import ttk
from typing import List
from system import views
from system.database.db_handler import UserDB
from system.database.db_handler import OrderDB
from system.database.db_handler import ProductDB
from system.controllers.abstract_controllers import AbstractAdminController


class AdminController(AbstractAdminController):
    def __init__(self, access_controller):
        self.root = access_controller.root
        self.user = access_controller.user
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
        self.insert_order(tree_view, orders)

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
                tree_view.insert("", "end", text="Item", values=(product_name, "", ""))
            else:
                tree_view.insert("", "end", text="Item", values=(product_name, date, subtotal))
