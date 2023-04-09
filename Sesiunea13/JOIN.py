import sqlite3
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# JOIN- unim date din mai multe tabele

# returnam toate datele si informatiile nume:Eva
sql_query = "SELECT * FROM students s JOIN grades g ON s.id=g.student_id WHERE s.name='Eva'"
cursor.execute(sql_query)
pprint((cursor.fetchall()))

# returnam numele,materia si nota lui Eva
# s.name=nume, g.grade=nota, g.topic=materia
sql_query = "SELECT s.name, g.grade, g.topic FROM students s JOIN grades g ON s.id=g.student_id WHERE s.name='Eva'"
cursor.execute(sql_query)
pprint((cursor.fetchall()))
