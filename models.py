# Módulo: models.py

"""
class User(BaseModel):
    id: int | None = None  # id será opcional al crear un usuario
    name: str
    email: str
"""

from pydantic import BaseModel

class Product(BaseModel):
    id: int | None = None  # id será opcional al crear un usuario
    name: str
    price: float