"""
EJERCICIO 10
Escribí la función borrar_adyacentes(lista) que recibe una lista donde sus 
elementos son caracteres (strings de longitud 1) y retorna una lista en la 
que queda una única ocurrencia de todos los caracteres adyacentes repetidos. 

Ejemplo: borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a']) 
retornará ['a', '*', 'b', '=', 'c', 'a'].
"""

from funciones import borrar_adyacentes

# Ejemplo 1
lista1 = ['a', 'a', '*', 'b', '=', '=', 'c', 'a']
resultado1 = borrar_adyacentes(lista1)
print("Original:", lista1)
print("Resultado:", resultado1)
print()

# Ejemplo 2
lista2 = ['x', 'x', 'x', 'y', 'z', 'z']
resultado2 = borrar_adyacentes(lista2)
print("Original:", lista2)
print("Resultado:", resultado2)
print()

# Ejemplo 3
lista3 = ['a', 'b', 'c', 'd']
resultado3 = borrar_adyacentes(lista3)
print("Original:", lista3)
print("Resultado:", resultado3)
print()

# Ejemplo 4
lista4 = []
resultado4 = borrar_adyacentes(lista4)
print("Original:", lista4)
print("Resultado:", resultado4)