import tkinter as tk
from tkinter import ttk


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.setup_view()
        self.load_widgets()

    def setup_view(self):
        self.root.geometry("600x500")
        self.root.title("Wholesaler System")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0)

    def load_widgets(self):
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        login_label = ttk.Label(self.frame, text="Login", font=(None, 20))
        login_label.grid(row=0, columnspan=2, pady=20)
        user_name_label = ttk.Label(self.frame, text="Username", font=(None, 11))
        user_name_label.grid(row=1, column=0, pady=10)
        password_label = ttk.Label(self.frame, text="Password", font=(None, 11))
        password_label.grid(row=2, column=0, pady=10)
        repeat_password_label = ttk.Label(self.frame, text="Repeat Password", font=(None, 11))
        repeat_password_label.grid(row=3, column=0, pady=10)

    def load_interactions(self):
        user_name_entry = ttk.Entry(self.frame, width=27,
                                    textvariable=self.controller.input["username"])
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self.frame, width=27, show="*",
                                   textvariable=self.controller.input["password"])
        password_entry.grid(row=2, column=1, padx=10, pady=10)
        repeat_password_entry = ttk.Entry(self.frame, width=27, show="*",
                                          textvariable=self.controller.input["r_password"])
        repeat_password_entry.grid(row=3, column=1, padx=10, pady=10)
        login_button = ttk.Button(self.frame, text="Login", command=lambda:
                                  self.controller.login_user(self.root, self.frame))
        login_button.grid(row=4, column=0, padx=10, pady=20)
        register_button = ttk.Button(self.frame, text="Don't have an account?", command=lambda:
                                     self.controller.register_view(self.root, self.frame))
        register_button.grid(row=4, column=1, padx=10, pady=20)
