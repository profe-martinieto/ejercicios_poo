import tkinter as tk

# Modelo (POO puro)
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

# Lógica de negocio
class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

# GUI (Interfaz gráfica)
class AppTareas(tk.Tk):
    def __init__(self, gestor):
        super().__init__()
        self.gestor = gestor
        self.title("Gestor de Tareas")
        self.entrada = tk.Entry(self)
        self.entrada.pack()
        tk.Button(self, text="Agregar", command=self.agregar).pack()
    
    def agregar(self):
        tarea = Tarea(self.entrada.get())
        self.gestor.agregar_tarea(tarea)  # Delegar lógica al gestor
        print(f"Tarea agregada: {tarea.descripcion}")

# Uso
if __name__ == "__main__":
    gestor = GestorTareas()
    app = AppTareas(gestor)
    app.mainloop()
