def indice_mayor(lista):
    #devulve el indice del elemento mas grande de la lista
    
    #si la lista esta vacia, no tiene indice
    if not lista:
        return None
    
    mayor = lista[0]
    indice = 0

    for i in range(1,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i 
    return indice
print(indice_mayor(["6","2","1","20"]))