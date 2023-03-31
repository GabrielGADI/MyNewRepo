import csv


class UsersRepo:
    def __init__(self, filename):
        self.filename = filename

    # deschidem fisierul si returnam intreg continutul
    def read(self):
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)  # reader este iterator de fisier

            return list(reader)  # afiseaza datele

    # deschidem fisierul si returnam continut dupa nume(unul)
    def find_one(self, name):
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for user in reader:
                if user["name"] == name:
                    return user

    # adaugam un utilizator nou
    def create(self, new_user):
        with open(self.filename,
                  "a") as f:  # folosim modul append "a" cand adaugam unul, cu writte "w" scriem tot fisierul
            writer = csv.writer(f)
            writer.writerow(new_user.values())  # dintr-un fisier obtinem doar valorile cu ".value"
