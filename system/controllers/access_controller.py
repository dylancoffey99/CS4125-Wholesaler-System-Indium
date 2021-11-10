import hashlib
import tkinter as tk
from system import views
from system.database.db_handler import UserDB
from system.controllers.abstract_controllers import AbstractAccessController


class AccessController(AbstractAccessController):
    def __init__(self):
        self.root = tk.Tk()
        self.user_db = UserDB("system/database/userDB")
        self.view = views.HomeView(self.root, self)

    def start(self):
        self.root.mainloop()

    def login_view(self, root, frame):
        self.destroy_frame(frame)
        self.view = views.LoginView(root, self)

    def register_view(self, root, frame):
        self.destroy_frame(frame)
        self.view = views.RegisterView(root, self)

    def login_user(self, user_name: str, password: str):
        country_id = User.get_country_id(self)
        is_admin = User.get_is_admin(self)
        user = User(user_name, password, is_admin, country_id)
        self.user_db.get_user(user)
        print("Login successful!")

    def register_user(self, user_name: str, password: str, country_id: int):
        pass

    def destroy_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()

    def hash_password(self, password: str) -> str:
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password
