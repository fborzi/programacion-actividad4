numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.add(11)
numeros.add(12)

numeros.update(range(30,36))

numeros.update([232, -264])

numeros = list(numeros)
primero = numeros[0]
ultimo = numeros[-1]

print("a)")
print(f"Primer número: {primero}")
print(f"Último número: {ultimo}")

print("b)")
print(f"Pertenencia del numero 7: {7 in numeros}")
print(f"Pertenencia del numero 20: {20 in numeros}")

print(f"c) Cantidad de elementos: {len(numeros)}")