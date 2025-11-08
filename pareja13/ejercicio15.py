# Ejemplo
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

# Pruebas
print(obtenerCiudad(personas, 40173542))             # Debería mostrar: Rosario
print(obtenerProvincia(personas, ciudades, 40173542))  # Debería mostrar: Santa Fe
print(contarPoblacion(personas, ciudades, "Córdoba"))  # Debería mostrar: 2

