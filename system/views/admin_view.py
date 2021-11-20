import tkinter as tk
from tkinter import ttk


class AdminView:
    def __init__(self, root, controller):
        self.root = root
        self.root.geometry("1300x500")
        self.root.rowconfigure(0, weight=0)
        self.root.columnconfigure(0, weight=0)
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Frame labels
        label = ttk.Label(self.root, text="Choose a User")
        label.grid(row=0, column=0, padx=10, pady=10)
        discount_category_label = ttk.Label(self.root, text="Discount Category")
        discount_category_label.grid(row=0, column=2, padx=10, pady=10)
        product_name_label = ttk.Label(self.root, text="Product Name")
        product_name_label.grid(row=0, column=5, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.root, text="Quantity")
        product_quantity_label.grid(row=0, column=7, padx=10, pady=10)
        product_price_label = ttk.Label(self.root, text="Price")
        product_price_label.grid(row=0, column=9, padx=10, pady=10)

        # Frame combobox/entries
        user_combobox = ttk.Combobox(self.root, width=37, state="readonly",
                                     textvariable=self.controller.order_input["user_name"])
        user_combobox["values"] = self.controller.fill_users()
        user_combobox.grid(row=0, column=1, pady=10)
        discount_list = tk.StringVar()
        discount_category = ttk.Combobox(self.root, width=17, state="readonly",
                                         textvariable=discount_list)
        discount_category["values"] = ("Education", "Small Business", "Start-up Businesses")
        discount_category.grid(row=0, column=3, padx=10, pady=10)
        product_name_entry = ttk.Entry(self.root, width=42)
        product_name_entry.grid(row=0, column=6, padx=10, pady=10)
        product_quantity_entry = ttk.Entry(self.root, width=8)
        product_quantity_entry.grid(row=0, column=8, padx=10, pady=10)
        product_price_entry = ttk.Entry(self.root, width=8)
        product_price_entry.grid(row=0, column=10, padx=10, pady=10)

        # Frame separator
        separator = ttk.Separator(self.root, orient="vertical")
        separator.grid(row=0, rowspan=7, column=4, sticky="ns")
        separator_expand = ttk.Label(self.root, text="")  # To push separator to the bottom
        separator_expand.grid(row=6, column=7, columnspan=4)

        # Frame tree views
        order_tree_view = ttk.Treeview(self.root, column=("c1", "c2", "c3"),
                                       show="headings", height=21)
        order_tree_view.column("c1", width=140)
        order_tree_view.column("c2", width=140)
        order_tree_view.column("c3", width=80)
        order_tree_view.heading("c1", text="Product Name")
        order_tree_view.heading("c2", text="Date")
        order_tree_view.heading("c3", text="Subtotal")
        order_tree_view.grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)
        product_tree_view = ttk.Treeview(self.root, column=("c1", "c2", "c3"),
                                         show="headings", height=21)
        product_tree_view.column("c1", width=190)
        product_tree_view.column("c2", width=85)
        product_tree_view.column("c3", width=85)
        product_tree_view.heading("c1", text="Product Name")
        product_tree_view.heading("c2", text="Quantity")
        product_tree_view.heading("c3", text="Price")
        product_tree_view.grid(row=1, rowspan=5, column=5, columnspan=2, padx=10, pady=2)

        # Frame buttons
        view_order_button = ttk.Button(self.root, width=20, text="View Order", command=lambda:
                                       self.controller.view_order(order_tree_view))
        view_order_button.grid(row=1, column=2, columnspan=2, padx=10)
        add_discount_button = ttk.Button(self.root, width=20, text="Add Discount")
        add_discount_button.grid(row=2, column=2, columnspan=2, padx=10)
        add_product_button = ttk.Button(self.root, width=20, text="Add Product")
        add_product_button.grid(row=1, column=7, columnspan=4, padx=10)
        edit_product_button = ttk.Button(self.root, width=20, text="Edit Product")
        edit_product_button.grid(row=2, column=7, columnspan=4, padx=10)
        remove_product_button = ttk.Button(self.root, width=20, text="Remove Product")
        remove_product_button.grid(row=3, column=7, columnspan=4, padx=10)
        log_out_button = ttk.Button(self.root, width=20, text="Logout", command=lambda:
                                    self.controller.logout_user(self.root, self.frame))
        log_out_button.grid(row=5, column=7, columnspan=4, padx=10)
