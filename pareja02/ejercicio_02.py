"""
EJERCICIO 2: Determinar la posición de un elemento
Dada la lista b = [4, "palabra", [0, 1], 9.6, False]:
Determinar en qué posición (índice) se encuentra el elemento [0, 1]
"""

# Lista dada
b = [4, "palabra", [0, 1], 9.6, False]

# Elemento a buscar
elemento = [0, 1]

# Encontrar el índice
indice = b.index(elemento)

print("Lista b:", b)
print(f"\nEl elemento {elemento} se encuentra en el índice: {indice}")
print(f"Verificación: b[{indice}] = {b[indice]}")
