"""
This module contains the CustomerView class. The module imports the tk package from the
tkinter package, the ttk module from the tkinter package, and the classes AbstractView,
AbstractSelectView, and AbstractUserView from the abstract_views module, all in the
systems views package.
"""
import tkinter as tk
from tkinter import ttk
from typing import List

from system.views.abstract_views import AbstractView, AbstractSelectView, AbstractUserView


class CustomerView(AbstractView, AbstractSelectView, AbstractUserView):
    """
    This class represents the customer view of the system and implements AbstractView,
    AbstractSelectView, and AbstractUserView. It contains a constructor, the setup/load
    methods for the root/widgets, and the implemented abstract methods.
    """

    def __init__(self, root, frame, user):
        """
        This constructor instantiates a customer view object.

        :param root: Tkinter window to hold the frame of the view.
        :param frame: Tkinter frame to hold the widgets of the view.
        :param user: Object of the logged in user.
        """
        self.root = root
        self.frame = frame
        self.user = user
        self.input = {"product_name": tk.StringVar(), "product_quantity": tk.StringVar()}
        self.update_widgets = [ttk.Label(), ttk.Combobox(), ttk.Treeview()]
        self.observers = []
        self.setup_view()

    def setup_view(self):
        self.root.title("Wholesaler System - " + self.user.get_user_name())
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        self.update_widgets[0] = ttk.Label(self.frame, text="Basket Subtotal = €0")
        self.update_widgets[0].grid(row=1, column=2, columnspan=3, padx=10, pady=10)
        product_label = ttk.Label(self.frame, text="Choose a product")
        product_label.grid(row=0, column=0, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.frame, text="Quantity")
        product_quantity_label.grid(row=0, column=2, padx=10, pady=10)

    def load_interactions(self):
        self.update_widgets[1] = ttk.Combobox(self.frame, width=34, state="readonly",
                                              textvariable=self.input["product_name"])
        self.update_widgets[1].grid(row=0, column=1, pady=10)
        self.update_widgets[2] = ttk.Treeview(self.frame, column=("c1", "c2", "c3"),
                                              show='headings', height=21)
        self.update_widgets[2].column("c1", width=190)
        self.update_widgets[2].column("c2", width=85)
        self.update_widgets[2].column("c3", width=85)
        self.update_widgets[2].heading("c1", text="Product Name")
        self.update_widgets[2].heading("c2", text="Quantity")
        self.update_widgets[2].heading("c3", text="Price")
        self.update_widgets[2].grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)
        self.update_widgets[2].bind("<Button-1>", lambda event:
                                    self.stop_tree_view_resize(self.update_widgets[2], event))
        product_quantity_entry = ttk.Entry(self.frame, width=18,
                                           textvariable=self.input["product_quantity"])
        product_quantity_entry.grid(row=0, column=3, padx=10, pady=10)
        add_product_button = ttk.Button(self.frame, width=20, text="Add to Basket",
                                        command=lambda: self.notify(1))
        add_product_button.grid(row=2, column=2, columnspan=3, padx=10)
        remove_product_button = ttk.Button(self.frame, width=20, text="Remove from Basket",
                                           command=lambda: self.notify(2))
        remove_product_button.grid(row=3, column=2, columnspan=3, padx=10)
        checkout_button = ttk.Button(self.frame, width=20, text="Checkout",
                                     command=lambda: self.notify(3))
        checkout_button.grid(row=4, column=2, columnspan=3, padx=10)
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
        return self.update_widgets[2]

    def set_combobox(self, combobox_items: List[str]):
        self.update_widgets[1]["values"] = combobox_items

    def insert_item(self, tree_view: ttk.Treeview, *args):
        tree_view.insert("", "end", text="Item", values=(args[0], args[1], args[2]))

    def edit_item(self, tree_view: ttk.Treeview, item, *args):
        tree_view.item(item, text="Item", values=(args[0], args[1], args[2]))

    def remove_item(self, tree_view: ttk.Treeview, item):
        tree_view.delete(item)

    def clear_tree_view(self, tree_view: ttk.Treeview):
        for item in tree_view.get_children():
            tree_view.delete(item)

    def stop_tree_view_resize(self, tree_view: ttk.Treeview, event):
        if tree_view.identify_region(event.x, event.y) == "separator":
            return "break"
        return "continue"

    def set_basket_subtotal_label(self, basket_subtotal: float):
        """
        This method sets the text of the basket subtotal label.

        :param basket_subtotal: Basket subtotal to be set to the label.
        """
        self.update_widgets[0].config(text="Basket Subtotal = €" + str(basket_subtotal))
