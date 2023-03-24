import os
import time
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from database import Database


class ImportCSV:
    def __init__(self):
        self.options = {
            '1': self.choosefile,
        }

    @staticmethod
    def display_menu():
        print("""
        ==========================================
        |               CSV Import:              |
        ==========================================
        |   1: Choose the CSV file               |
        |   q: Main Menu                         |
        ==========================================
        """)

    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_menu()
            choice = input("Enter your choice> ")
            if choice in self.options:
                self.options[choice]()
                break
            elif choice == 'q':
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, please try again.")
            time.sleep(1)

    @staticmethod
    def importcsv(file):
        values = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                sid = row[0]
                name = row[1]
                surname = row[2]
                initials = row[3]
                age = row[4]
                dob = row[5]
                values.append("('{}','{}','{}','{}','{}','{}')".format(sid,
                                                                       name,
                                                                       surname,
                                                                       initials,
                                                                       age,
                                                                       dob))
        db = Database()
        db.connect()
        db.insert(values)
        db.close()

    def choosefile(self):
        Tk().withdraw()
        file = askopenfilename()
        if not (len(file) == 0):
            if file.endswith('.csv'):
                print("Importing {}...".format(file))
                tic = time.perf_counter()
                self.importcsv(file)
                toc = time.perf_counter()
                print(f"Successfully imported {file} in {toc - tic:0.4f} seconds")
                input("Press any key to return to the main menu...")
            else:
                print("Invalid file type, please try again.")
                time.sleep(1)
        else:
            self.run()
