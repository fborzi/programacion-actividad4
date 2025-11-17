def minimo_elemento(lista):
    #devuelve el valor minimo de una lista

    #Si la lista esta vacia devuelve None
    if len(lista) == 0:
     return None
    #toma el primer elemento minimo
    minimo = lista [0]
    #recorre el resto de los elementos para encontrar el menor
    for elemento in lista [1:]:
        if elemento < minimo:
           minimo = elemento
    #devuelve el valor minimo que se encontro       
    return minimo 