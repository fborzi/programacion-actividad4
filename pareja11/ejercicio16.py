numeros = set(range(1, 11))

numeros.update([11, 12])

numeros.update(range(30,36))

numeros.update([232, -264])


# a)
ordenados = sorted(numeros)

primer = ordenados[0]

ultimo = ordenados[-1]

print(f"Primer numero: {primer}, ultimo numero : {ultimo}")

# b)
print("7 pertenece al conjunto?", 7 in numeros)
print("20 pertenece al conjunto?", 20 in numeros)
