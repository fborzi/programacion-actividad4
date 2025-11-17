#EJE17

# Crear conjunto con números del 1 al 10
numeros = set(range(1, 11))
print("Conjunto inicial (1 al 10):")
print(numeros)

# Añadir el 11 y el 12
numeros.add(11)
numeros.add(12)
print("\nDespués de añadir 11 y 12:")
print(numeros)

# Actualizar con números del 30 al 35
numeros.update(range(30, 36))
print("\nDespués de añadir números del 30 al 35:")
print(numeros)

# Agregar 232 y -264
numeros.add(232)
numeros.add(-264)
print("\nDespués de añadir 232 y -264:")
print(numeros)

# Informar primer y último número
print("\n" + "="*60)
print("NOTA: Los conjuntos (sets) NO tienen orden definido.")
print("No se puede obtener el 'primer' o 'último' elemento de forma confiable.")
print("Si necesitamos orden, debemos convertir a lista ordenada:")
numeros_ordenados = sorted(numeros)
print(f"\nNúmeros ordenados: {numeros_ordenados}")
print(f"Primer número (mínimo): {numeros_ordenados[0]}")
print(f"Último número (máximo): {numeros_ordenados[-1]}")

# Verificar pertenencia
print("\n" + "="*60)
print("Verificar pertenencia:")
print(f"¿El 7 pertenece al conjunto? {7 in numeros}")
print(f"¿El 20 pertenece al conjunto? {20 in numeros}")

# Cantidad de elementos
print("\n" + "="*60)
print(f"Cantidad de elementos almacenados: {len(numeros)}")
