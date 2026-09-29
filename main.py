from modelos import Cliente
from repository import ClienteRepository


def mostrar_menu():
    print("\n=== SISTEMA DE ATENCIÓN DE CLIENTES ===")
    print("1. Agregar cliente")
    print("2. Atender siguiente cliente")
    print("3. Consultar siguiente cliente")
    print("4. Ver cantidad de clientes")
    print("5. Ver clientes en espera")
    print("6. Verificar si la cola está vacía")
    print("0. Salir")


def main():
    repository = ClienteRepository()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            tramite = input("Trámite: ").strip()

            if not codigo or not nombre or not tramite:
                print("Todos los campos son obligatorios.")
                continue

            repository.agregar_cliente(Cliente(codigo, nombre, tramite))
            print("Cliente agregado correctamente.")

        elif opcion == "2":
            cliente = repository.atender_cliente()
            print(f"Cliente atendido: {cliente}" if cliente else "No hay clientes en espera.")

        elif opcion == "3":
            cliente = repository.siguiente_cliente()
            print(f"Siguiente cliente: {cliente}" if cliente else "No hay clientes en espera.")

        elif opcion == "4":
            print(f"Clientes almacenados: {repository.cantidad_clientes()}")

        elif opcion == "5":
            clientes = repository.listar_clientes()
            if not clientes:
                print("No hay clientes en espera.")
            else:
                print("\nClientes en espera:")
                for i, cliente in enumerate(clientes, 1):
                    print(f"{i}. {cliente}")

        elif opcion == "6":
            print("¿La cola está vacía?:", "sí" if repository.esta_vacio() else "no")

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
