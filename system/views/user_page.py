import tkinter as tk
from tkinter import ttk


class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Choose the Item")
        label.grid(row=5, column=0, padx=10, pady=10)

        product_list = tk.StringVar()
        product_sold = ttk.Combobox(self, width=27, textvariable=product_list)
        product_sold['values'] = (' Laptop',
                                  ' Monitors',
                                  ' Mouse',
                                  ' Keyboard',
                                  )

        product_sold.grid(row=5, column=1)

        quantity_label = ttk.Label(self, text="Quantity")
        quantity_label.grid(row=5, column=4, padx=10, pady=10)
        quantity_entry = ttk.Entry(self)
        quantity_entry.grid(row=5, column=5, padx=10, pady=10)

        add_to_bag_button = ttk.Button(self, text="Add to Bag",
                                       command=lambda: controller.show_frame(UserPage))

        add_to_bag_button.grid(row=3, column=1, padx=10, pady=10)
        add_to_bag_button = ttk.Button(self, text="Checkout",
                                       command=lambda: controller.show_frame(UserPage))

        add_to_bag_button.grid(row=3, column=1, padx=10, pady=10)
