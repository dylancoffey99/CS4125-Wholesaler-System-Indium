from abc import ABC, abstractmethod
from tkinter import ttk
from typing import List


class AbstractView(ABC):
    @abstractmethod
    def setup_view(self):
        pass

    @abstractmethod
    def load_labels(self):
        pass

    @abstractmethod
    def load_interactions(self):
        pass

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def notify(self, command: int):
        pass

    @abstractmethod
    def clear_frame(self):
        pass


class AbstractUserView(ABC):
    @abstractmethod
    def get_input_value(self, dict_value: str) -> str:
        pass

    @abstractmethod
    def get_tree_view(self):
        pass

    @abstractmethod
    def set_combobox(self, combobox_items: List[str]):
        pass

    @abstractmethod
    def insert_item(self, tree_view: ttk.Treeview, *args):
        pass

    @abstractmethod
    def edit_item(self, tree_view: ttk.Treeview, item, *args):
        pass

    @abstractmethod
    def remove_item(self, tree_view: ttk.Treeview, item):
        pass

    @abstractmethod
    def clear_tree_view(self, tree_view: ttk.Treeview):
        pass

    @abstractmethod
    def stop_tree_view_resize(self, tree_view: ttk.Treeview, event):
        pass
