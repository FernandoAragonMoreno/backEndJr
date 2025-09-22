import sqlite3

class UserRepository:
  def insert_user(self, conn: sqlite3.Connection, name: str, email: str):
    cursor = conn.cursor()
    try:
      cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
      conn.commit()
      return True # Retorna True si la inserción es exitosa
    except sqlite3.IntegrityError:
      return False # Retorna False si hay un error de integridad (ej. correo duplicado)

  def get_users(self, conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users_db = cursor.fetchall()

    # Convertimos los resultados a una lista de diccionarios
    users = [{"id": user["id"], "name": user["name"], "email": user["email"]} for user in users_db]
    return users

  def update_user(self, conn: sqlite3.Connection,user_id: int, name: str, email: str):
    cursor = conn.cursor()
    try:
      cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
      conn.commit()
      return cursor.rowcount > 0  # Retorna True si se actualizó una fila
    except sqlite3.IntegrityError:
      return False # Retorna False si hay un error de integridad (ej. correo duplicado)

  def delete_user(self, conn: sqlite3.Connection, user_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return cursor.rowcount > 0