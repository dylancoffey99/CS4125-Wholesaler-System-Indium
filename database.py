# database.py
# Defines Database and ProductDB classes
# Author: Dylan Coffey - 18251382

import db_interfaces as db


class Database(db.IDatabase):
    def open_db(self, db_name, operation):
        pass

    def read_db(self, db_name):
        pass

    def write_db(self, db_name):
        pass


class ProductDB(Database, db.IProductDB):
    def add_product(self, product_id, product_name, product_quantity, product_price):
        pass

    def remove_product(self, product_id):
        pass

    def get_product(self, product_id):
        pass

    def get_product_id(self, product_name):
        pass

    def edit_product_name(self, product_id, product_name):
        pass

    def edit_product_quantity(self, product_id, product_quantity):
        pass

    def edit_product_price(self, product_id, product_price):
        pass
