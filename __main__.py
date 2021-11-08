import tkinter as tk
from system.database.db_handler import UserDB
from system.database.db_handler import ProductDB


class MainApplication(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    user_db = UserDB("userDB")
    product_db = ProductDB("productDB")
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
