'''
1. Sa se scrie o functie care citeste date dintr-un fisier csv si le scrie intr-un fisier json.
 Functia primeste numele fisierelor ca parametri.
'''
import csv
import json


def convert_csv_to_json(csv_file_path, json_file_path):
    # Deschide fisierul CSV pentru citire
    with open(csv_file_path, 'r') as csv_file:
        # Citeste continutul fisierului CSV
        csv_data = csv.DictReader(csv_file)

        # Transforma datele CSV in dictionar Python
        data = []
        for row in csv_data:
            data.append(row)

    # Scrie datele in fisierul JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


convert_csv_to_json('input.csv', 'output.json')

'''
2.Sa se scrie o functie care citeste date dintr-un fisier json si le imparte in alte doua fisiere astfel
 incat prima jumatate a datelor va fi in fisierul prima_jumatate.json, iar a doua in a_doua_jumatate.json.
'''


def split_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    mid = len(data) // 2  # impartim in 2 fisierul ce contine date

    first_half = data[:mid]  # prima jumatate
    second_half = data[mid:]  # a doua jumatate

    with open('prima_jumatate.json', 'w') as f:
        json.dump(first_half, f, indent=4)

    with open('a_doua_jumatate.json', 'w') as f:
        json.dump(second_half, f, indent=4)


split_json_file('input.json')

'''
3.Sa se scrie o functie care citeste date dintr-un fisier csv si le elimina pe cele care 
in oricare coloana contin litera ‘a’. Dupa aceea va actualiza fisierul cu datele ce raman.
'''


def remove_rows_with_a(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # citim header-ul
        rows_to_keep = []
        for row in reader:
            if not any('a' in col for col in row):
                rows_to_keep.append(row)

    with open(filename, 'w', newline='') as csvfile:  # new line folosit pentru a evita adaugarea unui rand gol
        writer = csv.writer(csvfile)  # scriem datele in fisier
        writer.writerow(header)  # rescriem header-ul
        writer.writerows(rows_to_keep)  # scriem fiecare rand din lista in fisier


remove_rows_with_a('input.csv')  # actualizam fisierul csv