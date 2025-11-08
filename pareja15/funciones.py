def dos_minimos(lista):
    """Retorna los dos valores menores de la lista"""
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        lista_ordenada = sorted(lista)
        return (lista_ordenada[0], lista_ordenada[1])

def digitos(numero):
    """Retorna la lista con los dígitos que forman al número"""
    return [int(d) for d in str(abs(numero))]

def ocurrencias(lista):
    """Retorna la lista con cada elemento y su número de ocurrencias contiguas"""
    if not lista:
        return []
    
    resultado = []
    elemento_actual = lista[0]
    contador = 1
    
    for i in range(1, len(lista)):
        if lista[i] == elemento_actual:
            contador += 1
        else:
            resultado.append([elemento_actual, contador])
            elemento_actual = lista[i]
            contador = 1
    
    resultado.append([elemento_actual, contador])
    return resultado