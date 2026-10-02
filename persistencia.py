import json
from pathlib import Path
from modelos import Cliente

def cargar_clientes(archivo):
    ruta = Path(archivo)
    if not ruta.exists():
        return []
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return [Cliente(str(x["codigo"]), str(x["nombre"]), str(x["tramite"])) for x in datos]

def guardar_clientes(archivo, clientes):
    datos = [{"codigo": c.codigo, "nombre": c.nombre, "tramite": c.tramite} for c in clientes]
    Path(archivo).write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
