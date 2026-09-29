from cola import Cola
from modelos import Cliente


class ClienteRepository:
    """Repository que separa el manejo de datos de la lógica principal."""

    def __init__(self):
        self._cola = Cola()

    def agregar_cliente(self, cliente: Cliente):
        self._cola.agregar(cliente)

    def atender_cliente(self):
        return self._cola.eliminar()

    def siguiente_cliente(self):
        return self._cola.consultar_siguiente()

    def esta_vacio(self):
        return self._cola.esta_vacia()

    def cantidad_clientes(self):
        return self._cola.cantidad()

    def listar_clientes(self):
        clientes = []
        actual = self._cola.frente

        while actual is not None:
            clientes.append(actual.dato)
            actual = actual.siguiente

        return clientes
