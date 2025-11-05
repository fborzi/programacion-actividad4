#---------------------------------------------------------------------------------------#
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
#---------------------------------------------------------------------------------------#
"""FUNCION 7"""
def dos_minimos(lista):
    """
    Devuelve los dos valores menores de una lista.
    Si hay menos de dos elementos, completa con None.
    
    Args:
        lista: Lista de elementos comparables
        
    Returns:
        Tupla con los dos menores valores (o None si faltan elementos)
    """
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        # Ordenar la lista y tomar los dos primeros elementos
        lista_ordenada = sorted(lista)
        return (lista_ordenada[0], lista_ordenada[1])


# Ejemplos de uso
print(dos_minimos([23, 456, 12, 16, -4, 56]))  # (-4, 12)
print(dos_minimos([4]))                         # (4, None)
print(dos_minimos([]))                          # (None, None)
#---------------------------------------------------------------------------------------#
"""FUNCION EJERCICIO 8"""
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
#---------------------------------------------------------------------------------------#
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
#---------------------------------------------------------------------------------------#
"""FUNCION 11"""


#---------------------------------------------------------------------------------------#
"""FUNCION EJERCICIO 12"""
def suma_digitos(n):
    """
    Dado un número entero positivo, retorna la suma de sus dígitos.
    @params - n: int - numero entero positivo
    @return: int - suma de los digitos del numero
    """
    suma = 0

    while n > 0:
        digito = n % 10
        suma = suma + digito
        n = n // 10
    return suma

def sumatoria_digitos(lista):
    """
    Dada una lista de numeros enteros positivos, retorna una lista con 
    la suma de los dígitos de cada uno de los números.
    @params - int: numeros enteros positivos
    @return - int: numeros enteros positivos
    """
    resultado = []

    for numero in lista:
        suma = suma_digitos(numero)
        resultado.append(suma)
    return resultado
#---------------------------------------------------------------------------------------#
"""FUNCIONES EJERCICIO 14"""
def dos_sumando(lista, resultado):
    """
    Dada una lista de numeros y un resultado, retorna los índices de dos
    elementos de la lista que sumados dan como resultado el número indicado.
    @params - lista: list - lista de numeros
    @params - resultado: int - numero objetivo de la suma
    @return: list - lista de dos indices
    """

    for i in range(len(lista)):
        for j in range (i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i,j]
            
    return[]
#---------------------------------------------------------------------------------------#
"""FUNCION 18"""
def digitos_repetidos(n):
    """
    Dado un número n, retorna una lista con los dígitos que se repiten en n.
    Cada dígito aparece una única vez en la lista.
    @params - n: int - numero entero
    @return: list - lista con los dígitos repetidos
    """

    numero_str = str(n)

    contador = {}

    for digito in numero_str:
        if digito in contador:
            contador[digito] = contador[digito] + 1
        else: 
            contador[digito] = 1

    repetidos = []

    for digito in contador:
        if contador[digito] > 1:
            repetidos.append(int(digito))

    return repetidos