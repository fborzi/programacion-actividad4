
# EJERCICIO 8: Dos mínimos

def dos_minimos(lista):
    """
    Retorna los dos valores menores encontrados en la lista.
    
    Args:
        lista: Lista de elementos comparables
    
    Returns:
        Tupla con los dos menores valores (o None para elementos faltantes)
    
    Ejemplos:
        >>> dos_minimos([23, 456, 12, 16, -4, 56])
        (-4, 12)
        >>> dos_minimos([4])
        (4, None)
        >>> dos_minimos([])
        (None, None)
    """
    # Si la lista está vacía, retornamos dos None
    if len(lista) == 0:
        return (None, None)
    # Si la lista tiene un solo elemento, retornamos ese elemento y None
    elif len(lista) == 1:
        return (lista[0], None)
    # Si la lista tiene dos o más elementos
    else:
        # Ordenamos la lista de menor a mayor
        lista_ordenada = sorted(lista)
        # Retornamos el primer elemento (el menor) y el segundo (el segundo menor)
        return (lista_ordenada[0], lista_ordenada[1])

# EJERCICIO 10: Dígitos

def digitos(numero):
    """
    Retorna una lista con los dígitos que componen al número.
    
    Args:
        numero: Número entero
    
    Returns:
        Lista con los dígitos del número
    
    Ejemplo:
        >>> digitos(18413)
        [1, 8, 4, 1, 3]
    """
    # Convertimos el número a su valor absoluto (para manejar negativos),
    # luego a string, y finalmente cada carácter lo convertimos a entero
    # usando list comprehension
    return [int(d) for d in str(abs(numero))]



# EJERCICIO 12: Ocurrencias
def ocurrencias(lista):
    """
    Retorna una lista con cada elemento y su número de ocurrencias contiguas.
    
    Args:
        lista: Lista de elementos
    
    Returns:
        Lista de listas [elemento, cantidad]
    
    Ejemplo:
        >>> ocurrencias(['z', 7, True, True, 34, 'z', 'z', 'z', 3.14])
        [['z', 1], [7, 1], [True, 2], [34, 1], ['z', 3], [3.14, 1]]
    """
    # Si la lista está vacía, retornamos una lista vacía
    if not lista:
        return []
    
    # Inicializamos la lista de resultados
    resultado = []
    # Guardamos el primer elemento como el elemento actual
    elemento_actual = lista[0]
    # Inicializamos el contador en 1
    contador = 1
    
    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(lista)):
        # Si el elemento actual es igual al anterior
        if lista[i] == elemento_actual:
            # Incrementamos el contador
            contador += 1
        else:
            # Si es diferente, agregamos el elemento y su contador al resultado
            resultado.append([elemento_actual, contador])
            # Actualizamos el elemento actual
            elemento_actual = lista[i]
            # Reiniciamos el contador
            contador = 1
    
    # Agregamos el último elemento y su contador
    resultado.append([elemento_actual, contador])
    return resultado





# EJERCICIO 14: Índice del mayor

def indice_mayor(lista):
    """
    Retorna el índice donde se encuentra el mayor número de la lista.
    
    Args:
        lista: Lista de números
    
    Returns:
        Índice del elemento mayor
    
    Ejemplo:
        >>> indice_mayor([6, 1, 7, 19, 2])
        3
    """
    # Si la lista está vacía, retornamos None
    if not lista:
        return None
    # Encontramos el valor máximo con max() y luego buscamos su índice con index()
    return lista.index(max(lista))

# EJERCICIO 16: Ciudades y personas

def obtenerCiudad(personas, DNI):
    """
    Retorna la ciudad donde vive una persona dado su DNI.
    
    Args:
        personas: Lista de [nombre, DNI, ciudad]
        DNI: DNI de la persona a buscar
    
    Returns:
        Nombre de la ciudad o None si no se encuentra
    """
    # Recorremos la lista de personas
    for persona in personas:
        # Si el DNI coincide (persona[1] es el DNI)
        if persona[1] == DNI:
            # Retornamos la ciudad (persona[2] es la ciudad)
            return persona[2]
    # Si no encontramos la persona, retornamos None
    return None


