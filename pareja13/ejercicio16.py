# Crear el conjunto con los números del 1 al 10
numeros = set(range(1, 11))
print("Conjunto inicial:", numeros)

# Agregar el 11 y el 12
numeros.add(11)
numeros.add(12)
print("Después de agregar 11 y 12:", numeros)

# Incorporar los números del 30 al 35 sin hacerlo de a uno
numeros.update(range(30, 36))
print("Después de agregar del 30 al 35:", numeros)

# Agregar los números 232 y -264
numeros.update([232, -264])
print("Conjunto final:", numeros)

# Informar el primer y el último número (ordenamos para poder verlos)
ordenados = sorted(numeros)
print("Primer número:", ordenados[0])
print("Último número:", ordenados[-1])

# Verificar si el 7 y el 20 pertenecen al conjunto
print("¿Está el 7 en el conjunto?", 7 in numeros)
print("¿Está el 20 en el conjunto?", 20 in numeros)

# Cantidad total de elementos almacenados
print("Cantidad de elementos:", len(numeros))
