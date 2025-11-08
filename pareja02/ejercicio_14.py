"""
EJERCICIO 14: Función índice del mayor
Implementar la función indice_mayor(lista) que retorna el índice
donde se encuentra el mayor número.
"""

from funciones import indice_mayor

print("Pruebas de la función indice_mayor():\n")

# Ejemplo 1
lista1 = [6, 1, 7, 19, 2]
resultado1 = indice_mayor(lista1)
print(f"Lista: {lista1}")
print(f"Índice del mayor: {resultado1}")
print(f"Verificación: lista[{resultado1}] = {lista1[resultado1]}\n")

# Ejemplo 2
lista2 = [100, 50, 200, 75, 150]
resultado2 = indice_mayor(lista2)
print(f"Lista: {lista2}")
print(f"Índice del mayor: {resultado2}")
print(f"Verificación: lista[{resultado2}] = {lista2[resultado2]}\n")

# Ejemplo 3
lista3 = [-5, -10, -3, -8]
resultado3 = indice_mayor(lista3)
print(f"Lista: {lista3}")
print(f"Índice del mayor: {resultado3}")
print(f"Verificación: lista[{resultado3}] = {lista3[resultado3]}")
