import tkinter as tk
from tkinter import ttk
from system.views.registration_view import RegistrationView
from system.views.user_view import UserView


class LoginView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Login Page", font='Aerial 20 bold')
        label.grid(row=0, column=3, padx=10, pady=10)

        name_label = ttk.Label(self, text="Name", font='Aerial 12')
        name_label.grid(row=3, column=2)
        password_label = ttk.Label(self, text="Password", font='Aerial 12')
        password_label.grid(row=4, column=2)

        name_entry = ttk.Entry(self)
        name_entry.grid(row=3, column=3, padx=10, pady=10)
        password_entry = ttk.Entry(self)
        password_entry.grid(row=4, column=3, padx=10, pady=10)

        login_button = ttk.Button(self, text="Login",
                                  command=lambda: controller.show_frame(UserView))

        login_button.grid(row=6, column=2, padx=10, pady=10)

        register_button = ttk.Button(self, text="Register",
                                     command=lambda: controller.show_frame(RegistrationView))

        register_button.grid(row=6, column=3, padx=10, pady=10)
