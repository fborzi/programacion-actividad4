"""Funcion EJERCICIO 6"""
def minimo_elemento(lista):
    """
    Recibe una lista de elementos comparables y devuelve
    el mínimo valor. Si la lista esta vacia, devuelve None.

    @params - numeros : int
    @return - int o string
    """

    if len(lista) == 0:
        return None
    
    minimo = lista[0]
    
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    
    return minimo