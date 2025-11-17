'''Dadas dos listas, una con datos de ciudades y otra con datos de personas, con el siguiente formato:
- La lista de ciudades contiene listas con nombres de ciudades y la provincia a la que pertenecen.
Ejemplo:
[ ["Rosario","Santa Fe"], ["Carlos Paz","Córdoba"], ["Balcarce","Buenos Aires"], ["Cosquín","Córdoba"] ]
- La lista de personas contiene listas con nombre, DNI y ciudad de cada persona.
Ejemplo:
[ ["Juan Perez",26782345,"Carlos Paz"], ["María Gomez",40173542,"Rosario"], ["Ana Ríos",9216378,"Cosquín"] ]
a. Escribir la función obtenerCiudad(personas, DNI) que, dada la lista de personas y el DNI de una persona, retorne la ciudad donde vive.
b. Escribir la función obtenerProvincia(personas, ciudades, DNI) que, dadas las dos listas y el DNI de una persona retorne la provincia donde vive. Utilizar la función del inciso a.
c. Escribir la función contarPoblacion(personas, ciudades, provincia) que, dadas las dos listas y una provincia, informe cuántas personas viven en esa provincia. Utilizar la función del inciso b.'''
from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion
ciudades=[
    ["Rosario","Santa Fe"],
    ["Carlos Paz","Cordoba"],
    ["Balcarce","Buenos Aires"],
    ["Cosquin","Cordoba"]
]
personas=[["Juan Perez",26782345,"Carlos Paz"],
          ["Maria Gomez",40173542,"Rosario"],
          ["Ana Rios",9216378,"Cosquin"]  
]
 
print(obtenerCiudad(personas, 40173542))
print(obtenerProvincia(personas, ciudades, 9216378))
print(contarPoblacion(personas, ciudades, "Cordoba"))



