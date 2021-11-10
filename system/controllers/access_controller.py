import hashlib
import tkinter as tk
from system import views
from system.database.db_handler import UserDB
from system.models.users.customer import Customer
from system.controllers.abstract_controllers import AbstractAccessController


class AccessController(AbstractAccessController):
    def __init__(self):
        self.root = tk.Tk()
        self.user_db = UserDB("system/database/userDB")
        self.view = views.HomeView(self.root, self)
        self.input = {}

    def start(self):
        self.root.mainloop()

    def login_view(self, root, frame):
        self.destroy_frame(frame)
        self.view = views.LoginView(root, self)

    def register_view(self, root, frame):
        self.destroy_frame(frame)
        self.input = {"username": tk.StringVar(), "password": tk.StringVar(),
                      "r_password": tk.StringVar(), "country": tk.StringVar()}
        self.view = views.RegisterView(root, self)

    def login_user(self, user_name: str, password: str):
        country_id = User.get_country_id(self)
        is_admin = User.get_is_admin(self)
        user = User(user_name, password, is_admin, country_id)
        self.user_db.get_user(user)
        print("Login successful!")

    def register_user(self, root, frame):
        username = self.input["username"].get()
        password = self.input["password"].get()
        r_password = self.input["r_password"].get()
        country = self.input["country"].get()
        if username == "" or password == "" or r_password == "" or country == "":
            print("Error: please enter all the fields!")
        elif password != r_password:
            print("Error: the passwords are not the same!")
        else:
            if not self.user_db.user_exists(username):
                print("Error: that username already exists!")
            else:
                country_dict = {"Austria": 1, "Belgium": 2, "Bulgaria": 3, "Croatia": 4,
                                "Cyprus": 5, "Czech": 6, "Denmark": 7, "Estonia": 8,
                                "Finland": 9, "France": 10, "Germany": 11, "Greece": 12,
                                "Hungary": 13, "Ireland": 14, "Italy": 15, "Latvia": 16,
                                "Lithuania": 17, "Luxembourg": 18, "Malta": 19,
                                "Netherlands": 20, "Poland": 21, "Portugal": 22,
                                "Romania": 23, "Slovakia": 24, "Slovenia": 25,
                                "Spain": 26, "Sweden": 27, "United Kingdom": 28}
                customer = Customer(username, self.hash_password(password), country_dict.get(country))
                self.user_db.add_user(customer)
                self.destroy_frame(frame)
                self.view = views.CustomerView(root, self)
                print("Registration successful!")

    def destroy_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()

    def hash_password(self, password: str) -> str:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password
