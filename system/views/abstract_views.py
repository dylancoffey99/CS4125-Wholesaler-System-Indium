"""
This module contains the abstract classes AbstractView, AbstractSelectView, and
AbstractUserView. The module imports ABC (Abstract Base Class), abstractmethod
from the abc module, the module ttk from the tkinter package, and the type List
from the typing module.
"""
from abc import ABC, abstractmethod
from tkinter import ttk
from typing import List


class AbstractView(ABC):
    """
    This abstract class represents an interface view, containing the abstract
    methods to be implemented in view classes.
    """

    @abstractmethod
    def setup_view(self):
        """
        This method configs the views root and calls the load methods for the
        views Tkinter widgets.
        """

    @abstractmethod
    def load_labels(self):
        """This method loads the Tkinter labels of the view."""

    @abstractmethod
    def load_interactions(self):
        """
        This method loads the Tkinter interaction widgets of the view,
        such as the buttons, entries, tree views, and combo boxes.
        """

    @abstractmethod
    def attach(self, observer):
        """
        This method appends an observer of the view to a list.

        :param observer: Observer to be appended to a list.
        """

    @abstractmethod
    def notify(self, command: int):
        """
        This method checks a passed command and then runs the observer
        method that has the same command assigned to it.

        :param command: Command of a certain observer method.
        """

    @abstractmethod
    def clear_frame(self):
        """This method clears the frame of the view and all its widgets."""


class AbstractSelectView(ABC):
    """
    This abstract class represents an interface of a select view, containing the
    abstract methods to be implemented in select view classes.
    """

    @abstractmethod
    def set_combobox(self, combobox_items: List[str]):
        """
        This method sets the values of the views combo box.

        :param combobox_items: List to be set to the views combo box.
        """


class AbstractUserView(ABC):
    """
    This abstract class represents an interface of a user view, containing the
    abstract methods to be implemented in user view classes.
    """

    @abstractmethod
    def get_input_value(self, dict_value: str) -> str:
        """
        This method gets the input of a value in the views input dictionary.

        :param dict_value: Value of the views input dictionary.
        """

    @abstractmethod
    def get_tree_view(self) -> ttk.Treeview:
        """
        This method gets the views tree view.

        :returns: Tree view of the view.
        """

    @abstractmethod
    def insert_item(self, tree_view: ttk.Treeview, *args):
        """
        This method inserts an item into a tree view.

        :param tree_view: Tree view to insert an item into.
        :param args: Values of the items columns (3 arguments).
        """

    @abstractmethod
    def edit_item(self, tree_view: ttk.Treeview, item, *args):
        """
        This method edits an item of a tree view.

        :param tree_view: Tree view to edit an item from.
        :param item: Item to be edited.
        :param args: Values of the items columns (3 arguments).
        """

    @abstractmethod
    def remove_item(self, tree_view: ttk.Treeview, item):
        """
        This method removes an item from a tree view.

        :param tree_view: Tree view to remove an item from.
        :param item: Item to be removed.
        """

    @abstractmethod
    def clear_tree_view(self, tree_view: ttk.Treeview):
        """
        This method clears all items of a tree view.

        :param tree_view: Tree view to be cleared.
        """

    @abstractmethod
    def stop_tree_view_resize(self, tree_view: ttk.Treeview, event):
        """
        This method stops the resizing of the columns of a tree view.

        :param tree_view: Tree view to be stopped.
        :param event: Event to be stopped.
        """
