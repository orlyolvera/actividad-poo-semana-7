# Semana 7 — Sistema de Atención de Clientes

## Descripción
Sistema de atención de clientes que utiliza una cola FIFO para atender primero al cliente que llegó primero.

## Objetivo
Aplicar una cola implementada manualmente, el patrón Repository, persistencia de datos, interfaz gráfica y pruebas unitarias.

## Funcionalidades
- Cola FIFO mediante nodos enlazados.
- Agregar, eliminar y consultar el siguiente elemento.
- Verificar si la cola está vacía y consultar su cantidad.
- Patrón Repository.
- Persistencia mediante archivo JSON.
- Interfaz gráfica mediante Tkinter.
- Pruebas unitarias con pytest.

## Archivos
- `cola.py`: cola FIFO manual.
- `modelos.py`: modelo Cliente.
- `repository.py`: Repository.
- `persistencia.py`: almacenamiento JSON.
- `main.py`: aplicación de consola.
- `gui.py`: interfaz gráfica.
- `test_cola.py`: pruebas de cola.
- `test_repository.py`: pruebas del Repository.
- `clientes.json`: datos persistentes.

## Ejecución

Instalar dependencias:
```bash
python -m pip install -r requirements.txt
```

Ejecutar interfaz gráfica:
```bash
python gui.py
```

Ejecutar pruebas:
```bash
python -m pytest -v
```

## Lenguaje
Python.
