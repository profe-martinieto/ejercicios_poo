# Python (Clase abstracta)
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        print("Acelerando...")
