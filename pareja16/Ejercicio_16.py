# Crear el conjunto con los números del 1 al 10
numeros = set(range(1, 11))
print("Conjunto inicial:", numeros)

# Agregar el 11 y el 12
numeros.add(11)
numeros.add(12)

# Incorporar los números del 30 al 35 (sin hacerlo uno por uno)
numeros.update(range(30, 36))

# Agregar 232 y -264
numeros.add(232)
numeros.add(-264)

# Informar primer y último número (para esto conviene ordenar el conjunto)
numeros_ordenados = sorted(numeros)
print("Primer número:", numeros_ordenados[0])
print("Último número:", numeros_ordenados[-1])

# Verificar pertenencia de 7 y 20
print("¿7 está en el conjunto?", 7 in numeros)
print("¿20 está en el conjunto?", 20 in numeros)

# Informar cantidad de elementos
print("Cantidad de elementos almacenados:", len(numeros))

