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
"""FUNCION EJERCICIO 9"""
def digitos(numero):
    """Versión usando operaciones matemáticas"""
    numero = abs(numero)  # Manejamos números negativos
    
    if numero == 0:
        return [0]
    
    resultado = []
    while numero > 0:
        resultado.insert(0, numero % 10)  # Extraemos el último dígito
        numero //= 10  # Removemos el último dígito
    
    return resultado
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
def ocurrencias(lista):
    """
    Retorna una lista con cada elemento y sus ocurrencias contiguas.
    
    Args:
        lista: lista con elementos de cualquier tipo
    
    Returns:
        lista de listas [elemento, cantidad_contigua]
    """
    if not lista:  
        return []
    
    resultado = []
    elemento_actual = lista[0]
    contador = 1
    
    for i in range(1, len(lista)):
        if lista[i] == elemento_actual:
            contador += 1
        else:
            resultado.append([elemento_actual, contador])
            elemento_actual = lista[i]
            contador = 1
    
    resultado.append([elemento_actual, contador])
    
    return resultado

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
"""FUNCION EJERCICIO 13"""
def indice_mayor(lista):
    """
    Retorna el índice donde se encuentra el mayor número de la lista.
    
    Args:
        lista: lista de números
    
    Returns:
        índice del mayor elemento
    """
    if not lista: 
        return None
    
    indice_max = 0
    valor_max = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] > valor_max:
            valor_max = lista[i]
            indice_max = i
    
    return indice_max

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
"""FUNCION EJERCICIO 15"""
def obtenerCiudad(personas, DNI):
    """
    Retorna la ciudad donde vive la persona con el DNI dado.
    
    Args:
        personas: lista de personas [nombre, DNI, ciudad]
        DNI: DNI a buscar
    
    Returns:
        nombre de la ciudad o None si no se encuentra
    """
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None


def obtenerProvincia(personas, ciudades, DNI):
    """
    Retorna la provincia donde vive la persona con el DNI dado.
    
    Args:
        personas: lista de personas [nombre, DNI, ciudad]
        ciudades: lista de ciudades [ciudad, provincia]
        DNI: DNI a buscar
    
    Returns:
        nombre de la provincia o None si no se encuentra
    """
    ciudad = obtenerCiudad(personas, DNI)
    
    if ciudad is None:
        return None
    
    for ciudad_info in ciudades:
        if ciudad_info[0] == ciudad:
            return ciudad_info[1]
    
    return None


def contarPoblacion(personas, ciudades, provincia):
    """
    Cuenta cuántas personas viven en la provincia dada.
    
    Args:
        personas: lista de personas [nombre, DNI, ciudad]
        ciudades: lista de ciudades [ciudad, provincia]
        provincia: nombre de la provincia
    
    Returns:
        cantidad de personas en esa provincia
    """
    contador = 0
    
    for persona in personas:
        DNI = persona[1]
        provincia_persona = obtenerProvincia(personas, ciudades, DNI)
        
        if provincia_persona == provincia:
            contador += 1
    
    return contador
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
#---------------------------------------------------------------------------------------#
"""FUNCION EJERCICIO 25"""
def frecuencia_caracteres(cadena):
    """
    retorna un diccionario con la frecuencia de cada caracter en la cadena.
    @params: cadena - String con el texto a analizar
    @returns: diccionario donde la clave son los caracteres y los valores son sus frecuencias.
    """
    frecuencia = {}

    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1

    return frecuencia
#---------------------------------------------------------------------------------------#
