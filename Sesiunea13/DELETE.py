import sqlite3
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#metoda de transmitere date sub forma de dictionar
#':topic' si ':id key' dintr-un dictionar de unde isi ia acest query(sql_query) datele datele
sql_query = "DELETE FROM grades WHERE topic=:topic AND student_id=:id; "
values_dict = {"id": 1, "topic": "Web Dev"}# transmitem datele sub forma de dictionar
cursor.execute(sql_query, values_dict)
conn.commit()
cursor.execute("SELECT * FROM Grades;")
pprint(cursor.fetchall())
