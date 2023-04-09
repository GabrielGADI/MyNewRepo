import sqlite3  # importam librarie pentru SQL(sqlite3)

conn = sqlite3.connect("students.db")
cursor = conn.cursor()  # cream obiect de tip cursor

# creare tabel
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, 
email TEXT,
age INTEGER NOT NULL CHECK(age>18)
);

CREATE TABLE IF NOT EXISTS Grades(
id INTEGER PRIMARY KEY AUTOINCREMENT,
topic TEXT,
grade INTEGER NOT NULL CHECK(0<=grade AND grade <=10),
student_id INTEGER NOT NULL,
FOREIGN KEY (student_id) REFERENCES Students(id)
);

""")
