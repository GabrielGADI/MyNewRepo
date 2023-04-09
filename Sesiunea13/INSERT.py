import sqlite3  # importam librarie pentru SQL(sqlite3)
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()  # cream obiect de tip cursor

# INSERT -inseram date in tabel

# mod inserare cate unul
# cursor.execute("INSERT INTO Students (name, email, age) VALUES ('Adam', 'adam@v.com', 28);")
# cursor.execute("INSERT INTO Students (name, email, age) VALUES ('Eva', 'eva@v.com', 25);")
# conn.commit()
cursor.execute("SELECT * FROM Students;")
pprint(cursor.fetchall())

# mod inserare mai multe date deodata
grades_values = [
    ("Web Dev", 8, 1),
    ("DB Dev", 10, 1),
    ("DB Dev", 6, 2),
    ("Front-End", 10, 2),
    ("Web Dev", 9, 2),
    ("Web Dev", 8, 2),
    ("Web Dev", 7, 1),
]
sql_query = "INSERT INTO grades (topic, grade, student_id) VALUES (?,?,?)"
cursor.executemany(sql_query, grades_values)
# conn.commit() # se aplica in baza de date
# cursor.execute("SELECT * FROM grades")
pprint(cursor.fetchall())
