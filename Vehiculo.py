# Python (Clase abstracta)
from abc import ABC, abstractmethod
import json
import os

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print("Acelerando...")

    def to_dict(self):
        return {"tipo": "Coche", "marca": self.marca}

def guardar_vehiculo(objeto):
    archivo = "Vehiculo.json"
    # Si el archivo existe, carga la lista, si no, crea una nueva
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            try:
                lista = json.load(f)
            except json.JSONDecodeError:
                lista = []
    else:
        lista = []
    lista.append(objeto.to_dict())
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

while True:
    marca = input("Introduce la marca del coche (o escribe 'salir' para terminar): ")
    if marca.lower() == 'salir':
        print("Programa finalizado.")
        break
    coche = Coche(marca)
    coche.acelerar()
    guardar_vehiculo(coche)
