# Módulo: main.py

from fastapi import FastAPI
from models import User
from database import insert_user, get_users, create_table

# Aseguramos que la tabla de usuarios exista al iniciar la app
create_table()

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hola, mundo"}

#Crea una nueva ruta @app.get("/saludo/{nombre}")
#que tome un parámetro de ruta llamado nombre y
#retorne un JSON con el mensaje {"saludo": "Hola, [nombre]!"}.

@app.get("/saludo/{nombre}")
def read_root(nombre: str):
  return {"saludo": f"Hola, [{nombre}]!"}

# Endpoint para crear un nuevo usuario
@app.post("/users/")
def create_user(user: User):
  insert_user(user.name, user.email)
  return {"message": "Usuario creado exitosamente"}

# Endpoint para leer todos los usuarios
@app.get("/users/")
def read_users():
  users = get_users()
  return users