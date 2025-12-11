import sqlite3

print("🔨 Re-construyendo base de datos con nuevas columnas...")

conexion = sqlite3.connect('futbol.db')
cursor = conexion.cursor()

cursor.execute('DROP TABLE IF EXISTS jugadores')


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


jugador_ejemplo = (
    "Lamine Yamal",          
    "13/07/2007",          
    17,                      
    "68 kg",                
    "1.80 m",                
    "Izquierda",             
    10,                      
    15,                     
    "Excelente visión de juego, debe mejorar físico.", 
    "Proyección de estrella mundial según estadísticas.", 
    "Jorge Mendes",         
    "+34 600 000 000",    
    "@lamineyamal",         
    "https://youtube.com/watch?v=ejemplo", 
    "https://img.a.transfermarkt.technology/portrait/header/937958-1700816462.jpg", 
    "FC Barcelona",         
    "Mataró"                 
)


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
