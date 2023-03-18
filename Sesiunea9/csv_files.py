# .csv - comma separated values - fisiere care contin valori separate prin ","
import csv
from pprint import pprint # un afisaj mai evident


# mod de citire dintr-un fisire csv
def read(filename):
    with open(filename, "r") as f:
        result = [] # salvam intr-o lista goala avand mai multe valori
        reader = csv.reader(f)
        for row in reader: # se va lua linie cu linie
            result.append(row)
    return result[1:] # [1:] eliminare cap de tabel


pprint(read("employees.csv"))

# 1-a metoda de scriere in .csv
def write(data, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)# returneaza atata timp cat este format o lista de liste


data=[
    ["Nume", "Varsta"],
    ["Sergiu", "25"],
    ["Andrei", "30"],
    ["Cristi", "34"]
]

write(data, "employees2.csv")

# mod citire format lista de dictionare
def read_dict(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


pprint(read_dict("employees.csv"))

# date in format dictionar
data2=[
    {"Nume": "Sergiu", "Varsta": "24"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}
    ]

# 2-a metoda de scriere
def write_dict(filename, data):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, data[0].keys())# obtinem cheile din dictionarele noastre (nume, varsta)
        writer.writeheader() # scriere cap de tabel
        writer.writerows(data)


write_dict("employees2.csv", data2)

