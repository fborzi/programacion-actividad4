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

"""FUNCION EJERCICOIO 8"""
def pieda_papel_tijera(uno, dos):
    """
    Determia el ganador del juego piedra, papel o tijeras.
    @params - string: cadena de caracteres
    @return: int
    """

    uno = uno.lower()
    dos = dos.lower()

    if uno == dos:
        return 0
    
    if ((uno == 'piedra' and dos == 'tijera') or
        (uno == 'tijera' and dos == ' papel') or
        (uno == 'papel' and dos == 'piedra')):
        return 1
    
    return 2