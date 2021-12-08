from tkinter import ttk
from system.views.abstract_view import AbstractView


class RegisterView(AbstractView):
    def __init__(self, frame, controller):
        self.frame = frame
        self.controller = controller
        self.setup_view()

    def setup_view(self):
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
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

    def load_interactions(self):
        user_name_entry = ttk.Entry(self.frame, width=27,
                                    textvariable=self.controller.input["username"])
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self.frame, width=27, show="*",
                                   textvariable=self.controller.input["password"])
        password_entry.grid(row=3, column=1, padx=10, pady=10)
        repeat_password_entry = ttk.Entry(self.frame, width=27, show="*",
                                          textvariable=self.controller.input["r_password"])
        repeat_password_entry.grid(row=4, column=1, padx=10, pady=10)
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
        register_button = ttk.Button(self.frame, text="Register",
                                     command=self.controller.register_user)
        register_button.grid(row=5, column=0, padx=10, pady=20)
        login_button = ttk.Button(self.frame, text="Already have an account?",
                                  command=self.controller.login_view)
        login_button.grid(row=5, column=1, padx=10, pady=20)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
