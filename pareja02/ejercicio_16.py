"""
EJERCICIO 16: Ciudades y personas
Implementar funciones para trabajar con listas de ciudades y personas.
"""

from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

# Datos de ejemplo
ciudades = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Córdoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquín", "Córdoba"]
]

personas = [
    ["Juan Perez", 26782345, "Carlos Paz"],
    ["María Gomez", 40173542, "Rosario"],
    ["Ana Ríos", 9216378, "Cosquín"]
]

print("DATOS:")
print("\nCiudades:")
for ciudad in ciudades:
    print(f"  {ciudad[0]} - {ciudad[1]}")

print("\nPersonas:")
for persona in personas:
    print(f"  {persona[0]} (DNI: {persona[1]}) - {persona[2]}")

print("\n" + "="*60)

# a) Obtener ciudad de una persona
print("\na) Obtener ciudad por DNI:")
dni = 40173542
ciudad = obtenerCiudad(personas, dni)
print(f"   DNI {dni} vive en: {ciudad}")

# b) Obtener provincia de una persona
print("\nb) Obtener provincia por DNI:")
dni = 26782345
provincia = obtenerProvincia(personas, ciudades, dni)
print(f"   DNI {dni} vive en la provincia de: {provincia}")

# c) Contar población por provincia
print("\nc) Contar población por provincia:")
provincia = "Córdoba"
cantidad = contarPoblacion(personas, ciudades, provincia)
print(f"   Personas en {provincia}: {cantidad}")

provincia = "Santa Fe"
cantidad = contarPoblacion(personas, ciudades, provincia)
print(f"   Personas en {provincia}: {cantidad}")
