# Módulo: main.py

from fastapi import FastAPI, HTTPException, status
from models import User
from database import insert_user, get_users, create_table, update_user, delete_user

# Aseguramos que la tabla de usuarios exista al iniciar la app
create_table()

app = FastAPI()

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
@app.post("/users/")
def create_user(user: User):
  if not insert_user(user.name, user.email):
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT, # El código 409 es para conflictos
      detail = "El email ya está registrado"
    )
  return {"message": "Usuario creado exitosamente"}

# Endpoint para leer todos los usuarios
@app.get("/users/")
def read_users():
  users = get_users()
  return users

# Endpoint para actualizar un usuario
@app.put("/users/{user_id}")
def update_existing_user(user_id: int, user: User):
  if not update_user(user_id, user.name, user.email):
    # Si el usuario no existe, levanta un error 404
    # Si el correo ya existe, también retorna False
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail = "El correo ya está registrado"
    )
  return {"message": "Usuario actualizado exitosamente"}

# Endpoint para eliminar un usuario
@app.delete("/users/{user_id}")
def delete_existing_user(user_id: int):
  if not delete_user(user_id):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail = "Usuario no encontrado"
    )
  return {"message": "Usuario eliminado exitosamente"}
