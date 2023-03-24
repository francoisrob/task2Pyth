import time
import os

from generate import GenerateCSV
from importcsv import ImportCSV


class MainMenu:
    def __init__(self):
        self.choice = None
        self.options = {
            '1': GenerateCSV().run,
            '2': ImportCSV().run,
            'q': self.exit
        }

    @staticmethod
    def display_menu():
        print("""
        ==========================================
        |               TASK 2   :               |
        ==========================================
        |   1: Generate CSV                      |
        |   2: Import CSV                        |
        |   q: Quit                              |
        ==========================================
        """)

    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.display_menu()
            self.choice = input("Enter your choice> ")
            if self.choice in self.options:
                self.options[self.choice]()
            else:
                print("Invalid choice, please try again.")
                time.sleep(1)

    @staticmethod
    def exit():
        print("Exiting program...")
        time.sleep(1)
        exit()


menu = MainMenu()
menu.run()
