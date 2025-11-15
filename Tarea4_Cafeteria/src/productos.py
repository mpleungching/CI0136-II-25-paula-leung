from abc import ABC, abstractmethod


class ProductoBase(ABC):
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def tipo(self):
        pass


# PRODUCTOS CONCRETOS
class Cafe(ProductoBase):
    def __init__(self):
        self.nombre = "Café"

    def descripcion(self):
        return self.nombre

    def preparar(self):
        return self.descripcion()

    def tipo(self):
        return "bebida"


class TeVerde(ProductoBase):
    def __init__(self):
        self.nombre = "Té verde"

    def descripcion(self):
        return self.nombre

    def preparar(self):
        return self.descripcion()

    def tipo(self):
        return "bebida"


class Croissant(ProductoBase):
    def __init__(self):
        self.nombre = "Croissant"

    def descripcion(self):
        return self.nombre

    def preparar(self):
        return self.descripcion()

    def tipo(self):
        return "comida"
