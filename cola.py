class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """Cola FIFO implementada manualmente con nodos enlazados."""

    def __init__(self):
        self.frente = None
        self.final = None
        self._cantidad = 0

    def agregar(self, elemento):
        nuevo = Nodo(elemento)
        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self._cantidad += 1

    def eliminar(self):
        if self.esta_vacia():
            return None

        elemento = self.frente.dato
        self.frente = self.frente.siguiente
        self._cantidad -= 1

        if self._cantidad == 0:
            self.final = None

        return elemento

    def consultar_siguiente(self):
        if self.esta_vacia():
            return None
        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None

    def cantidad(self):
        return self._cantidad
