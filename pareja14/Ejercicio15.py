from Funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

# Datos de ejemplo
ciudades = [["Rosario","Santa Fe"], ["Carlos Paz","Córdoba"], ["Balcarce","Buenos Aires"], ["Cosquín","Córdoba"]]
personas = [["Juan Perez",26782345,"Carlos Paz"], ["María Gomez",40173542,"Rosario"], ["Ana Ríos",9216378,"Cosquín"]]

# Pruebas
print(obtenerCiudad(personas, 26782345))  # Output: "Carlos Paz"
print(obtenerProvincia(personas, ciudades, 26782345))  # Output: "Córdoba"
print(contarPoblacion(personas, ciudades, "Córdoba"))  # Output: 2