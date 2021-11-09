import tkinter as tk
from tkinter import ttk


class CustomerView:
    def __init__(self, root, controller):
        self.root = root
        self.root.rowconfigure(0, weight=0)
        self.root.columnconfigure(0, weight=0)
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Frame labels
        product_label = ttk.Label(self.root, text="Choose a product")
        product_label.grid(row=0, column=0, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.root, text="Quantity")
        product_quantity_label.grid(row=0, column=2, padx=10, pady=10)

        # Frame combobox/entries
        product_list = tk.StringVar()
        product_combobox = ttk.Combobox(self.root, width=34, state="readonly",
                                        textvariable=product_list)
        product_combobox["values"] = ("Laptop", "Monitors", "Mouse", "Keyboard")
        product_combobox.grid(row=0, column=1, pady=10)
        product_quantity_entry = ttk.Entry(self.root, width=18)
        product_quantity_entry.grid(row=0, column=3, padx=10, pady=10)

        # Frame tree views
        product_tree_view = ttk.Treeview(self.root, column=("c1", "c2", "c3"),
                                         show='headings', height=21)
        product_tree_view.column("c1", width=190)
        product_tree_view.column("c2", width=85)
        product_tree_view.column("c3", width=85)
        product_tree_view.heading("c1", text="Product Name")
        product_tree_view.heading("c2", text="Quantity")
        product_tree_view.heading("c3", text="Price")
        product_tree_view.grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)

        # Frame buttons
        add_product_button = ttk.Button(self.root, width=20, text="Add to Basket")
        add_product_button.grid(row=1, column=2, columnspan=3, padx=10)
        remove_product_button = ttk.Button(self.root, width=20, text="Remove from Basket")
        remove_product_button.grid(row=2, column=2, columnspan=3, padx=10)
        checkout_button = ttk.Button(self.root, width=20, text="Checkout")
        checkout_button.grid(row=3, column=2, columnspan=3, padx=10)
        log_out_button = ttk.Button(self.root, width=20, text="Logout")
        log_out_button.grid(row=5, column=2, columnspan=3, padx=10)
