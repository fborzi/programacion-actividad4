def dos_sumandos(lista, resultado):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None

print(dos_sumandos([2, 7, 11, 15], 17))

