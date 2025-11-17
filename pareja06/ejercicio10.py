"""
EJERCICIO 10: Función borrar adyacentes
Implementar la función borrar_adyacentes(lista) que retorna una lista
con una única ocurrencia de caracteres adyacentes repetidos.
"""

from funciones import borrar_adyacentes

# === PRUEBAS DE LA FUNCIÓN ===

print("=== BORRAR CARACTERES ADYACENTES REPETIDOS ===")
print()

# Prueba 1: Ejemplo del enunciado
entrada1 = ['a', 'a', '*', 'b', '=', '=', 'c', 'a']
salida1 = borrar_adyacentes(entrada1)
print(f"Entrada:  {entrada1}")
print(f"Salida:   {salida1}")
print()

# Prueba 2: Múltiples repeticiones
entrada2 = ['x', 'x', 'x', 'y', 'z', 'z', 'z', 'z']
salida2 = borrar_adyacentes(entrada2)
print(f"Entrada:  {entrada2}")
print(f"Salida:   {salida2}")
print()

# Prueba 3: Sin repeticiones adyacentes
entrada3 = ['a', 'b', 'c', 'd']
salida3 = borrar_adyacentes(entrada3)
print(f"Entrada:  {entrada3}")
print(f"Salida:   {salida3}")
print()

# Prueba 4: Todos iguales
entrada4 = ['m', 'm', 'm', 'm', 'm']
salida4 = borrar_adyacentes(entrada4)
print(f"Entrada:  {entrada4}")
print(f"Salida:   {salida4}")
print()

# Prueba 5: Lista vacía
entrada5 = []
salida5 = borrar_adyacentes(entrada5)
print(f"Entrada:  {entrada5}")
print(f"Salida:   {salida5}")
print()

# Prueba 6: Un solo elemento
entrada6 = ['q']
salida6 = borrar_adyacentes(entrada6)
print(f"Entrada:  {entrada6}")
print(f"Salida:   {salida6}")
print()

# Prueba 7: Repeticiones no adyacentes (no se eliminan)
entrada7 = ['a', 'b', 'a', 'b', 'a']
salida7 = borrar_adyacentes(entrada7)
print(f"Entrada:  {entrada7}")
print(f"Salida:   {salida7}")
print(f"Nota: Las 'a' no se eliminan porque no son adyacentes")