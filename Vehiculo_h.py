# Python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

# Crear un coche con marca "Toyota" y modelo "1994"
coche = Coche("Toyota", "1994")
print(f"Marca: {coche.marca}, Modelo: {coche.modelo}")
