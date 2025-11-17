
numeros = set(range(1, 11))


numeros.add(11)
numeros.add(12)


numeros.update(range(30, 36))


numeros.update([232, -264])

print("Conjunto:", numeros)



print("Primer número (mínimo):", min(numeros))
print("Último número (máximo):", max(numeros))


print("¿7 pertenece al conjunto?", 7 in numeros)
print("¿20 pertenece al conjunto?", 20 in numeros)


print("Cantidad de elementos:", len(numeros))
