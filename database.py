# database.py
# Defines Database and ProductDB classes
# Author: Dylan Coffey - 18251382

import csv
import db_interfaces as db


class Database(db.IDatabase):
    def open_db(self, db_name, operation):
        database = open(db_name + ".csv", operation, newline="")
        return database

    def read_db(self, db_name, operation):
        reader = csv.reader(self.open_db(db_name, operation), delimiter=",")
        return reader

    def write_db(self, db_name, operation):
        writer = csv.writer(self.open_db(db_name, operation), delimiter=",")
        return writer


class ProductDB(Database, db.IProductDB):
    def __init__(self):
        self.db_name = "productDB"

    def add_product(self, product_id, product_name, product_quantity, product_price):
        product = [product_id, product_name, product_quantity, product_price]
        writer = self.write_db(self.db_name, "a")
        writer.writerow(product)

    def remove_product(self, product_id):
        temp_rows = list()
        reader = self.read_db(self.db_name, "r")
        for row in reader:
            temp_rows.append(row)
            if row[0] == product_id:
                temp_rows.remove(row)
        writer = self.write_db(self.db_name, "w")
        writer.writerows(temp_rows)

    def get_product(self, product_id):
        reader = self.read_db(self.db_name, "r")
        for row in reader:
            if row[0] == product_id:
                return row

    def get_product_id(self, product_name):
        reader = self.read_db(self.db_name, "r")
        for row in reader:
            if row[1] == product_name:
                return row[0]

    def edit_product(self, product_id, column, new_value):
        temp_rows = list()
        reader = self.read_db(self.db_name, "r")
        for row in reader:
            if row[0] == product_id:
                row[column] = new_value
            temp_rows.append(row)
        writer = self.write_db(self.db_name, "w")
        writer.writerows(temp_rows)


# Example use of methods
pDB = ProductDB()
pDB.add_product("5", "product5", "150", "10")
pDB.remove_product("1")
print(pDB.get_product("3"))
print(pDB.get_product_id("product3"))
pDB.edit_product("4", 1, "editedProduct")
