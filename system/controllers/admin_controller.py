from typing import List
from tkinter import ttk, messagebox as mb
from system.views import HomeView, AdminView
from system.database.db_handler import UserDB, OrderDB, ProductDB
from system.models.users.customer import Customer
from system.models.shopping.product import Product
from system.models.shopping.discount import DiscountCategory
from system.controllers.abstract_controllers import AbstractController, AbstractObserverController


class AdminController(AbstractController, AbstractObserverController):
    def __init__(self, access_controller):
        self.access_controller = access_controller
        self.user_db = UserDB("system/database/csv/userDB")
        self.order_db = OrderDB("system/database/csv/orderDB")
        self.product_db = ProductDB("system/database/csv/productDB")
        self.view = AdminView(self.access_controller.root, self.access_controller.frame,
                              self.access_controller.user)
        self.view.set_combobox(self.fill_users())
        self.tree_views = self.view.get_tree_view()
        self.fill_products()
        self.attach_observers()
        self.customer = None

    def fill_users(self) -> List[str]:
        users = self.user_db.get_all_users()
        user_names = []
        for user, _ in enumerate(users):
            if users[user].get_is_admin() == 0:
                user_names.append(users[user].get_user_name())
        return user_names

    def fill_products(self):
        products = self.product_db.get_all_products()
        for product in products:
            product_name = product.get_product_name()
            quantity = product.get_product_quantity()
            price = product.get_product_price()
            self.view.insert_item(self.tree_views[1], product_name, quantity, price)

    def view_order(self):
        user_name = self.view.get_input_value("user_name")
        orders = self.order_db.get_customer_orders(user_name)
        if not orders:
            mb.showwarning("Error", "This user does not have any orders!")
        else:
            self.view.clear_tree_view(self.tree_views[0])
            for order in orders:
                product_name = order[1]
                date_time = order[2]
                subtotal = order[3]
                self.view.insert_item(self.tree_views[0], product_name, date_time, subtotal)

    def add_discount(self):
        user_name = self.view.get_input_value("user_name")
        discount_category = self.view.get_input_value("discount_category")
        if user_name == "":
            mb.showwarning("Error", "Please select a user!")
        elif discount_category == "":
            mb.showwarning("Error", "Please select a discount category!")
        else:
            if self.customer is None:
                user = self.user_db.get_user(user_name)
                self.customer = Customer(user.get_user_name(), user.get_password(),
                                         user.get_is_admin(), user.get_country_id())
            if user_name != self.customer.get_user_name():
                self.customer = None
            elif isinstance(self.customer.get_discount_category(), DiscountCategory):
                mb.showwarning("Error", "Customer already has a discount category!")
            else:
                discount = self.check_discount(discount_category)
                discount_percentage = discount.get_discount_percentage()
                self.customer.set_discount_category(discount)
                self.update_orders(self.tree_views[0], discount_percentage)
                self.order_db.update_order_subtotals(user_name, discount_percentage)

    def add_product(self):
        product_name = self.view.get_input_value("product_name")
        quantity = self.view.get_input_value("product_quantity")
        price = self.view.get_input_value("product_price")
        if product_name == "" or quantity == "" or price == "":
            mb.showwarning("Error", "Please enter all fields!")
        else:
            if self.product_db.product_exists(product_name):
                mb.showwarning("Error", "That product name already exists!")
            else:
                if not quantity.isdigit():
                    mb.showwarning("Error", "The quantity entered is not a valid number!")
                elif not price.isdigit():
                    mb.showwarning("Error", "The price entered is not a valid number!")
                else:
                    product = Product(product_name, int(quantity), float(price))
                    self.product_db.add_product(product)
                    self.view.insert_item(self.tree_views[1], product_name, quantity, float(price))

    def edit_product(self, tree_view: ttk.Treeview):
        product_name = self.input["product_name"].get()
        quantity = self.input["product_quantity"].get()
        product = self.product_db.get_product(product_name)
        price = float(quantity) * product.get_product_price()
        self.product_db.add_product(product)
        self.product_db.get_product_price(price)
        self.insert_data(tree_view, product_name, quantity, price)

    def remove_product(self, tree_view: ttk.Treeview):
        pass

    def logout_user(self):
        self.view.clear_frame()
        self.view = HomeView(self.access_controller.root, self.access_controller.frame,
                             self.access_controller.observers)

    def attach_observers(self):
        self.view.attach((1, self.view_order))
        self.view.attach((2, self.add_discount))
        self.view.attach((3, self.add_product))
        self.view.attach((4, self.edit_product))
        self.view.attach((5, self.remove_product))
        self.view.attach((6, self.logout_user))

    @staticmethod
    def check_discount(discount_name):
        if discount_name == "Education":
            discount = DiscountCategory(0, "Education", 0.10)
        elif discount_name == "Small Business":
            discount = DiscountCategory(0, "Small Business", 0.15)
        else:
            discount = DiscountCategory(0, "Start-up Business", 0.20)
        return discount

    @staticmethod
    def update_orders(tree_view: ttk.Treeview, discount_percentage: float):
        tree_list = list(tree_view.get_children(""))
        for item in tree_list:
            product_name = tree_view.item(item, "values")[0]
            date_time = tree_view.item(item, "values")[1]
            subtotal = float(tree_view.item(item, "values")[2])
            discount = subtotal * discount_percentage
            subtotal -= discount
            tree_view.item(item, text="Item", values=(product_name, date_time, subtotal))
