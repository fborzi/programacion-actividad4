#Funciones con listas de ciudades y personas

from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

# Datos de ejemplo en el pdf
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

print("\nDatos:")
print(f"Ciudades: {ciudades}")
print(f"Personas: {personas}")

# obtenerCiudad
print("\na) Función obtenerCiudad:")
dni1 = 26782345
ciudad1 = obtenerCiudad(personas, dni1)
print(f"La persona con DNI {dni1} vive en: {ciudad1}")

dni2 = 40173542
ciudad2 = obtenerCiudad(personas, dni2)
print(f"La persona con DNI {dni2} vive en: {ciudad2}")

# obtenerProvincia
print("\nb) Función obtenerProvincia:")
dni3 = 26782345
provincia1 = obtenerProvincia(personas, ciudades, dni3)
print(f"La persona con DNI {dni3} vive en la provincia de: {provincia1}")

dni4 = 9216378
provincia2 = obtenerProvincia(personas, ciudades, dni4)
print(f"La persona con DNI {dni4} vive en la provincia de: {provincia2}")

# contarPoblacion
print("\nc) Función contarPoblacion:")
provincia_cordoba = "Córdoba"
cantidad = contarPoblacion(personas, ciudades, provincia_cordoba)
print(f"Cantidad de personas en {provincia_cordoba}: {cantidad}")

provincia_santafe = "Santa Fe"
cantidad2 = contarPoblacion(personas, ciudades, provincia_santafe)
print(f"Cantidad de personas en {provincia_santafe}: {cantidad2}")