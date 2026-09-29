# Semana 7 — Sistema de Atención de Clientes

## Problema seleccionado
Sistema de atención de clientes donde se atiende primero al cliente que llegó primero.

## Estructura de datos
Se implementó manualmente una **cola FIFO** mediante nodos enlazados, sin utilizar `queue.Queue` ni `collections.deque`.

Operaciones:
- Agregar elementos.
- Eliminar elementos.
- Consultar el siguiente elemento.
- Verificar si está vacía.
- Consultar la cantidad.

## Patrón Repository
`ClienteRepository` separa el manejo de los datos de la lógica principal de la aplicación. El Repository utiliza internamente la cola.

## Archivos
- `cola.py`: implementación manual de la cola.
- `modelos.py`: modelo Cliente.
- `repository.py`: patrón Repository.
- `main.py`: aplicación principal.
- `test_cola.py`: pruebas de la cola.
- `test_repository.py`: pruebas del Repository.
- `requirements.txt`: dependencia pytest.

## Instalación
```bash
python -m pip install -r requirements.txt
```

## Ejecutar aplicación
```bash
python main.py
```

## Ejecutar pruebas
```bash
python -m pytest -v
```

## Ejemplo FIFO
Si llegan C001, C002 y C003, se atienden en este orden:

`C001 -> C002 -> C003`
