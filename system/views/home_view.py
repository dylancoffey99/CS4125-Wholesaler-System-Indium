"""
This module contains the HomeView class. The module imports the ttk module from the
tkinter package, and the AbstractView class from the abstract_views module, in the
systems views package.
"""
from tkinter import ttk

from system.views.abstract_views import AbstractView


class HomeView(AbstractView):
    """
    This class represents the home view of the system and implements AbstractView.
    It contains a constructor, the setup/load methods for the root/widgets, and the
    implemented abstract methods.
    """

    def __init__(self, root, frame, observers):
        """
        This constructor instantiates a home view object.

        :param root: Tkinter window to hold the frame of the view.
        :param frame: Tkinter frame to hold the widgets of the view.
        :param observers: List to hold the observers of the view.
        """
        self.root = root
        self.frame = frame
        self.observers = observers
        self.setup_view()

    def setup_view(self):
        self.root.geometry("600x500")
        self.root.title("Wholesaler System")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.resizable(width=False, height=False)
        self.frame.grid(row=0, column=0)
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        system_label = ttk.Label(self.frame, text="Wholesaler System", font=(None, 20))
        system_label.grid(row=0, column=0, pady=10)

    def load_interactions(self):
        login_button = ttk.Button(self.frame, text="Login", command=lambda: self.notify(3))
        login_button.grid(row=1, column=0, pady=10)
        register_button = ttk.Button(self.frame, text="Register", command=lambda: self.notify(4))
        register_button.grid(row=2, column=0, pady=10)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, command: int):
        for observer in self.observers:
            if observer[0] == command:
                observer[1]()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
