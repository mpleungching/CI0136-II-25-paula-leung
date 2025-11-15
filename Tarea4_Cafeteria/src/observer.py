from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def actualizar(self, producto):
        pass

class Cliente(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, producto):
        print(f"[Sistema]: {self.nombre}, tu {producto.tipo()} está lista: {producto.descripcion()}")

class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_a(self, observador, producto):
        observador.actualizar(producto)
