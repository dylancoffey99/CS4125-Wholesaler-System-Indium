import tkinter as tk
from abc import ABC, abstractmethod


class AbstractAccessController(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login_view(self, root: tk.Tk, frame: tk.Frame):
        pass

    @abstractmethod
    def register_view(self, root: tk.Tk, frame: tk.Frame):
        pass

    @abstractmethod
    def login_user(self, root: tk.Tk, frame: tk.Frame):
        pass

    @abstractmethod
    def logout_user(self, root: tk.Tk, frame: tk.Frame):
        pass

    @abstractmethod
    def register_user(self, root: tk.Tk, frame: tk.Frame):
        pass
