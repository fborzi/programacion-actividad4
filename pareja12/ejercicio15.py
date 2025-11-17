from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

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

print(obtenerCiudad(personas, 26782345))  
print(obtenerCiudad(personas, 40173542))  
print(obtenerCiudad(personas, 99999999))  

print(obtenerProvincia(personas, ciudades, 26782345))  
print(obtenerProvincia(personas, ciudades, 40173542))  
print(obtenerProvincia(personas, ciudades, 9216378))   

print(contarPoblacion(personas, ciudades, "Córdoba"))       
print(contarPoblacion(personas, ciudades, "Santa Fe"))      
print(contarPoblacion(personas, ciudades, "Buenos Aires"))  
