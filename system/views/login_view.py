"""
This module contains the LoginView class. The module imports the ttk module from the
tkinter package, and the AbstractView class from the systems views package.
"""
from tkinter import ttk

from system.views.abstract_views import AbstractView


class LoginView(AbstractView):
    """
    This class represents the login view of the system and implements AbstractView.
    It contains a constructor, the setup/load methods for the root/widgets, and the
    implemented abstract methods.
    """

    def __init__(self, frame, access_input, observers):
        """
        This constructor instantiates a login view object.

        :param frame: Tkinter frame to hold the widgets of the view.
        :param access_input: Input dictionary to hold the inputs of the user.
        :param observers: List to hold the observers of the view.
        """
        self.frame = frame
        self.input = access_input
        self.observers = observers
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
                                    textvariable=self.input["username"])
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self.frame, width=27, show="*",
                                   textvariable=self.input["password"])
        password_entry.grid(row=2, column=1, padx=10, pady=10)
        repeat_password_entry = ttk.Entry(self.frame, width=27, show="*",
                                          textvariable=self.input["r_password"])
        repeat_password_entry.grid(row=3, column=1, padx=10, pady=10)
        login_button = ttk.Button(self.frame, text="Login", command=lambda: self.notify(1))
        login_button.grid(row=4, column=0, padx=10, pady=20)
        register_button = ttk.Button(self.frame, text="Don't have an account?",
                                     command=lambda: self.notify(4))
        register_button.grid(row=4, column=1, padx=10, pady=20)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, command: int):
        for observer in self.observers:
            if observer[0] == command:
                observer[1]()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
