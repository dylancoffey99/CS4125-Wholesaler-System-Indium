import hashlib
import tkinter as tk
from system.database.db_handler import UserDB
from system.models.users.customer import Customer
from system.views import HomeView, LoginView, RegisterView
from system.controllers.admin_controller import AdminController
from system.controllers.customer_controller import CustomerController
from system.controllers.abstract_controllers import AbstractAccessController


class AccessController(AbstractAccessController):
    def __init__(self):
        self.root = tk.Tk()
        self.user_db = UserDB("system/database/userDB")
        self.view = HomeView(self.root, self)
        self.input = {}
        self.user = None

    def start(self):
        self.root.mainloop()

    def login_view(self, frame: tk.Frame):
        self.destroy_frame(frame)
        self.input = {"username": tk.StringVar(), "password": tk.StringVar(),
                      "r_password": tk.StringVar()}
        self.view = LoginView(self.root, self)

    def register_view(self, frame: tk.Frame):
        self.destroy_frame(frame)
        self.input = {"username": tk.StringVar(), "password": tk.StringVar(),
                      "r_password": tk.StringVar(), "country": tk.StringVar()}
        self.view = RegisterView(self.root, self)

    def login_user(self, frame: tk.Frame):
        username = self.input["username"].get()
        password = self.input["password"].get()
        r_password = self.input["r_password"].get()
        if username == "" or password == "" or r_password == "":
            print("Error: please enter all the fields!")
        elif not self.user_db.user_exists(username):
            print("Error: that username does not exist!")
        elif password != r_password:
            print("Error: the passwords are not the same!")
        else:
            self.user = self.user_db.get_user(username)
            if self.user.get_password() != self.hash_password(password):
                print("Error: the password is incorrect!")
            else:
                self.destroy_frame(frame)
                if self.user.get_is_admin() == 1:
                    AdminController(self)
                else:
                    CustomerController(self)
                print("Login successful!")

    def register_user(self, frame: tk.Frame):
        username = self.input["username"].get()
        password = self.input["password"].get()
        r_password = self.input["r_password"].get()
        country = self.input["country"].get()
        if username == "" or password == "" or r_password == "" or country == "":
            print("Error: please enter all the fields!")
        elif self.user_db.user_exists(username):
            print("Error: that username already exists!")
        elif password != r_password:
            print("Error: the passwords are not the same!")
        else:
            country_dict = {"Austria": 1, "Belgium": 2, "Bulgaria": 3, "Croatia": 4,
                            "Cyprus": 5, "Czech": 6, "Denmark": 7, "Estonia": 8,
                            "Finland": 9, "France": 10, "Germany": 11, "Greece": 12,
                            "Hungary": 13, "Ireland": 14, "Italy": 15, "Latvia": 16,
                            "Lithuania": 17, "Luxembourg": 18, "Malta": 19,
                            "Netherlands": 20, "Poland": 21, "Portugal": 22,
                            "Romania": 23, "Slovakia": 24, "Slovenia": 25,
                            "Spain": 26, "Sweden": 27, "United Kingdom": 28}
            self.user = Customer(username, self.hash_password(password), country_dict.get(country))
            self.user_db.add_user(self.user)
            self.destroy_frame(frame)
            CustomerController(self)
            print("Registration successful!")

    def destroy_frame(self, frame: tk.Frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()

    @staticmethod
    def hash_password(password: str) -> str:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password
