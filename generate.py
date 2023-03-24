import csv
import datetime
import os
import time
import random


class GenerateCSV:
    def __init__(self):
        self.date = datetime.date.today()
        self.names = [
            "Bianca",
            "Jacques",
            "Francois",
            "Vance",
            "Pranav",
            "Thomas",
            "Carl",
            "Nico",
            "Luis",
            "Sean",
            "Sasha Cohen",
            "Erica",
            "Megan",
            "Katya",
            "Annalette",
            "Phillip",
            "Ricus",
            "Jowan",
            "Amiel",
            "Genise"
        ]
        self.surnames = [
            "Robbertze",
            "Harmon",
            "Bolton",
            "Guerrero",
            "Quinn",
            "Hubbard",
            "Moore",
            "Mahoney",
            "Abbott",
            "Spears",
            "Pierce",
            "Hood",
            "Cline",
            "Henderson",
            "Barnard",
            "Jensen",
            "Kirk",
            "Huynh",
            "Acosta",
            "Mcclain"
        ]

    @staticmethod
    def display_menu():
        print("""
        ==========================================
        |               Generate CSV:            |
        ==========================================
        |   Enter the amount of variations       |
        |   q: Main Menu                         |
        ==========================================
        """)

    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_menu()
            choice = input("Enter your choice> ")
            if choice.isdigit():
                print("Generating unique records...")
                tic = time.perf_counter()
                self.generate(choice)
                toc = time.perf_counter()
                print(f"Successfully generated {choice} unique variations in {toc - tic:0.4f} seconds.")
                input("Press any key to return to the main menu...")
                break
            elif choice == 'q':
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, please try again.")
            time.sleep(1)

    @staticmethod
    def get_initials(name):
        return ''.join([i[0] for i in name.split(' ')])

    def calc_age(self, dob):
        bday = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
        age = self.date.year - bday.year - ((self.date.month, self.date.day) < (bday.month, bday.day))
        return age

    @staticmethod
    def random_date(start=datetime.date(1940, 1, 1), end=datetime.date(2005, 1, 1)):
        delta = end - start
        return start + datetime.timedelta(days=random.randint(0, delta.days))

    def generate(self, choice):
        data = set()
        rows = []
        count = 0
        while count < int(choice):
            name = random.choice(self.names)
            surname = random.choice(self.surnames)
            dob = self.random_date().strftime("%Y-%m-%d")
            age = self.calc_age(dob)
            ihash = hash(name + surname + str(age) + dob)

            if ihash not in data:
                count += 1
                data.add(ihash)
                initials = self.get_initials(name)
                row = [count, name, surname, initials, age, dob]
                rows.append(row)

        if not os.path.exists('./output'):
            os.makedirs('./output')
        with open(os.path.join("./output", "output.csv"), "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Surname", "Initials", "Age", "DateOfBirth"])
            writer.writerows(rows)
