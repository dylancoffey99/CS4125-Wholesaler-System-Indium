import tkinter as tk
from tkinter import messagebox as mb

from system.controllers import AbstractObserverController
from system.controllers.admin_controller import AdminController
from system.controllers.customer_controller import CustomerController
from system.models.access import UserAccess
from system.models.users.admin import Admin
from system.models.users.customer import Customer
from system.views import HomeView, LoginView, RegisterView


class AccessController(AbstractObserverController):
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.input = {"username": tk.StringVar(), "password": tk.StringVar(),
                      "r_password": tk.StringVar(), "country": tk.StringVar()}
        self.observers = []
        self.view = HomeView(self.root, self.frame, self.observers)
        self.user = None
        self.access = UserAccess()
        self.attach_observers()

    def start(self):
        self.root.mainloop()

    def login_view(self):
        self.view.clear_frame()
        self.clear_input()
        self.view = LoginView(self.frame, self.input, self.observers)

    def register_view(self):
        self.view.clear_frame()
        self.clear_input()
        self.view = RegisterView(self.frame, self.input, self.observers)
        self.view.set_combobox(self.access.get_country_names())

    def login_user(self):
        username = self.input["username"].get()
        password = self.input["password"].get()
        r_password = self.input["r_password"].get()
        if username == "" or password == "" or r_password == "":
            mb.showwarning("Error", "Please enter all the fields!")
        else:
            access = UserAccess()
            if not access.user_exists(username):
                mb.showwarning("Error", "That username does not exist!")
            elif password != r_password:
                mb.showwarning("Error", "The passwords are not the same!")
            else:
                if access.verify_password(password):
                    mb.showwarning("Error", "The password is incorrect!")
                else:
                    self.view.clear_frame()
                    self.clear_input()
                    self.user = access.get_user(username)
                    if access.is_admin(username):
                        self.user = Admin(self.user.get_user_name(), self.user.get_password())
                        AdminController(self)
                    else:
                        self.user = Customer(self.user.get_user_name(), self.user.get_password(),
                                             self.user.get_country_id())
                        CustomerController(self)

    def register_user(self):
        username = self.input["username"].get()
        password = self.input["password"].get()
        r_password = self.input["r_password"].get()
        country = self.input["country"].get()
        if username == "" or password == "" or r_password == "" or country == "":
            mb.showwarning("Error", "Please enter all the fields!")
        else:
            if self.access.user_exists(username):
                mb.showwarning("Error", "That username already exists!")
            elif password != r_password:
                mb.showwarning("Error", "The passwords are not the same!")
            else:
                country_dict = self.access.get_country_dict()
                self.view.clear_frame()
                self.clear_input()
                self.user = Customer(username, self.access.hash_password(password),
                                     country_dict.get(country))
                self.access.add_customer(self.user)
                CustomerController(self)

    def clear_input(self):
        for value in self.input.items():
            value = value[0]
            self.input[value].set("")

    def attach_observers(self):
        self.view.attach((1, self.login_user))
        self.view.attach((2, self.register_user))
        self.view.attach((3, self.login_view))
        self.view.attach((4, self.register_view))
