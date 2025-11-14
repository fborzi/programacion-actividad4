#Ejercicio16
"""Crea un conjunto de números enteros del 1 al 10. Agrega los números 11 y 12 al conjunto.
Luego, agrega los números del 30 al 35 utilizando un rango. Finalmente, agrega los números 232 y -264 al conjunto.
Después de realizar estas operaciones, imprime el conjunto completo, el número mínimo y máximo del conjunto,"""
numeros = set(range(1, 11))
numeros.add(11)
numeros.add(12)
numeros.update(range(30, 36))
numeros.update([232, -264])

print("Primer número (menor):", min(numeros))
print("Último número (mayor):", max(numeros))
print("¿El 7 está en el conjunto?", 7 in numeros)
print("¿El 20 está en el conjunto?", 20 in numeros)
print("Cantidad de elementos en el conjunto:", len(numeros))

