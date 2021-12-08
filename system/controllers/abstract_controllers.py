from tkinter import ttk
from typing import List
from abc import ABC, abstractmethod


class AbstractAccessController(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login_view(self):
        pass

    @abstractmethod
    def register_view(self):
        pass

    @abstractmethod
    def login_user(self):
        pass

    @abstractmethod
    def register_user(self):
        pass


class AbstractCustomerController(ABC):
    @abstractmethod
    def fill_products(self) -> List[str]:
        pass

    @abstractmethod
    def add_product(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def remove_product(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def checkout(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def create_order(self, customer_name, product_names):
        pass

    @abstractmethod
    def logout_user(self):
        pass


class AbstractAdminController(ABC):
    @abstractmethod
    def fill_users(self) -> List[str]:
        pass

    @abstractmethod
    def fill_products(self) -> List[str]:
        pass

    @abstractmethod
    def view_order(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def add_discount(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def add_product(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def edit_product(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def remove_product(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def logout_user(self):
        pass
