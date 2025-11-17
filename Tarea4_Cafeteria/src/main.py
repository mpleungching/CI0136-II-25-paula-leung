from sistema_cafeteria import SistemaCafeteria
from observer import Cliente
from productos import Cafe, TeVerde, Croissant
from decoradores import Leche, Canela, Crema, RellenoChocolate, DobleEspresso


def main():
    print("=== Simulación de Cafeteria === \n")
    sistema = SistemaCafeteria()

    # PEDIDO ANA
    print("Cliente: Ana")
    Ana = Cliente("Ana")
    sistema.registrar_cliente(Ana)

    print("Ordena un café con leche y canela")
    print("Ordena un croissant con relleno de chocolate\n")

    pedido1 = Canela(Leche(Cafe()))
    pedido2 = RellenoChocolate(Croissant())
    sistema.asignar_pedido(Ana, pedido1)
    sistema.asignar_pedido(Ana, pedido2)

    # PEDIDO CARLOS
    print("Cliente: Carlos")
    Carlos = Cliente("Carlos")
    sistema.registrar_cliente(Carlos)

    print("Ordena un té verde")
    print("Ordena un café doble espresso con crema\n")

    pedido3 = TeVerde()
    pedido4 = Crema(DobleEspresso(Cafe()))
    sistema.asignar_pedido(Carlos, pedido3)
    sistema.asignar_pedido(Carlos, pedido4)

    sistema.preparar(pedido1)
    sistema.preparar(pedido2)
    sistema.preparar(pedido3)
    sistema.preparar(pedido4)

if __name__ == "__main__":
    main()
