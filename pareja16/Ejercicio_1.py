
b = [4, "palabra", [0, 1], 9.6, False]

# Verificar si los elementos pertenecen a la lista
elementos = [9.6, 0, False, [0, 1], 4.0, "p"]

for e in elementos:

    if e in b:
        print(e, "sí pertenece a la lista.")
    else:
        print(e, "no pertenece a la lista.")

# Obtener el índice del elemento [0, 1]


indice = b.index([0, 1])
print("El índice de [0, 1] es:", indice)


