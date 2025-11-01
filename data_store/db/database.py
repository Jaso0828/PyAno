import sqlite3
import os

db_path = '/Users/jaso/REPOS/PyAno/data_store/db/py_ano.db'

# Ako je baza oštećena, ručno ju izbriši prije pokretanja
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS pianos (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    description TEXT
)
''')

# Provjeri postoji li već isti unos
cur.execute("SELECT COUNT(*) FROM pianos WHERE id = 1")
exists = cur.fetchone()[0]

if not exists:
    cur.execute('''
    INSERT INTO pianos (id, name, type, description)
    VALUES (?, ?, ?, ?)
    ''', (
        1,
        'Steinway',
        'Grand piano',
        'The Steinway Model O is one of the most recognized and valued grand pianos from the Steinway & Sons brand, known for its excellence in crafting high-quality pianos.'
    ))
    print("✅ Novi red je dodan.")
else:
    print("ℹ️ Red s ID=1 već postoji, preskačem unos.")

con.commit()

cur.execute("SELECT * FROM pianos")
for row in cur.fetchall():
    print(row)

con.close()