def obtenerProvincia(personas, ciudades, DNI):
    """
    Retorna la provincia donde vive una persona dado su DNI.
    
    Args:
        personas: Lista de [nombre, DNI, ciudad]
        ciudades: Lista de [ciudad, provincia]
        DNI: DNI de la persona a buscar
    
    Returns:
        Nombre de la provincia o None si no se encuentra
    """
    # Primero obtenemos la ciudad de la persona
    ciudad = obtenerCiudad(personas, DNI)
    # Si no se encontró la ciudad, retornamos None
    if ciudad is None:
        return None
    
    # Buscamos la provincia correspondiente a esa ciudad
    for c in ciudades:
        # Si el nombre de la ciudad coincide (c[0] es la ciudad)
        if c[0] == ciudad:
            # Retornamos la provincia (c[1] es la provincia)
            return c[1]
    # Si no encontramos la provincia, retornamos None
    return None


def contarPoblacion(personas, ciudades, provincia):
    """
    Cuenta cuántas personas viven en una provincia.
    
    Args:
        personas: Lista de [nombre, DNI, ciudad]
        ciudades: Lista de [ciudad, provincia]
        provincia: Nombre de la provincia
    
    Returns:
        Cantidad de personas en la provincia
    """
    # Inicializamos el contador en 0
    contador = 0
    # Recorremos todas las personas
    for persona in personas:
        # Obtenemos la provincia de cada persona usando su DNI
        prov = obtenerProvincia(personas, ciudades, persona[1])
        # Si la provincia coincide con la que buscamos
        if prov == provincia:
            # Incrementamos el contador
            contador += 1
    # Retornamos el total de personas en la provincia
    return contador

# EJERCICIO 22: Análisis de texto multilínea

def tiene_n_vocales_diferentes(palabra, n):
    """
    Verifica si una palabra tiene al menos n vocales diferentes.
    
    Args:
        palabra: String con la palabra
        n: Número mínimo de vocales diferentes
    
    Returns:
        True si cumple la condición, False en caso contrario
    """
    # Definimos un conjunto con todas las vocales (con y sin acento)
    vocales = set('aeiouáéíóúAEIOUÁÉÍÓÚ')
    # Creamos un conjunto vacío para almacenar las vocales únicas encontradas
    vocales_palabra = set()
    
    # Recorremos cada carácter de la palabra
    for c in palabra:
        # Si el carácter es una vocal
        if c in vocales:
            # Normalizamos las vocales con acento a su versión sin acento
            if c in 'áÁ':
                vocales_palabra.add('a')
            elif c in 'éÉ':
                vocales_palabra.add('e')
            elif c in 'íÍ':
                vocales_palabra.add('i')
            elif c in 'óÓ':
                vocales_palabra.add('o')
            elif c in 'úÚ':
                vocales_palabra.add('u')
            else:
                # Si no tiene acento, la agregamos en minúscula
                vocales_palabra.add(c.lower())
    
    # Verificamos si la cantidad de vocales diferentes es mayor o igual a n
    return len(vocales_palabra) >= n


def contar_oraciones(texto):
    """
    Cuenta la cantidad de oraciones en un texto.
    
    Args:
        texto: String con el texto
    
    Returns:
        Cantidad de oraciones (terminadas en punto)
    """
    # Contamos la cantidad de puntos en el texto (cada punto indica una oración)
    return texto.count('.')


def palabras_por_oracion(oracion):
    """
    Cuenta las palabras en una oración.
    
    Args:
        oracion: String con la oración
    
    Returns:
        Cantidad de palabras
    """
    # Dividimos la oración por espacios y contamos los elementos resultantes
    return len(oracion.split())

# EJERCICIO 26: Frecuencia de caracteres

def frecuencia_caracteres(cadena):
    """
    Retorna la frecuencia de cada carácter en la cadena.
    
    Args:
        cadena: String a analizar
    
    Returns:
        Diccionario con caracteres como claves y frecuencias como valores
    """
    # Inicializamos un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    # Recorremos cada carácter de la cadena
    for caracter in cadena:
        # Si el carácter ya está en el diccionario
        if caracter in frecuencias:
            # Incrementamos su contador
            frecuencias[caracter] += 1
        else:
            # Si es la primera vez que aparece, lo inicializamos en 1
            frecuencias[caracter] = 1
    # Retornamos el diccionario con las frecuencias
    return frecuencias
