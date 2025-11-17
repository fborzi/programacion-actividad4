"""
 Ejercicio 2:
 Dada la lista L = [5, 6, [9, 5], 2, 5]:
 Contar cuántas veces aparece el elemento 5 en la lista L
 """

# Definimos la lista L según el enunciado
L = [5, 6, [9, 5], 2, 5]

# Elemento a contar
elemento = 5

# Utilizamos el método count() para contar las apariciones del elemento 5
# IMPORTANTE: count() solo cuenta elementos en el primer nivel de la lista
# No cuenta elementos dentro de listas anidadas
cantidad = L.count(5)

# Mostramos el resultado
print(f"La lista L es: {L}")
print(f"\nEl elemento 5 aparece: {cantidad} veces en la lista L")
print("\nNota: El 5 dentro de [9, 5] NO se cuenta porque está dentro de otra lista")
