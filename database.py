# Módulo: database.py

import sqlite3

DATABASE_NAME = "users.db"

def get_db():
  conn = sqlite3.connect(DATABASE_NAME)
  # Permite acceder a las columnas por nombre
  conn.row_factory = sqlite3.Row
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
  cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
  conn.commit()
  conn.close()


"""
El objetivo es crear un endpoint que recupere todos los usuarios
de la base de datos y los retorne como una lista.
"""

def get_users():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("SELECT id, name, email FROM users")
  users_db = cursor.fetchall()
  conn.close()

  # Convertimos los resultados a una lista de diccionarios
  users = [{"id": user["id"], "name": user["name"], "email": user["email"]} for user in users_db]
  return users

