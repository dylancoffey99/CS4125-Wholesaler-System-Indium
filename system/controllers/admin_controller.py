import tkinter as tk
from system import views
from system.database.db_handler import ProductDB
from system.controllers.abstract_controllers import AbstractAdminController


class AdminController(AbstractAdminController):
    def __init__(self, root, user, access_controller):
        self.root = root
        self.user = user
        self.access_controller = access_controller
        self.product_db = ProductDB("system/database/productDB")
        self.view = views.AdminView(self.root, self)
        self.input = {}

    def logout_admin(self, root: tk.Tk, frame: tk.Frame):
        self.destroy_frame(frame)
        for child in root.winfo_children():
            child.destroy()
        self.view = views.LoginView(self.root, self.access_controller)
        print("Logout successful!")

    def destroy_frame(self, frame: tk.Frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()
