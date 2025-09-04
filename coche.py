# Python
class Coche:
    def __init__(self, marca):
        self.marca = marca
    
    def arrancar(self):
        print("Este coche ",self.marca,", ha arrancado")

mi_coche = Coche("Toyota")
mi_coche.arrancar()
