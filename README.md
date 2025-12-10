⚽ ODAJ - Plataforma de Scouting de Talentos (Ecuador)

ODAJ (Observación y Desarrollo de Atletas Juveniles) es una plataforma de gestión de talentos diseñada para el scouting de jóvenes futbolistas en Ecuador. Combina reportes de entrenadores con análisis de datos avanzado e inteligencia artificial para identificar y seguir la progresión de las promesas.

## 🚀 Tecnologías Utilizadas

Este proyecto es una aplicación web sencilla, escalable y modular.

* **Frontend:** HTML5, CSS (a través de **Tailwind CSS**), JavaScript.
* **Backend:** **Flask** (Micro-framework de Python).
* [cite_start]**Base de Datos:** **SQLite**[cite: 1, 2].

## 📂 Estructura del Proyecto

| Archivo | Descripción |
| :--- | :--- |
| `app.py` | Configuración del servidor Flask y la API REST para los datos de jugadores. |
| `crear_db.py` | Script de Python para inicializar y poblar la base de datos `futbol.db` con la estructura de scouting detallada. |
| `futbol.db` | [cite_start]Base de datos SQLite que almacena los perfiles detallados de los jugadores[cite: 1]. |
| `index.html` | Interfaz de usuario principal, que incluye la lista de talentos, filtros, el modal de perfil detallado y el acceso para entrenadores. |
| `setup_db.py` | (Alternativo/Legacy) Un script inicial para crear una base de datos con una estructura más simple. |

## 🛠️ Configuración e Instalación

Sigue estos pasos para poner la aplicación en funcionamiento en tu entorno local.

### Prerrequisitos

Necesitas tener **Python 3.x** y **pip** instalados.

### 1. Entorno Virtual

Se recomienda usar un entorno virtual:

```bash
# Crear entorno virtual (solo la primera vez)
python3 -m venv venv
# Activar el entorno virtual
source venv/bin/activate  # En Linux/macOS
# o
.\venv\Scripts\activate   # En Windows
