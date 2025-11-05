def borrar_adyacentes(lista):
    if not lista:  
        return []

    resultado = [lista[0]]  

    for elemento in lista[1:]:
        if elemento != resultado[-1]: 
            resultado.append(elemento)

    return resultado
print(borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a']))
# → ['a', '*', 'b', '=', 'c', 'a']
