# Python
class Coche:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print(f"Coche {self.marca} arrancado")

while True:
    marca = input("Introduce la marca del coche (o escribe 'salir' para terminar): ")
    if marca.lower() == 'salir':
        print("Programa finalizado.")
        break
    mi_coche = Coche(marca)
    mi_coche.arrancar()
