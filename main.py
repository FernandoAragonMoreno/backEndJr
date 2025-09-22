# Módulo: main.py

from fastapi import FastAPI, HTTPException, status, Depends
from models import User
from repositories import UserRepository, pwd_context
from database import create_table
import sqlite3

#from database import insert_user, get_users, create_table, update_user, delete_user

# Aseguramos que la tabla de usuarios exista al iniciar la app
# create_table()

app = FastAPI()

# 1. Dependencia de la base de datos
def get_db():
  conn = sqlite3.connect("users.db")
  conn.row_factory = sqlite3.Row
  try:
    yield conn
  finally:
    conn.close()

"""
@app.get("/")
def read_root():
  return {"message": "Hola, mundo"}
"""

#Crea una nueva ruta @app.get("/saludo/{nombre}")
#que tome un parámetro de ruta llamado nombre y
#retorne un JSON con el mensaje {"saludo": "Hola, [nombre]!"}.

"""
@app.get("/saludo/{nombre}")
def read_root(nombre: str):
  return {"saludo": f"Hola, [{nombre}]!"}
"""

# Endpoint para crear un nuevo usuario
# 2. Uso de la dependencia de la base de datos - "Inyección de Dependencias"
@app.post("/users/")
def create_user(user: User, db: sqlite3.Connection = Depends(get_db)):
  repo = UserRepository()
  if not repo.insert_user(db, user.name, user.email, user.password):
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT, # El código 409 es para conflictos
      detail = "El email ya está registrado"
    )
  return {"message": "Usuario creado exitosamente"}

# Endpoint para leer todos los usuarios
@app.get("/users/")
def read_users(db: sqlite3.Connection = Depends(get_db)):
  repo = UserRepository()
  users = repo.get_users(db)
  return users

# Endpoint para actualizar un usuario
@app.put("/users/{user_id}")
def update_existing_user(user_id: int, user: User, db: sqlite3.Connection = Depends(get_db)):
  repo = UserRepository()
  if not repo.update_user(db, user_id, user.name, user.email, user.password):
    # Si el usuario no existe, levanta un error 404
    # Si el correo ya existe, también retorna False
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail = "El correo ya está registrado"
    )
  return {"message": "Usuario actualizado exitosamente"}

# Endpoint para eliminar un usuario
@app.delete("/users/{user_id}")
def delete_existing_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
  repo = UserRepository()
  if not repo.delete_user(db, user_id):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail = "Usuario no encontrado"
    )
  return {"message": "Usuario eliminado exitosamente"}

@app.post("/token")
def login(email: str, password: str, db: sqlite3.Connection = Depends(get_db)):
  repo = UserRepository()
  user = repo.get_user_by_email(db, email)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail = "Credenciales incorrectas"
    )

  # Verificar la contraseña
  if not pwd_context.verify(password, user["password"]):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail = "Credenciales incorrectas"
    )

  return {"message": "Inicio de sesión exitoso", "token": "TOKEN_FALSO_POR_AHORA"}
