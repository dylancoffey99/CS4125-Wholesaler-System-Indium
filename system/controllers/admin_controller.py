"""
This module contains the AdminController class. The module imports the messagebox module
from the tkinter package, the type List from the typing module, the AbstractUserController
and AbstractObserverController classes from the systems controllers package, the Product
class from the systems shopping package, and the views HomeView and AdminView from the
systems views package.
"""
from tkinter import messagebox as mb
from typing import List

from system.controllers import AbstractUserController, AbstractObserverController
from system.models.shopping import Product
from system.views import HomeView, AdminView


class AdminController(AbstractUserController, AbstractObserverController):
    """
    This class represents an admin controller and implements
    AbstractUserController and AbstractObserverController. It contains
    a constructor, the methods for controlling AdminView, and the
    implemented abstract methods.
    """

    def __init__(self, access_controller):
        """
        This constructor instantiates an admin controller object.

        :param access_controller: Object of AccessController"""
        self.access_controller = access_controller
        self.admin = self.access_controller.user
        self.view = AdminView(self.access_controller.root, self.access_controller.frame,
                              self.admin)
        self.view.set_combobox(self.fill_customers())
        self.tree_views = self.view.get_tree_view()
        self.fill_products()
        self.attach_observers()

    def fill_customers(self) -> List[str]:
        """
        This method gets a list of all customer usernames from the user
        database so it can be filled into the customer combobox.

        :returns: A list of customer usernames.
        """
        customers = self.admin.get_all_customers()
        user_names = []
        for customer in customers:
            user_names.append(customer.get_user_name())
        return user_names

    def fill_products(self):
        """
        This method gets all the product objects from the product database
        so they can be inserted into the AdminView product tree view.
        """
        products = self.admin.get_all_products()
        for product in products:
            product_name = product.get_product_name()
            quantity = product.get_product_quantity()
            price = product.get_product_price()
            self.view.insert_item(self.tree_views[1], product_name, quantity, price)

    def view_order(self):
        """
        This method displays the orders of a selected customer into the
        AdminView order tree view.
        """
        user_name = self.view.get_input_value("user_name")
        if user_name == "":
            mb.showwarning("Error", "Please select a customer!")
        elif not self.admin.orders_exist(user_name):
            mb.showwarning("Error", "This customer does not have any orders!")
        else:
            orders = self.admin.get_customer_orders(user_name)
            self.view.clear_tree_view(self.tree_views[0])
            for order in orders:
                product_name = order[1]
                date_time = order[2]
                subtotal = order[3]
                self.view.insert_item(self.tree_views[0], product_name, date_time, subtotal)

    def add_discount(self):
        """
        This method adds a discount to the orders of a selected customer
        by updating the customers order subtotals in the order database,
        and in the AdminView order tree view."""
        user_name = self.view.get_input_value("user_name")
        discount_category = self.view.get_input_value("discount_category")
        if user_name == "":
            mb.showwarning("Error", "Please select a customer!")
        elif discount_category == "":
            mb.showwarning("Error", "Please select a discount category!")
        else:
            customer = self.admin.get_customer(user_name)
            if not self.admin.orders_exist(user_name):
                mb.showwarning("Error", "This customer does not have any orders!")
            elif customer.get_discount_id() != -1:
                mb.showwarning("Error", "This customer already has a discount category!")
            else:
                discount = customer.check_discount_category()
                discount_id = discount.get_discount_id()
                discount_percentage = discount.get_discount_percentage()
                customer.set_discount_id(discount_id)
                self.view_order()
                self.admin.set_customer_discount(user_name, discount_id)
                self.admin.update_order_subtotals(user_name, discount_percentage)
                self.update_orders(discount_percentage)

    def update_orders(self, discount_percentage: float):
        """
        This method updates and gives a discount to a customers order
        subtotals in the AdminView order tree view.

        :param discount_percentage: Discount percentage to be used.
        """
        tree_list = list(self.tree_views[0].get_children(""))
        for item in tree_list:
            product_name = self.tree_views[0].item(item, "values")[0]
            date_time = self.tree_views[0].item(item, "values")[1]
            if product_name == "================" or date_time == "":
                continue
            subtotal = float(self.tree_views[0].item(item, "values")[2])
            discount = subtotal * discount_percentage
            subtotal -= discount
            self.view.edit_item(self.tree_views[0], item, product_name, date_time, subtotal)

    def add_product(self):
        """
        This method adds a product to the product database and the
        AdminView product tree view.
        """
        product_name = self.view.get_input_value("product_name")
        quantity = self.view.get_input_value("product_quantity")
        price = self.view.get_input_value("product_price")
        if product_name == "" or quantity == "" or price == "":
            mb.showwarning("Error", "Please enter all the fields!")
        elif self.admin.product_exists(product_name):
            mb.showwarning("Error", "That product name already exists!")
        else:
            if self.product_check(product_name, quantity, price):
                product = Product(product_name, int(quantity), float(price))
                self.admin.add_product(product)
                self.view.insert_item(self.tree_views[1], product_name, quantity, float(price))

    def edit_product(self):
        """
        This method edits a product in the product database and the
        AdminView product tree view.
        """
        values = [self.view.get_input_value("product_name"),
                  self.view.get_input_value("product_quantity"),
                  self.view.get_input_value("product_price")]
        selected_item = self.tree_views[1].focus()
        if len(self.tree_views[1].get_children("")) == 0:
            mb.showwarning("Error", "There aren't any products to edit!")
        elif not selected_item:
            mb.showwarning("Error", "Please select a product to edit!")
        elif values[0] == "" and values[1] == "" and values[2] == "":
            mb.showwarning("Error", "Please enter a field to edit!")
        else:
            product_name = self.tree_views[1].item(selected_item, "values")[0]
            if values[0] != "" and values[0] != product_name and \
                    self.admin.product_exists(values[0]):
                mb.showwarning("Error", "That product name already exists!")
            else:
                for i, value in enumerate(values):
                    if value == "":
                        values[i] = self.tree_views[1].item(selected_item, "values")[i]
                if self.product_check(values[0], values[1], values[2]):
                    product = self.admin.get_product(product_name)
                    for i, value in enumerate(values):
                        self.admin.edit_product(product, i, value)
                    self.view.edit_item(self.tree_views[1], selected_item, values[0], values[1],
                                        str(float(values[2])))

    def remove_product(self):
        """
        This method removes a product from the product database and the
        AdminView product tree view.
        """
        selected_item = self.tree_views[1].focus()
        if len(self.tree_views[1].get_children("")) == 0:
            mb.showwarning("Error", "There aren't any products to remove!")
        elif not selected_item:
            mb.showwarning("Error", "Please select a product to remove!")
        else:
            item_dict = self.tree_views[1].item(selected_item)
            values = list(item_dict.values())
            product_name = values[2][0]
            product = self.admin.get_product(product_name)
            self.admin.remove_product(product)
            self.view.remove_item(self.tree_views[1], selected_item)

    def logout_user(self):
        self.view.clear_frame()
        self.view = HomeView(self.access_controller.root, self.access_controller.frame,
                             self.access_controller.observers)
        self.access_controller.user = None

    def attach_observers(self):
        self.view.attach((1, self.view_order))
        self.view.attach((2, self.add_discount))
        self.view.attach((3, self.add_product))
        self.view.attach((4, self.edit_product))
        self.view.attach((5, self.remove_product))
        self.view.attach((6, self.logout_user))

    @staticmethod
    def product_check(product_name: str, quantity: str, price: str):
        """
        This method checks that the values entered by the admin are the
        correct types, and don't exceed certain lengths.
        """
        if not quantity.isdigit():
            mb.showwarning("Error", "The quantity entered is not a valid number!")
        try:
            float(price)
            price.isdigit()
        except ValueError:
            mb.showwarning("Error", "The price entered is not a valid number!")
        else:
            if len(product_name) > 30:
                mb.showwarning("Error", "The product name has to be less than 30 characters!")
            elif len(quantity) > 7:
                mb.showwarning("Error", "The quantity has to be less than 7 digits!")
            elif float(price) >= 10000 or len(price) > 7:
                mb.showwarning("Error", "The price has to be less than 10,000 and 7 digits!")
            else:
                return True
        return False
