# Módulo: database.py

import sqlite3

DATABASE_NAME = "users.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    """)
    conn.commit()
    conn.close()

# Para ejecutarlo la primera vez:
# create_table()

"""
Dentro del archivo database.py, crea una función insert_user.
Esta función debe aceptar name (string) y email (string) como argumentos,
e insertar un nuevo registro en la tabla users que ya está definida.
No te olvides de hacer conn.commit() para guardar los cambios y conn.close() al final.
"""

def insert_user(name: str, email: str):
    conn = get_db()
    cursor = conn.cursor()
    # Usamos (?) como placeholders
    cursor.execute("""
        INSERT INTO users (name, email) VALUES (?, ?);
    """, (name, email)) # Pasamos los valores como una tupla
    conn.commit()
    conn.close()