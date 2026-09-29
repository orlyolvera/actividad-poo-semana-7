from dataclasses import dataclass


@dataclass
class Cliente:
    codigo: str
    nombre: str
    tramite: str

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.tramite}"
