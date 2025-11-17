"""
Ejercicio 16: 
 Operaciones con conjuntos (sets)
 """

print("=== EJERCICIO 16: CONJUNTOS ===")
print()

# Creamos el conjunto con números del 1 al 10
# Usamos set() con range(1, 11) porque range no incluye el último número
numeros = set(range(1, 11))
print(f"1. Conjunto inicial (1 al 10): {numeros}")
print()

# Añadimos el 11 y el 12
numeros.add(11)
numeros.add(12)
print(f"2. Después de añadir 11 y 12: {numeros}")
print()

# Actualizamos incorporando números del 30 al 35
# Usamos update() con range para agregar múltiples elementos a la vez
numeros.update(range(30, 36))  # range(30, 36) genera [30, 31, 32, 33, 34, 35]
print(f"3. Después de añadir 30 al 35: {numeros}")
print()

# Agregamos 232 y -264
numeros.add(232)
numeros.add(-264)
print(f"4. Después de añadir 232 y -264: {numeros}")
print()

print("=" * 50)
print()

# a. Informar el primer y el último número almacenado
print("a) PRIMER Y ÚLTIMO NÚMERO:")
print("   IMPORTANTE: Los conjuntos NO tienen orden garantizado.")
print("   No existe concepto de 'primero' y 'último' en un conjunto.")
print(f"   Sin embargo, podemos convertirlo a lista ordenada:")

numeros_ordenados = sorted(numeros)
print(f"   Números ordenados: {numeros_ordenados}")
print(f"   Mínimo (primer número): {numeros_ordenados[0]}")
print(f"   Máximo (último número): {numeros_ordenados[-1]}")
print()

# También podemos usar min() y max() directamente
print(f"   O directamente: min = {min(numeros)}, max = {max(numeros)}")
print()

# b. Informar si el 7 y el 20 pertenecen al conjunto
print("b) PERTENENCIA AL CONJUNTO:")
print(f"   ¿El 7 pertenece al conjunto? {7 in numeros}")
print(f"   ¿El 20 pertenece al conjunto? {20 in numeros}")
print()

# c. Informar cuántos elementos hay almacenados
print("c) CANTIDAD DE ELEMENTOS:")
print(f"   Cantidad de elementos en el conjunto: {len(numeros)}")
print()

# === INFORMACIÓN ADICIONAL SOBRE CONJUNTOS ===
print("=" * 50)
print("INFORMACIÓN ADICIONAL SOBRE CONJUNTOS:")
print()
print("Características de los conjuntos (sets):")
print("  • No tienen orden (no se puede acceder por índice)")
print("  • No permiten elementos duplicados")
print("  • Son mutables (se pueden modificar)")
print("  • Son ideales para operaciones de pertenencia (in)")
print("  • Permiten operaciones matemáticas: unión, intersección, diferencia")
print()

# Demostración: los conjuntos no permiten duplicados
print("Demostración - No hay duplicados:")
conjunto_prueba = {1, 2, 2, 3, 3, 3, 4}
print(f"  {1, 2, 2, 3, 3, 3, 4} se convierte en: {conjunto_prueba}")