import json
import os

class Mascota:
    def __init__(self, nombre, tipo, edad, vacunacion, duenio):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.vacunacion = vacunacion
        self.duenio = duenio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "edad": self.edad,
            "vacunacion": self.vacunacion,
            "duenio": self.duenio
        }

class GestorMascotas:
    def __init__(self, archivo_json):
        self.archivo_json = archivo_json
        self.mascotas = self.cargar_mascotas()

    def cargar_mascotas(self):
        if not os.path.exists(self.archivo_json):
            return []
        with open(self.archivo_json, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_mascotas(self):
        with open(self.archivo_json, "w", encoding="utf-8") as f:
            json.dump(self.mascotas, f, indent=4)

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota.to_dict())
        self.guardar_mascotas()

    def obtener_mascota(self, nombre):
        for m in self.mascotas:
            if m["nombre"] == nombre:
                return m
        return None

    def actualizar_mascota(self, nombre, nuevos_datos):
        for m in self.mascotas:
            if m["nombre"] == nombre:
                m.update(nuevos_datos)
                self.guardar_mascotas()
                return True
        return False

    def eliminar_mascota(self, nombre):
        inicial = len(self.mascotas)
        self.mascotas = [m for m in self.mascotas if m["nombre"] != nombre]
        if len(self.mascotas) < inicial:
            self.guardar_mascotas()
            return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorMascotas("mascotas.json")
    mascota1 = Mascota("Firulais", "Perro", 5, True, "Juan Perez")
    gestor.agregar_mascota(mascota1)
    print(gestor.obtener_mascota("Firulais"))
    gestor.actualizar_mascota("Firulais", {"edad": 6})
    gestor.eliminar_mascota("Firulais")