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
        database = self.open_db(operation)
        reader = csv.reader(database, delimiter=",")
        return [reader, database]

    def write_db(self, operation):
        database = self.open_db(operation)
        writer = csv.writer(database, delimiter=",")
        return [writer, database]

    def add_row(self, product):
        writer = self.write_db("a")
        writer[0].writerow(product)
        writer[1].close()

    def get_row(self, product_id):
        reader = self.read_db("r")
        for row in reader[0]:
            if row[0] == product_id:
                reader[1].close()
                return row

    def get_all_rows(self):
        temp_rows = []
        reader = self.read_db("r")
        next(reader[0])
        for row in reader[0]:
            temp_rows.append(row)
        reader[1].close()
        return temp_rows

    def get_id(self, product_name):
        reader = self.read_db("r")
        for row in reader[0]:
            if row[1] == product_name:
                reader[1].close()
                return row[0]

    def remove_row(self, product_id):
        temp_rows = []
        reader = self.read_db("r")
        for row in reader[0]:
            temp_rows.append(row)
            if row[0] == product_id:
                temp_rows.remove(row)
        writer = self.write_db("w")
        writer[0].writerows(temp_rows)
        reader[1].close()
        writer[1].close()

    def edit_row(self, product_id, column, new_value):
        temp_rows = []
        reader = self.read_db("r")
        for row in reader[0]:
            if row[0] == product_id:
                row[column] = new_value
            temp_rows.append(row)
        writer = self.write_db("w")
        writer[0].writerows(temp_rows)
        reader[1].close()
        writer[1].close()


class UserDB(db.AbstractDBHandler):
    def __init__(self, db_name):
        self._db_name = db_name

    def open_db(self, operation):
        database = open(self._db_name + ".csv", operation, newline="")
        return database

    def read_db(self, operation):
        database = self.open_db(operation)
        reader = csv.reader(database, delimiter=",")
        return [reader, database]

    def write_db(self, operation):
        database = self.open_db(operation)
        writer = csv.writer(database, delimiter=",")
        return [writer, database]

    def add_row(self, user):
        writer = self.write_db("a")
        writer[0].writerow(user)
        writer[1].close()

    def get_row(self, user_id):
        reader = self.read_db("r")
        for row in reader[0]:
            if row[0] == user_id:
                reader[1].close()
                return row

    def get_all_rows(self):
        temp_rows = []
        reader = self.read_db("r")
        next(reader[0])
        for row in reader[0]:
            temp_rows.append(row)
        reader[1].close()
        return temp_rows

    def get_id(self, user_name):
        reader = self.read_db("r")
        for row in reader[0]:
            if row[1] == user_name:
                reader[1].close()
                return row[0]
