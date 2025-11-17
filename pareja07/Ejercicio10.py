def borrar_adyacentes(lista):
    if not lista:
        return []
    
    resultado = [lista[0]]
    for elem in lista[1:]:
        if elem != resultado[-1]:
            resultado.append(elem)
    return resultado

print(borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a']))

