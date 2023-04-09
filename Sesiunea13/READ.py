import sqlite3
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students;")
pprint(cursor.fetchall())
pprint(cursor.fetchone())
cursor.execute("SELECT * FROM Grades;")
pprint(cursor.fetchmany(4))  # va lua primele 4 elemente din acel raspuns
pprint(cursor.fetchmany(3))  # returneaza urmatoarele 3 elemente

cursor.execute("SELECT topic,grade FROM Grades;")  # pentru a selecta anumite coloane
pprint(cursor.fetchall())  # returneaza doar 2 campuri din raspuns doar coloane Topic si Grades

# putem filtra in functie de valorile din anumite coloane
cursor.execute("SELECT * FROM grades WHERE topic = ?", ("Web Dev",))  # ("Web Dev,") - tuplu
pprint(cursor.fetchall())
