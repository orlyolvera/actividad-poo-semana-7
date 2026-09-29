from cola import Cola


def test_cola_inicia_vacia():
    cola = Cola()
    assert cola.esta_vacia()
    assert cola.cantidad() == 0
    assert cola.consultar_siguiente() is None
    assert cola.eliminar() is None


def test_agregar_incrementa_cantidad():
    cola = Cola()
    cola.agregar("A")
    cola.agregar("B")
    assert cola.cantidad() == 2
    assert not cola.esta_vacia()


def test_fifo_y_consulta_siguiente():
    cola = Cola()
    cola.agregar("A")
    cola.agregar("B")
    cola.agregar("C")

    assert cola.consultar_siguiente() == "A"
    assert cola.eliminar() == "A"
    assert cola.eliminar() == "B"
    assert cola.eliminar() == "C"
    assert cola.esta_vacia()


def test_cola_vuelve_a_vacia():
    cola = Cola()
    cola.agregar("A")
    cola.eliminar()
    assert cola.esta_vacia()
    assert cola.cantidad() == 0
