import tkinter as tk
from tkinter import ttk
from typing import List
from system.views.abstract_views import AbstractView, AbstractUserView


class AdminView(AbstractView, AbstractUserView):
    def __init__(self, root, frame, user):
        self.root = root
        self.frame = frame
        self.user = user
        self.input = {"user_name": tk.StringVar(), "discount_category": tk.StringVar(),
                      "product_name": tk.StringVar(), "product_quantity": tk.StringVar(),
                      "product_price": tk.StringVar()}
        self.combo_boxes = [ttk.Combobox(), ttk.Combobox()]
        self.tree_views = [ttk.Treeview(), ttk.Treeview()]
        self.observers = []
        self.setup_view()

    def setup_view(self):
        self.root.geometry("1300x500")
        self.root.title("Wholesaler System - " + self.user.get_user_name())
        self.load_labels()
        self.load_separator()
        self.load_interactions()

    def load_labels(self):
        customer_label = ttk.Label(self.frame, text="Choose a Customer")
        customer_label.grid(row=0, column=0, padx=10, pady=10)
        discount_label = ttk.Label(self.frame, text="Discount Category")
        discount_label.grid(row=0, column=2, padx=10, pady=10)
        product_name_label = ttk.Label(self.frame, text="Product Name")
        product_name_label.grid(row=0, column=5, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.frame, text="Quantity")
        product_quantity_label.grid(row=0, column=7, padx=10, pady=10)
        product_price_label = ttk.Label(self.frame, text="Price")
        product_price_label.grid(row=0, column=9, padx=10, pady=10)

    def load_separator(self):
        separator = ttk.Separator(self.frame, orient="vertical")
        separator.grid(row=0, rowspan=7, column=4, sticky="ns")
        separator_expand = ttk.Label(self.frame, text="")  # To expand separator to the bottom
        separator_expand.grid(row=6, column=7, columnspan=4)

    def load_interactions(self):
        self.combo_boxes[0] = ttk.Combobox(self.frame, width=32, state="readonly",
                                           textvariable=self.input["user_name"])
        self.combo_boxes[0].grid(row=0, column=1, pady=10)
        self.combo_boxes[1] = ttk.Combobox(self.frame, width=17, state="readonly",
                                           textvariable=self.input["discount_category"])
        self.combo_boxes[1]["values"] = ("Education", "Small Business", "Start-up Business")
        self.combo_boxes[1].grid(row=0, column=3, padx=10, pady=10)
        self.tree_views[0] = ttk.Treeview(self.frame, column=("c1", "c2", "c3"),
                                          show="headings", height=21)
        self.tree_views[0].column("c1", width=140)
        self.tree_views[0].column("c2", width=140)
        self.tree_views[0].column("c3", width=80)
        self.tree_views[0].heading("c1", text="Product Name")
        self.tree_views[0].heading("c2", text="Date")
        self.tree_views[0].heading("c3", text="Subtotal")
        self.tree_views[0].grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)
        self.tree_views[0].bind("<Button-1>", lambda event:
                                self.stop_tree_view_resize(self.tree_views[0], event))
        self.tree_views[1] = ttk.Treeview(self.frame, column=("c1", "c2", "c3"),
                                          show="headings", height=21)
        self.tree_views[1].column("c1", width=190)
        self.tree_views[1].column("c2", width=85)
        self.tree_views[1].column("c3", width=85)
        self.tree_views[1].heading("c1", text="Product Name")
        self.tree_views[1].heading("c2", text="Quantity")
        self.tree_views[1].heading("c3", text="Price")
        self.tree_views[1].grid(row=1, rowspan=5, column=5, columnspan=2, padx=10, pady=2)
        self.tree_views[1].bind("<Button-1>", lambda event:
                                self.stop_tree_view_resize(self.tree_views[1], event))
        product_name_entry = ttk.Entry(self.frame, width=42,
                                       textvariable=self.input["product_name"])
        product_name_entry.grid(row=0, column=6, padx=10, pady=10, )
        product_quantity_entry = ttk.Entry(self.frame, width=8,
                                           textvariable=self.input["product_quantity"])
        product_quantity_entry.grid(row=0, column=8, padx=10, pady=10)
        product_price_entry = ttk.Entry(self.frame, width=8,
                                        textvariable=self.input["product_price"])
        product_price_entry.grid(row=0, column=10, padx=10, pady=10)
        view_order_button = ttk.Button(self.frame, width=20, text="View Order",
                                       command=lambda: self.notify(1))
        view_order_button.grid(row=1, column=2, columnspan=2, padx=10)
        add_discount_button = ttk.Button(self.frame, width=20, text="Add Discount",
                                         command=lambda: self.notify(2))
        add_discount_button.grid(row=2, column=2, columnspan=2, padx=10)
        add_product_button = ttk.Button(self.frame, width=20, text="Add Product",
                                        command=lambda: self.notify(3))
        add_product_button.grid(row=1, column=7, columnspan=4, padx=10)
        edit_product_button = ttk.Button(self.frame, width=20, text="Edit Product",
                                         command=lambda: self.notify(4))
        edit_product_button.grid(row=2, column=7, columnspan=4, padx=10)
        remove_product_button = ttk.Button(self.frame, width=20, text="Remove Product",
                                           command=lambda: self.notify(5))
        remove_product_button.grid(row=3, column=7, columnspan=4, padx=10)
        log_out_button = ttk.Button(self.frame, width=20, text="Logout",
                                    command=lambda: self.notify(6))
        log_out_button.grid(row=5, column=7, columnspan=4, padx=10)

    def attach(self, observer):
        self.observers.append(observer)

    def detach_all(self):
        for observer in self.observers:
            self.observers.remove(observer)

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

    def get_tree_view(self) -> List[ttk.Treeview]:
        return self.tree_views

    def set_combobox(self, combobox_items: List[str]):
        self.combo_boxes[0]["values"] = combobox_items

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
