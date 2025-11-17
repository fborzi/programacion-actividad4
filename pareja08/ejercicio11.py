'''Escribí la función ocurrencias(lista) que recibe una lista y retorna una lista que contiene listas formadas por cada elemento de la lista junto con el número de ocurrencias contiguas de ese elemento en la lista, con el orden en que fueron apareciendo.
Ejemplo: ocurrencias(['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]) retornará [['z', 1], [7, 1], [True, 2], [34, 1], ['z', 3], [3.14, 1]]'''

from funciones import ocurrencias
lista=['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]

print(ocurrencias(lista))
