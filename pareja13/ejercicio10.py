def borrar_adyacentes(lista):

#si la lista esta vacia
    if not lista:
        return[]

    #Comienza con el primer elemento
    nueva_lista = [lista[0]]

    #Recorre desde el segundo elemento de la lista
    for i in range(1,len(lista)):
        if lista[i] != lista[i - 1]:
            nueva_lista.append(lista[i])
            
    return nueva_lista

#ejemplo
print(borrar_adyacentes(["a","f","d","e","g","r","#","a","#"]))