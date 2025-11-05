
from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

# Definimos listas de ejemplo
ciudades = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Córdoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquín", "Córdoba"]
]

personas = [
    ["Juan", 123, "Rosario"],
    ["Ana", 456, "Carlos Paz"],
    ["Luis", 789, "Rosario"],
    ["Maria", 101, "Cosquín"]
]

dni = int(input("Ingresar el DNI de la persona: "))
provincia = input("Ingresar el nombre de la provincia: ")

print("Ciudad de la persona:", obtenerCiudad(personas, dni))
print("Provincia de la persona:", obtenerProvincia(personas, ciudades, dni))
print(f"Cantidad de personas en {provincia}:", contarPoblacion(personas, ciudades, provincia))

