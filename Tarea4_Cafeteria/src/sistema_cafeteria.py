from observer import Sujeto


class SistemaCafeteria:
    def __init__(self):
        self.sujeto = Sujeto()
        self.pedidos = {}

    def registrar_cliente(self, cliente):
        self.sujeto.agregar_observador(cliente)

    def asignar_pedido(self, cliente, producto):
        self.pedidos[producto] = cliente

    def preparar(self, producto):
        cliente = self.pedidos.get(producto)

        if producto.tipo() == "bebida":
            print("[Barista]: Preparo bebida:", producto.descripcion())
        else:
            print("[Pastelero]: Preparo comida:", producto.descripcion())

        self.sujeto.notificar_a(cliente, producto)
