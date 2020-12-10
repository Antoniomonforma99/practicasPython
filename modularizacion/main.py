from funciones import *
import modelos

saludar("antonio")

despedir("antonio")

p = modelos.Persona("Antonio", "Montero")
print(f"{p.nombre}, {p.apellidos}")
