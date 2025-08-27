# Módulo: main.py

"""
@app.get("/")
def read_root():
    return {"message": "Hola, mundo"}
Crea una nueva ruta @app.get("/saludo/{nombre}")
que tome un parámetro de ruta llamado nombre y
retorne un JSON con el mensaje {"saludo": "Hola, [nombre]!"}.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo/{nombre}")
def read_root(nombre: str):
    return {"saludo": f"Hola, [{nombre}]!"}