def dos_sumandos(lista,resultado):

    #recorre la lista con dos indices diferentes
    for i in range(len(lista)):
        for j in range( i + 1,len(lista)): #evita usar dos veces el mismo numero 
            if lista[i] + lista[j] == resultado:
                return[i,j] #devulve los indices cuando encuentra la suma
    
    # si no hay combinacion posible
    return []
#ejemplo
print(dos_sumandos([2, 7, 11, 15], 17))


