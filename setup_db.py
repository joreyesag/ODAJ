import sqlite3
conn = sqlite3.connect('futbol.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        posicion TEXT,
        equipo TEXT,
        valor TEXT
    )
''')

jugadores_iniciales = [
    ('Lionel Messi', 'Delantero', 'Inter Miami', '35M'),
    ('Erling Haaland', 'Delantero', 'Manchester City', '180M'),
    ('Jude Bellingham', 'Mediocampista', 'Real Madrid', '120M'),
    ('Kylian Mbappé', 'Delantero', 'PSG', '180M')
]

cursor.executemany('''
    INSERT INTO jugadores (nombre, posicion, equipo, valor)
    VALUES (?, ?, ?, ?)
''', jugadores_iniciales)

conn.commit()
conn.close()

print("✅ Base de datos 'futbol.db' creada y poblada con éxito.")
