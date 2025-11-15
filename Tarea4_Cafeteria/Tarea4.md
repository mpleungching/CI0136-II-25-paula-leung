

# Tarea 4: Simulación de Cafetería

Se implementa un sistema sencillo de gestión de pedidos mediante el uso de dos patrones de diseño fundamentales: **Decorator** y **Observer**. Con e objetivo de simular la preparación de bebidas y alimentos, permitiendo extender los productos con ingredientes adicionales y notificando al cliente cuando su pedido está listo.

---

## Patrón Decorator

El patrón Decorator se utilizó para añadir ingredientes adicionales a bebidas y alimentos sin alterar las clases concretas de los productos.

Los productos pueden tener combinaciones variadas, por ejemplo:

* Café con leche
* Café con leche y canela
* Café doble espresso con crema
* Croissant con relleno de chocolate

Sin un decorador, sería necesario crear múltiples clases como `CafeConLeche`, `CafeConCremaYCanela`, lo cual lo hace insostenible.

El decorador permite envolver un producto dentro de otro y agregar características extras:

```python
pedido1 = Canela(Leche(Cafe()))
```

Cada decorador solo añade un elemento a la descripción y delega el resto al producto envuelto.

### Estructura

Clase base del decorador:

```python
class DecoradorProducto(ProductoBase, ABC):
    def __init__(self, producto_envuelto):
        self.producto_envuelto = producto_envuelto

    def preparar(self):
        return self.descripcion()

    def tipo(self):
        return self.producto_envuelto.tipo()
```

Decoradores concretos:

```python
class Leche(DecoradorProducto):
    def descripcion(self):
        return f"{self.producto_envuelto.descripcion()} con leche"
```

El diseño permite agregar decoradores en cadena y extender productos en tiempo de ejecución sin modificar el código ya existente.

---

# Patrón Observer

El patrón Observer se utiliza para notificar al cliente cuando su producto está listo.

El sistema requiere que cada cliente reciba una notificación personalizada para sus pedidos:

* "[Sistema]: Ana, tu bebida está lista..."
* "[Sistema]: Carlos, tu comida está lista..."

### Estructura

Interfaz del observador:

```python
class Observador(ABC):
    @abstractmethod
    def actualizar(self, producto):
        pass
```

Observador concreto:

```python
class Cliente(Observador):
    def actualizar(self, producto):
        print(f"[Sistema]: {self.nombre}, tu {producto.tipo()} está lista: {producto.descripcion()}")
```

Sujeto que gestiona observadores:

```python
class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_a(self, observador, producto):
        observador.actualizar(producto)
```

A diferencia de una notificación general a todos los observadores, solo se notifica al cliente que realizó el pedido. Esto evita que Carlos reciba notificaciones de pedidos de Ana y viceversa.

---

# Sistema de Cafetería y Lógica del Pedido

`SistemaCafeteria` administra las relaciones entre productos y clientes, tomando en cuenta cuál cliente debe ser notificado.

```python
class SistemaCafeteria:
    def __init__(self):
        self.sujeto = Sujeto()
        self.pedidos = {} 
```

Asignación de pedidos:

```python
def asignar_pedido(self, cliente, producto):
    self.pedidos[producto] = cliente
```

Preparación del pedido:

```python
def preparar(self, producto):
    cliente = self.pedidos.get(producto)

    if producto.tipo() == "bebida":
        print("[Barista]: Preparo bebida:", producto.descripcion())
    else:
        print("[Pastelero]: Preparo comida:", producto.descripcion())

    self.sujeto.notificar_a(cliente, producto)
```

# Decisiones de Diseño Importantes

### 1. Uso de interfaces abstractas

Las clases `ProductoBase` y `Observador` se diseñaron como abstractas para garantizar que:

* Todos los productos implementen `descripcion`, `preparar` y `tipo`.
* Cualquier observador proporcione un método `actualizar`.


### 2. Notificación específica al cliente

Aunque el patrón Observer suele notificar a todos los observadores, en esta implementación el sistema requiere que solo el cliente correspondiente reciba el mensaje.

```python
self.sujeto.notificar_a(cliente, producto)
```

### 3. Uso de Decoradores

El diseño permite combinaciones libres de complementos y cumple el principio Open/Closed. El sistema no necesita cambios si se quisiera agregar un nuevo ingrediente (decorador concreto).

---

## Créditos

María Paula Leung - C34258

--- 

## Referencias
[1] [Refactoring.Guru — Patrón Observer](https://refactoring.guru/design-patterns/observer)

[2] [Refactoring.Guru — Patrón Decorator](https://refactoring.guru/design-patterns/decorator)

