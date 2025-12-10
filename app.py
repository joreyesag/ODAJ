from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# --- PROTECCIÓN DE RUTA ---
# Esto asegura que encuentre la DB sin importar desde dónde se ejecute el servidor
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, 'futbol.db')

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"Error conectando a la DB: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/jugadores')
def api_jugadores():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
            
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM jugadores')
        filas = cursor.fetchall()
        conn.close()
        
        # Convertimos las filas a diccionarios
        lista_jugadores = [dict(fila) for fila in filas]
        return jsonify(lista_jugadores)
    except Exception as e:
        print(f"Error en la API: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Esto solo corre si lo ejecutas en tu PC local
    app.run(debug=True, port=5000)