# Módulo: models.py

from pydantic import BaseModel

class User(BaseModel):
  id: int | None = None  # id será opcional al crear un usuario
  name: str
  email: str

"""
Basado en el ejemplo, crea un modelo Product usando Pydantic.
Debe tener los siguientes campos: id (int, opcional), name (str) y price (float).
"""

class Product(BaseModel):
  id: int | None = None  # id será opcional al crear un usuario
  name: str
  price: float