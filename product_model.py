# Módulo : product_model.py

"""
Crea una clase llamada Product.
Debe tener un método __init__ que reciba name (string) y price (float) y los guarde como atributos.
Luego, añade un método llamado get_price_with_tax que retorne el precio del producto más un 10% de impuesto.
"""

class Product:
  def __init__(self, name: str, price: float):
    self.name = name
    self.price = price

  def get_price_with_tax(self):
    return self.price * 1.1

# Ejemplo de uso
product = Product(name="Laptop", price=1000.0)
precio_final = product.get_price_with_tax()
print(f"El precio final del producto es: {precio_final}!")
# O bien, usarlo en otra operación
total_orden = precio_final + 50  # Podemos sumarlo con otros números