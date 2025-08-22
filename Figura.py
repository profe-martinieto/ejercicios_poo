# Python
class Figura:
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2
