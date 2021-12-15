"""
This module contains the CustomerController class. The module imports the datetime class
from the datetime module, the messagebox module from the tkinter package, the type List
from the typing module, and the AbstractUserController and AbstractObserverController
classes from the systems controllers package. It also imports the AbstractObserver and
Basket classes from the systems shopping package, the Order class from the systems
payment package, and the views HomeView and CustomerView from the systems views package.
"""
from datetime import datetime
from tkinter import messagebox as mb
from typing import List

from system.controllers import AbstractUserController, AbstractObserverController
from system.models.payment import Order
from system.models.shopping import AbstractObserver
from system.models.shopping.basket import Basket
from system.views import HomeView, CustomerView


class CustomerController(AbstractUserController, AbstractObserverController, AbstractObserver):
    """
    This class represents an customer controller and implements
    AbstractUserController, AbstractObserverController, and AbstractObserver.
    It contains a constructor, the methods for controlling CustomerView, and
    the implemented abstract methods.
    """

    def __init__(self, access_controller):
        """
        This constructor instantiates a customer controller object.

        :param access_controller: Object of AccessController"""
        self.access_controller = access_controller
        self.customer = self.access_controller.user
        self.view = CustomerView(self.access_controller.root, self.access_controller.frame,
                                 self.customer)
        self.view.set_combobox(self.fill_products())
        self.tree_view = self.view.get_tree_view()
        self.basket = Basket([], 0)
        self.attach_observers()

    def fill_products(self) -> List[str]:
        """
        This method gets a list of all product objects from the product
        database so it can be filled into the product combobox.

        :returns: A list of customer objects.
        """
        products = self.customer.get_all_products()
        product_names = []
        for product in products:
            product_names.append(product.get_product_name())
        return product_names

    def add_product(self):
        """
        This method adds a product to the basket items and the
        CustomerView product tree view.
        """
        product_name = self.view.get_input_value("product_name")
        quantity = self.view.get_input_value("product_quantity")
        if product_name == "" or quantity == "":
            mb.showwarning("Error", "Please enter all fields!")
        elif not quantity.isdigit() or quantity == str(0):
            mb.showwarning("Error", "The quantity entered is not a valid number!")
        else:
            product = self.customer.get_product(product_name)
            if self.basket.item_exists(product_name):
                mb.showwarning("Error", "That product is already in the basket!")
            elif product.get_product_quantity() == 0:
                mb.showwarning("Error", "Product out of stock!")
            elif int(quantity) > product.get_product_quantity():
                mb.showwarning("Error", "The quantity entered is too high,"
                                        " not enough left in stock!")
            else:
                price = product.calc_price(quantity)
                self.basket.add_item(product)
                self.basket.add_basket_subtotal(price)
                self.view.insert_item(self.tree_view, product_name, int(quantity), price)

    def remove_product(self):
        """
        This method removes a product from the basket items and the
        CustomerView product tree view.
        """
        selected_item = self.tree_view.focus()
        if len(self.tree_view.get_children("")) == 0:
            mb.showwarning("Error", "The basket is empty, there aren't any products to remove!")
        elif not selected_item:
            mb.showwarning("Error", "Please select a product from the basket!")
        else:
            item_dict = self.tree_view.item(selected_item)
            values = list(item_dict.values())
            product_name = values[2][0]
            quantity = values[2][1]
            products = self.basket.get_basket_items()
            for product in products:
                if product.get_product_name() == product_name:
                    price = product.calc_price(quantity)
                    self.basket.remove_item(product)
                    self.basket.sub_basket_subtotal(price)
                    self.view.remove_item(self.tree_view, selected_item)

    def checkout(self):
        """
        This method checks out the customers order by obtaining the basket items,
        subtracting the quantity of the products added from the the product database,
        and creating an order using the product names of the basket items.
        """
        if len(self.tree_view.get_children("")) == 0:
            mb.showwarning("Error", "The basket is empty, please add some products to the basket!")
        else:
            tree_list = list(self.tree_view.get_children(""))
            products = self.basket.get_basket_items()
            product_names = []
            for row in tree_list:
                product_name = self.tree_view.item(row, "values")[0]
                quantity = int(self.tree_view.item(row, "values")[1])
                for product in products:
                    if product_name == product.get_product_name():
                        self.customer.sub_product_quantity(product_name, quantity)
                        product_names.append(product.get_product_name())
            self.create_order(product_names)
            self.basket.clear_items()
            self.view.clear_tree_view(self.tree_view)

    def create_order(self, product_names: List[str]):
        """
        This method creates an order by calculating the subtotals needed from the
        basket. It then creates an order object which is added to the order database.
        """
        subtotals = self.basket.calc_subtotals(self.customer)
        order = Order(self.customer.get_user_name(), product_names, datetime.now(), subtotals[4])
        self.customer.add_order(order)
        mb.showinfo("Success", "Checkout successful, your order has been created!\n"
                               "\nBasket Subtotal = €" + str(f"{subtotals[0]:.1f}") +
                    "\nVAT Cost = €" + str(f"{subtotals[1]:.1f}") +
                    "\nShipping Cost = €" + str(subtotals[2]) +
                    "\nDiscount = €" + str(f"{subtotals[3]:.1f}") +
                    "\n=================\nTotal Cost = €" + str(f"{subtotals[4]:.1f}"))

    def logout_user(self):
        self.view.clear_frame()
        self.view = HomeView(self.access_controller.root, self.access_controller.frame,
                             self.access_controller.observers)
        self.access_controller.user = None

    def attach_observers(self):
        self.view.attach((1, self.add_product))
        self.view.attach((2, self.remove_product))
        self.view.attach((3, self.checkout))
        self.view.attach((4, self.logout_user))
        self.basket.attach(self)

    def update(self, subject):
        self.view.set_basket_subtotal_label(subject.get_basket_subtotal())
