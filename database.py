import sqlite3
import os


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        if not os.path.exists('./db'):
            os.makedirs('./db')
        self.conn = sqlite3.connect("./db/db.sqlite")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS csv_import")
        self.cursor.execute("""
        CREATE TABLE csv_import (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Surname TEXT,
            Initials TEXT,
            Age INTEGER,
            DateOfBirth TEXT
        )""")
        self.conn.commit()

    def insert(self, values):
        self.cursor.execute("""INSERT INTO csv_import 
        (Id, 
        Name, 
        Surname, 
        Initials, 
        Age, 
        DateOfBirth) 
        VALUES {}""".format(','.join(values)))
        self.conn.commit()

    def close(self):
        self.conn.close()
