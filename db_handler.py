# db_handler.py
# Defines ProductDB and UserDB classes implementing abstracts methods to manipulate their respective CSV files
# Author: Dylan Coffey - 18251382

import csv
import abstract_db_handler as db


class ProductDB(db.AbstractDBHandler):
    def __init__(self, db_name):
        self._db_name = db_name

    def open_db(self, operation):
        database = open(self._db_name + ".csv", operation, newline="")
        return database

    def read_db(self, operation):
        reader = csv.reader(self.open_db(operation), delimiter=",")
        return reader

    def write_db(self, operation):
        writer = csv.writer(self.open_db(operation), delimiter=",")
        return writer

    def add_row(self, product):
        writer = self.write_db("a")
        writer.writerow(product)

    def get_row(self, product_id):
        reader = self.read_db("r")
        for row in reader:
            if row[0] == product_id:
                return row

    def get_id(self, product_name):
        reader = self.read_db("r")
        for row in reader:
            if row[1] == product_name:
                return row[0]

    def remove_row(self, product_id):
        temp_rows = list()
        reader = self.read_db("r")
        for row in reader:
            temp_rows.append(row)
            if row[0] == product_id:
                temp_rows.remove(row)
        writer = self.write_db("w")
        writer.writerows(temp_rows)

    def edit_row(self, product_id, column, new_value):
        temp_rows = list()
        reader = self.read_db("r")
        for row in reader:
            if row[0] == product_id:
                row[column] = new_value
            temp_rows.append(row)
        writer = self.write_db("w")
        writer.writerows(temp_rows)


class UserDB(db.AbstractDBHandler):
    def __init__(self, db_name):
        self._db_name = db_name

    def open_db(self, operation):
        database = open(self._db_name + ".csv", operation, newline="")
        return database

    def read_db(self, operation):
        reader = csv.reader(self.open_db(operation), delimiter=",")
        return reader

    def write_db(self, operation):
        writer = csv.writer(self.open_db(operation), delimiter=",")
        return writer

    def add_row(self, user):
        writer = self.write_db("a")
        writer.writerow(user)

    def get_row(self, user_id):
        reader = self.read_db("r")
        for row in reader:
            if row[0] == user_id:
                return row

    def get_id(self, user_name):
        reader = self.read_db("r")
        for row in reader:
            if row[1] == user_name:
                return row[0]
