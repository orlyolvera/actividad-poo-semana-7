from modelos import Cliente
from repository import ClienteRepository


def test_repository_agrega_y_consulta():
    repository = ClienteRepository()
    cliente = Cliente("C001", "Ana", "Pago")

    repository.agregar_cliente(cliente)

    assert repository.cantidad_clientes() == 1
    assert repository.siguiente_cliente() == cliente


def test_repository_atiende_en_orden_fifo():
    repository = ClienteRepository()
    cliente1 = Cliente("C001", "Ana", "Pago")
    cliente2 = Cliente("C002", "Luis", "Consulta")

    repository.agregar_cliente(cliente1)
    repository.agregar_cliente(cliente2)

    assert repository.atender_cliente() == cliente1
    assert repository.atender_cliente() == cliente2
    assert repository.atender_cliente() is None
    assert repository.esta_vacio()


def test_repository_listar_no_elimina():
    repository = ClienteRepository()
    cliente1 = Cliente("C001", "Ana", "Pago")
    cliente2 = Cliente("C002", "Luis", "Consulta")

    repository.agregar_cliente(cliente1)
    repository.agregar_cliente(cliente2)

    assert repository.listar_clientes() == [cliente1, cliente2]
    assert repository.cantidad_clientes() == 2
