from tkinter import ttk
from system.views.abstract_view import AbstractView


class LoginView(AbstractView):
    def __init__(self, frame, controller):
        self.frame = frame
        self.controller = controller
        self.setup_view()

    def setup_view(self):
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
        login_button = ttk.Button(self.frame, text="Login",
                                  command=self.controller.login_user())
        login_button.grid(row=4, column=0, padx=10, pady=20)
        register_button = ttk.Button(self.frame, text="Don't have an account?",
                                     command=self.controller.register_view())
        register_button.grid(row=4, column=1, padx=10, pady=20)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
