"""
EJERCICIO 6: Función mínimo elemento
Implementar la función minimo_elemento(lista) que retorna el mínimo valor
o None si la lista está vacía.
"""

from funciones import minimo_elemento

  # === PRUEBAS DE LA FUNCIÓN ===

# Prueba 1: Lista de números
resultado1 = minimo_elemento([4, 8, 15, 16, 23, 42])
print(f"minimo_elemento([4, 8, 15, 16, 23, 42]) = {resultado1}")

# Prueba 2: String (Python trata strings como listas de caracteres)
resultado2 = minimo_elemento("PYTHON")
print(f"minimo_elemento('PYTHON') = '{resultado2}'")

# Prueba 3: Lista vacía
resultado3 = minimo_elemento([])
print(f"minimo_elemento([]) = {resultado3}")

# Pruebas adicionales
print()
print("=== PRUEBAS ADICIONALES ===")

# Prueba con números negativos
resultado4 = minimo_elemento([-5, 10, -20, 3, 0])
print(f"minimo_elemento([-5, 10, -20, 3, 0]) = {resultado4}")

# Prueba con un solo elemento
resultado5 = minimo_elemento([42])
print(f"minimo_elemento([42]) = {resultado5}")

# Prueba con decimales
resultado6 = minimo_elemento([3.14, 2.71, 1.41, 9.99])
print(f"minimo_elemento([3.14, 2.71, 1.41, 9.99]) = {resultado6}")
