import sqlite3

print("🔨 Re-construyendo base de datos con nuevas columnas...")

# 1. Conexión
conexion = sqlite3.connect('futbol.db')
cursor = conexion.cursor()

# 2. Borrón y cuenta nueva
cursor.execute('DROP TABLE IF EXISTS jugadores')

# 3. Nueva estructura con TUS columnas
cursor.execute('''
    CREATE TABLE jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        nacimiento TEXT,
        edad INTEGER,
        peso TEXT,
        altura TEXT,
        pierna_buena TEXT,
        goles_oficiales INTEGER,
        asistencias_oficiales INTEGER,
        comentarios_profesor TEXT,
        ia_analisis TEXT,
        contactos TEXT,
        telefono TEXT,
        instagram TEXT,
        video_url TEXT,
        foto_url TEXT,
        equipos TEXT,
        ciudad TEXT
    )
''')

# 4. Datos de prueba actualizados (Lamine Yamal como ejemplo)
# Fíjate que ahora hay que llenar MUCHOS más datos por jugador
jugador_ejemplo = (
    "Lamine Yamal",          # nombre
    "13/07/2007",            # nacimiento
    17,                      # edad
    "68 kg",                 # peso
    "1.80 m",                # altura
    "Izquierda",             # pierna_buena
    10,                      # goles_oficiales
    15,                      # asistencias_oficiales
    "Excelente visión de juego, debe mejorar físico.", # comentarios_profesor
    "Proyección de estrella mundial según estadísticas.", # ia_analisis
    "Jorge Mendes",          # contactos (agente/padre)
    "+34 600 000 000",       # telefono
    "@lamineyamal",          # instagram
    "https://youtube.com/watch?v=ejemplo", # video_url
    "https://img.a.transfermarkt.technology/portrait/header/937958-1700816462.jpg", # foto_url
    "FC Barcelona",          # equipos
    "Mataró"                 # ciudad
)

# Insertamos el jugador con las 17 columnas de datos
sql_insert = '''
    INSERT INTO jugadores (
        nombre, nacimiento, edad, peso, altura, pierna_buena, 
        goles_oficiales, asistencias_oficiales, comentarios_profesor, 
        ia_analisis, contactos, telefono, instagram, video_url, 
        foto_url, equipos, ciudad
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

cursor.execute(sql_insert, jugador_ejemplo)

conexion.commit()
conexion.close()
print("✅ ¡Base de datos actualizada con las nuevas columnas!")