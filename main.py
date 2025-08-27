# Módulo: main.py

from fastapi import FastAPI
from models import Product, User
from database import insert_user

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

# Crear un usuario
@app.post("/users/")
def create_user(user: User):
  # Tu lógica aquí
  # Pista: los datos del usuario están en la variable `user`
  insert_user(user.name, user.email)
  return {"message": "Usuario creado exitosamente"}