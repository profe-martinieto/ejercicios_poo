# Python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f"{self.titulo} - {self.autor}")

mi_libro = Libro("Cien años de soledad", "García Márquez")
mi_libro.mostrar_info()
