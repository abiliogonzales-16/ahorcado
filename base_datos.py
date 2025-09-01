import sqlite3

def crear_base_datos():
    conn = sqlite3.connect("ahorcado.db")
    cur = conn.cursor()

    # Crear tabla de palabras (lo esencial del juego)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS palabras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Base de datos 'ahorcado.db' creada.")
