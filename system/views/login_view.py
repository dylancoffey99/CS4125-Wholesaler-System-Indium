import tkinter as tk
from tkinter import ttk


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Frame labels
        login_label = ttk.Label(self.frame, text="Login", font=(None, 20))
        login_label.grid(row=0, columnspan=2, pady=20)
        user_name_label = ttk.Label(self.frame, text="Username", font=(None, 11))
        user_name_label.grid(row=1, column=0, pady=10)
        password_label = ttk.Label(self.frame, text="Password", font=(None, 11))
        password_label.grid(row=2, column=0, pady=10)
        repeat_password_label = ttk.Label(self.frame, text="Repeat Password", font=(None, 11))
        repeat_password_label.grid(row=3, column=0, pady=10)

        # Frame entries
        user_name_entry = ttk.Entry(self.frame, width=27)
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self.frame, width=27, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=10)
        repeat_password_entry = ttk.Entry(self.frame, width=27, show="*")
        repeat_password_entry.grid(row=3, column=1, padx=10, pady=10)

        # Frame buttons
        login_button = ttk.Button(self.frame, text="Login")
        login_button.grid(row=4, column=0, padx=10, pady=20)
        register_button = ttk.Button(self.frame, text="Don't have an account?", command=lambda:
                                     self.controller.register_view(self.root, self.frame))
        register_button.grid(row=4, column=1, padx=10, pady=20)
