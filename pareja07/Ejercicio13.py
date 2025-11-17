def indice_mayor(lista):
    if not lista:
        return None
    mayor = lista[0]
    indice = 0
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    return indice

print(indice_mayor([6, 1, 7, 19, 2]))  
