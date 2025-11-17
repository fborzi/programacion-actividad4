"""
EJERCICIO 12: Función ocurrencias
Implementar la función ocurrencias(lista) que retorna una lista con cada elemento
y el número de ocurrencias contiguas.
"""

from funciones import ocurrencias

print("Pruebas de la función ocurrencias():\n")

# Ejemplo 1
lista1 = ['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]
resultado1 = ocurrencias(lista1)
print(f"Lista original: {lista1}")
print(f"Resultado:      {resultado1}\n")

# Ejemplo 2
lista2 = [1, 1, 1, 2, 2, 3, 1, 1]
resultado2 = ocurrencias(lista2)
print(f"Lista original: {lista2}")
print(f"Resultado:      {resultado2}\n")

# Ejemplo 3: Sin repeticiones
lista3 = ['a', 'b', 'c', 'd']
resultado3 = ocurrencias(lista3)
print(f"Lista original: {lista3}")
print(f"Resultado:      {resultado3}\n")

# Ejemplo 4: Todos iguales
lista4 = [5, 5, 5, 5, 5]
resultado4 = ocurrencias(lista4)
print(f"Lista original: {lista4}")
print(f"Resultado:      {resultado4}")
