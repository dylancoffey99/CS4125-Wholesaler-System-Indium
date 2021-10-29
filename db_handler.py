# db_handler.py
# Defines ProductDB and UserDB classes implementing
# abstract methods to manipulate their respective CSV files
# Author: Dylan Coffey - 18251382

import csv
import abstract_db_handler as db


class ProductDB(db.AbstractDBHandler):
    def __init__(self, db_name):
        self._db_name = db_name
        self._db = None

    def open_db(self, operation):
        self._db = open(self._db_name + ".csv", operation, newline="", encoding="utf-8")

    def read_db(self, operation):
        self.open_db(operation)
        reader = csv.reader(self._db, delimiter=",")
        return reader

    def write_db(self, operation):
        self.open_db(operation)
        writer = csv.writer(self._db, delimiter=",")
        return writer

    def add_row(self, row):
        writer = self.write_db("a")
        writer.writerow(row)
        self._db.close()

    def get_row(self, _id):
        reader = self.read_db("r")
        for row in reader:
            if row[0] == _id:
                self._db.close()
                return row
        return "Error: that ID doesn't exist"

    def get_all_rows(self):
        temp_rows = []
        reader = self.read_db("r")
        next(reader)
        for row in reader:
            temp_rows.append(row)
        self._db.close()
        return temp_rows

    def get_id(self, name):
        reader = self.read_db("r")
        for row in reader:
            if row[1] == name:
                self._db.close()
                return row[0]
        return "Error: that name doesn't exist"

    def remove_row(self, _id):
        temp_rows = []
        reader = self.read_db("r")
        for row in reader:
            temp_rows.append(row)
            if row[0] == _id:
                temp_rows.remove(row)
        writer = self.write_db("w")
        writer.writerows(temp_rows)
        self._db.close()

    def edit_row(self, _id, column, new_value):
        temp_rows = []
        reader = self.read_db("r")
        for row in reader:
            if row[0] == _id:
                row[column] = new_value
            temp_rows.append(row)
        writer = self.write_db("w")
        writer.writerows(temp_rows)
        self._db.close()


class UserDB(db.AbstractDBHandler):
    def __init__(self, db_name):
        self._db_name = db_name
        self._db = None

    def open_db(self, operation):
        self._db = open(self._db_name + ".csv", operation, newline="", encoding="utf-8")

    def read_db(self, operation):
        self.open_db(operation)
        reader = csv.reader(self._db, delimiter=",")
        return reader

    def write_db(self, operation):
        self.open_db(operation)
        writer = csv.writer(self._db, delimiter=",")
        return writer

    def add_row(self, row):
        writer = self.write_db("a")
        writer.writerow(row)
        self._db.close()

    def get_row(self, _id):
        reader = self.read_db("r")
        for row in reader:
            if row[0] == _id:
                self._db.close()
                return row
        return "Error: that ID doesn't exist"

    def get_all_rows(self):
        temp_rows = []
        reader = self.read_db("r")
        next(reader)
        for row in reader:
            temp_rows.append(row)
        self._db.close()
        return temp_rows

    def get_id(self, name):
        reader = self.read_db("r")
        for row in reader:
            if row[1] == name:
                self._db.close()
                return row[0]
        return "Error: that name doesn't exist"
