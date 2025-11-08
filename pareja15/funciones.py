def dos_minimos(lista):
    """Retorna los dos valores menores de la lista"""
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        lista_ordenada = sorted(lista)
        return (lista_ordenada[0], lista_ordenada[1])
