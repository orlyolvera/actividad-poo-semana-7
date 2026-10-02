from cola import Cola
from modelos import Cliente
from persistencia import cargar_clientes, guardar_clientes

class ClienteRepository:
    def __init__(self, archivo=None):
        self._cola = Cola()
        self._archivo = archivo
        if archivo:
            for cliente in cargar_clientes(archivo):
                self._cola.agregar(cliente)

    def _guardar(self):
        if self._archivo:
            guardar_clientes(self._archivo, self.listar_clientes())

    def agregar_cliente(self, cliente: Cliente):
        self._cola.agregar(cliente)
        self._guardar()

    def atender_cliente(self):
        cliente = self._cola.eliminar()
        if cliente is not None:
            self._guardar()
        return cliente

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
