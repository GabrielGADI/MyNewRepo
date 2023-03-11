# json = java script object notation

import json
from pprint import pprint

def read(filename):
    with open(filename, "r") as f:
        return json.load(f)


pprint(read("employees.json"))

data2 = [
    {"Nume": "Sergiu", "Varsta": "24"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}

]


def write(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4) # adaugand parametru indent=4 pentru identare 4 spatii


write("employees2.json", data2) # se creeaza fisier json