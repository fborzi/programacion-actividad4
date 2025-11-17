def minimo_elemento(lista):
    if not lista:
        return None
    minimo = lista[0]
    for elemento in lista[1:]:
        if elemento < minimo:
            minimo = elemento
    return minimo

print(minimo_elemento([4, 8, 15, 16, 23, 42]))  
print(minimo_elemento("PYTHON"))                
