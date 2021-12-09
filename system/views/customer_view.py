import tkinter as tk
from tkinter import ttk
from typing import List
from system.views.abstract_views import AbstractView, AbstractUserView


class CustomerView(AbstractView, AbstractUserView):
    def __init__(self, root, frame, user):
        self.root = root
        self.frame = frame
        self.user = user
        self.input = {"product_name": tk.StringVar(), "product_quantity": tk.StringVar()}
        self.product_combobox = ttk.Combobox()
        self.product_tree_view = ttk.Treeview()
        self.observers = []
        self.setup_view()

    def setup_view(self):
        self.root.title("Wholesaler System - " + self.user.get_user_name())
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        product_label = ttk.Label(self.frame, text="Choose a product")
        product_label.grid(row=0, column=0, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.frame, text="Quantity")
        product_quantity_label.grid(row=0, column=2, padx=10, pady=10)

    def load_interactions(self):
        self.product_combobox = ttk.Combobox(self.frame, width=34, state="readonly",
                                             textvariable=self.input["product_name"])
        self.product_combobox.grid(row=0, column=1, pady=10)
        self.product_tree_view = ttk.Treeview(self.frame, column=("c1", "c2", "c3"),
                                              show='headings', height=21)
        self.product_tree_view.column("c1", width=190)
        self.product_tree_view.column("c2", width=85)
        self.product_tree_view.column("c3", width=85)
        self.product_tree_view.heading("c1", text="Product Name")
        self.product_tree_view.heading("c2", text="Quantity")
        self.product_tree_view.heading("c3", text="Price")
        self.product_tree_view.grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)
        product_quantity_entry = ttk.Entry(self.frame, width=18,
                                           textvariable=self.input["product_quantity"])
        product_quantity_entry.grid(row=0, column=3, padx=10, pady=10)
        add_product_button = ttk.Button(self.frame, width=20, text="Add to Basket",
                                        command=lambda: self.notify(1))
        add_product_button.grid(row=1, column=2, columnspan=3, padx=10)
        remove_product_button = ttk.Button(self.frame, width=20, text="Remove from Basket",
                                           command=lambda: self.notify(2))
        remove_product_button.grid(row=2, column=2, columnspan=3, padx=10)
        checkout_button = ttk.Button(self.frame, width=20, text="Checkout",
                                     command=lambda: self.notify(3))
        checkout_button.grid(row=3, column=2, columnspan=3, padx=10)
        log_out_button = ttk.Button(self.frame, width=20, text="Logout",
                                    command=lambda: self.notify(4))
        log_out_button.grid(row=5, column=2, columnspan=3, padx=10)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, command: int):
        for observer in self.observers:
            if observer[0] == command:
                observer[1]()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def get_input_value(self, dict_value: str) -> str:
        value = self.input[dict_value].get()
        return value

    def get_tree_view(self) -> ttk.Treeview:
        return self.product_tree_view

    def set_combobox(self, combobox_items: List[str]):
        self.product_combobox["values"] = combobox_items

    def insert_item(self, tree_view: ttk.Treeview, *args):
        tree_view.insert("", "end", text="Item", values=(args[0], args[1], args[2]))

    def remove_item(self, tree_view: ttk.Treeview):
        selected_item = tree_view.selection()[0]
        tree_view.delete(selected_item)

    def clear_tree_view(self, tree_view: ttk.Treeview):
        for item in tree_view.get_children():
            tree_view.delete(item)
