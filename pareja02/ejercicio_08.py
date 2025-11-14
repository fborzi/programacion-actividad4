"""
EJERCICIO 8: Función dos mínimos
Implementar la función dos_minimos(lista) que retorna los dos valores menores.
"""

from funciones import dos_minimos

# Pruebas de la función
print("Pruebas de la función dos_minimos():\n")

# Ejemplo 1: Lista con varios elementos
lista1 = [23, 456, 12, 16, -4, 56]
resultado1 = dos_minimos(lista1)
print(f"dos_minimos({lista1})")
print(f"Resultado: {resultado1}\n")

# Ejemplo 2: Lista con un solo elemento
lista2 = [4]
resultado2 = dos_minimos(lista2)
print(f"dos_minimos({lista2})")
print(f"Resultado: {resultado2}\n")

# Ejemplo 3: Lista vacía
lista3 = []
resultado3 = dos_minimos(lista3)
print(f"dos_minimos({lista3})")
print(f"Resultado: {resultado3}\n")

# Ejemplo 4: Lista con dos elementos
lista4 = [100, 50]
resultado4 = dos_minimos(lista4)
print(f"dos_minimos({lista4})")
print(f"Resultado: {resultado4}")
