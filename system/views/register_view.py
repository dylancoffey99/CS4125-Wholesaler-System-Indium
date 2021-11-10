import tkinter as tk
from tkinter import ttk


class RegisterView:
    def __init__(self, root, controller):
        self.root = root
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Frame labels
        register_label = ttk.Label(self.frame, text="Registration", font=(None, 20))
        register_label.grid(row=0, columnspan=2, pady=20)
        user_name_label = ttk.Label(self.frame, text="Username", font=(None, 11))
        user_name_label.grid(row=1, column=0, pady=10)
        country_label = ttk.Label(self.frame, text="Country", font=(None, 11))
        country_label.grid(row=2, column=0, pady=10)
        password_label = ttk.Label(self.frame, text="Password", font=(None, 11))
        password_label.grid(row=3, column=0, pady=10)
        repeat_password_label = ttk.Label(self.frame, text="Repeat Password", font=(None, 11))
        repeat_password_label.grid(row=4, column=0, pady=10)

        # Frame combobox/entries
        user_name_entry = ttk.Entry(self.frame, width=27,
                                    textvariable=self.controller.input["username"])
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)
        country_combobox = ttk.Combobox(self.frame, width=24, state="readonly",
                                        textvariable=self.controller.input["country"])
        country_combobox.grid(row=2, column=1, padx=10, pady=10)
        country_combobox["values"] = ("Austria", "Belgium", "Bulgaria", "Croatia",
                                      "Cyprus", "Czech", "Denmark", "Estonia",
                                      "Finland", "France", "Germany", "Greece",
                                      "Hungary", "Ireland", "Italy", "Latvia",
                                      "Lithuania", "Luxembourg", "Malta",
                                      "Netherlands", "Poland", "Portugal",
                                      "Romania", "Slovakia", "Slovenia",
                                      "Spain", "Sweden", "United Kingdom")
        password_entry = ttk.Entry(self.frame, width=27, show="*",
                                   textvariable=self.controller.input["password"])
        password_entry.grid(row=3, column=1, padx=10, pady=10)
        repeat_password_entry = ttk.Entry(self.frame, width=27, show="*",
                                          textvariable=self.controller.input["r_password"])
        repeat_password_entry.grid(row=4, column=1, padx=10, pady=10)

        # Frame buttons
        register_button = ttk.Button(self.frame, text="Register", command=lambda:
                                     self.controller.register_user(self.root, self.frame))
        register_button.grid(row=5, column=0, padx=10, pady=20)
        login_button = ttk.Button(self.frame, text="Already have an account?", command=lambda:
                                  self.controller.login_view(self.root, self.frame))
        login_button.grid(row=5, column=1, padx=10, pady=20)
