#desde ejercicio 6 importamos la funcion minimo elemento
from ejercicio6 import minimo_elemento

def dos_min(lista):

#devuelve los dos valores minimos de una lista.

    if len(lista) ==0:
        return(None)
    
    if len(lista) == 1:
        return (lista[0],None)
    
    #buscar el primer minimo
    primero=minimo_elemento(lista)

    lista_sin_min = lista.copy()
    lista_sin_min.remove(primero)

    #buscar el segundo minimo
    segundo=minimo_elemento(lista_sin_min)
    
    #devolver ambos valores
    return(primero,segundo)

print(dos_min([23, 456, 12, 16, -4, 56]))  # (-4, 12)
print(dos_min([4]))                        # (4, None)
print(dos_min([]))                         # (None, None)
