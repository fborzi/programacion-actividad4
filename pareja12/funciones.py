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
def piedra_papel_tijera(uno, dos):
    """
    Determina el ganador del juego piedra, papel o tijeras.
    @params - uno : string - eleccion del jugador 1('piedra', 'papel' o 'tijeras')
    @params - dos: string - eleccion del jugador 2('piedra', 'papel' o 'tijeras') 
    @return: int - 1 si gana el jugador 1, 2 si gana el jugador 2, 0 si hay empate
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

"""FUNCION EJERCICIO 10"""
def borrar_adyacentes(lista):
    """
    Recibe una lista de caracteres y retorna una lista donde queda una única
    ocurrencia de todos los caracteres adyacentes repetidos.
    @params - lista: list -lista de caracteres (string de 1 longitud)
    @return: list - lista sin caracteres repetidos
    """

    if len(lista) == 0:
        return[]
    
    resultado = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] != lista[i-1]:
            resultado.append(lista[i])
    
    return resultado

