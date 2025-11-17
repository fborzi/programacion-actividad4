def ocurrencias(lista):
    if not lista:
        return []
    
    resultado = []
    actual = lista[0]
    contador = 1

    for elem in lista[1:]:
        if elem == actual:
            contador += 1
        else:
            resultado.append([actual, contador])
            actual = elem
            contador = 1
    
    resultado.append([actual, contador])
    return resultado

print(ocurrencias(['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]))

