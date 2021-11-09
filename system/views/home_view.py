import tkinter as tk
from tkinter import ttk


class HomeView:
    def __init__(self, root, controller):
        self.root = root
        self.root.geometry("600x500")
        self.root.title("Wholesaler System")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.resizable(width=False, height=False)
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Frame labels
        system_label = ttk.Label(self.frame, text="Wholesaler System", font=(None, 20))
        system_label.grid(row=0, column=0, pady=10)

        # Frame buttons
        login_button = ttk.Button(self.frame, text="Login")
        login_button.grid(row=1, column=0, pady=10)
        register_button = ttk.Button(self.frame, text="Register")
        register_button.grid(row=2, column=0, pady=10)
