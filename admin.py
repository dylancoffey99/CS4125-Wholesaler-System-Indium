# admin.py
############################
# Implemented class for the Admin
#############################
# Author: Wasim - 17193559
# Last edited on 02/11
# Modification time 07:00 PM

from user import User
from stock_management import Product
from db_handler import ProductDB


class Admin:
    #def __init__():
    def __init__(self, product_id: int, product_name: str):
        self._product_id = product_id
        self._product_name = product_name

    # return void
    def add_product(self, product: Product):
        # We need to write those products to the CSV file

    # return void
    def remove_product(self):
        # We need to remove those products to the CSV file

    # return list
    def get_orders(self):
        # print the products order

