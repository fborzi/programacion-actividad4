# ejercicio15.py

from Funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

# Datos de ejemplo
ciudades = [
    ["Rosario", "Santa Fe"],
    ["MDQ", "Buenos Aires"],
    ["Rojas", "Buenos Aires"],
    ["Cosquín", "Córdoba"]
]

personas = [
    ["Juan Perez", 26782345, "Buenos Aires"],
    ["María Gomez", 40173542, "Rosario"],
    ["Ana Ríos", 9216378, "Cosquín"],
    ["Pedro Luna", 45678123, "Cosquín"]
]

# Pruebas
print(obtenerCiudad(personas, 26782345))              
print(obtenerProvincia(personas, ciudades, 40173542))  
print(contarPoblacion(personas, ciudades, "Córdoba"))  
