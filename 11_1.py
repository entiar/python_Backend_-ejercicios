import sqlite3
conn = sqlite3.connect("Alumnos.db")
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM alumnoslista WHERE Nombre = "Sandra"')
for row in rows:
    print(row)

cursor.close()
conn.close()
