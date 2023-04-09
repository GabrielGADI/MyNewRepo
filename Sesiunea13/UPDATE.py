import sqlite3
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#vom schimba nota unde este studentul x la materia x care are nota momentan y
sql_query="UPDATE grades SET grade=? WHERE student_id=? and topic=? And GRADE=?"
# 10=noua nota(SET grade), 2=student_id(studentul), Web Dev=topic(materia), 9=GRADE(nota actuala)
cursor.execute(sql_query,(10,2, "Web Dev",7))
conn.commit()
cursor.execute("SELECT * FROM Grades;")
pprint(cursor.fetchall())
