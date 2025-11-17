from abc import ABC
from productos import ProductoBase


# DECORADOR BASE
class DecoradorProducto(ProductoBase, ABC):
    def __init__(self, producto_envuelto):
        self.producto_envuelto = producto_envuelto

    def preparar(self):
        return self.descripcion()

    def tipo(self):
        return self.producto_envuelto.tipo()


# DECORADORES CONCRETOS
class Leche(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} con leche"

class Canela(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} y canela"

class Crema(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} con crema"

class RellenoChocolate(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} con relleno de chocolate"
    
class DobleEspresso(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} doble espresso"

