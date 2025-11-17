# EJE7
def minimo_elemento(lista):
    """Retorna el mínimo valor encontrado en la lista o None si está vacía."""
    if not lista:
        return None
    return min(lista)


# EJE8
def dos_minimos(lista):
    """Retorna los dos valores menores encontrados en la lista"""
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        lista_ordenada = sorted(lista)
        return (lista_ordenada[0], lista_ordenada[1])


# EJE9
def piedra_papel_tijera(uno, dos):
    """Determina el ganador del juego piedra, papel o tijera."""
    uno = uno.lower()
    dos = dos.lower()
    
    if uno == dos:
        return 0
    elif (uno == 'piedra' and dos == 'tijera') or \
         (uno == 'tijera' and dos == 'papel') or \
         (uno == 'papel' and dos == 'piedra'):
        return 1
    else:
        return 2


# EJE10
def digitos(numero):
    """Retorna una lista con los dígitos que componen al número"""
    return [int(d) for d in str(abs(numero))]


# EJE11
def borrar_adyacentes(lista):
    """Retorna una lista con una única ocurrencia de caracteres adyacentes repetidos"""
    if not lista:
        return []
    
    resultado = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] != lista[i-1]:
            resultado.append(lista[i])
    
    return resultado


# EJE12
def ocurrencias(lista):
    """Retorna una lista con cada elemento y su número de ocurrencias contiguas"""
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


# EJE13
def suma_digitos(n):
    """Retorna la suma de los dígitos de un número entero"""
    return sum(digitos(n))


def sumatoria_digitos(lista):
    """Retorna una lista con la suma de los dígitos de cada número"""
    return [suma_digitos(n) for n in lista]


# EJE14
def indice_mayor(lista):
    """Retorna el índice donde se encuentra el mayor número de la lista"""
    if not lista:
        return None
    return lista.index(max(lista))


# EJE15
def dos_sumandos(lista, resultado):
    """Retorna los índices de dos elementos cuya suma da el resultado esperado"""
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None


# EJE16
def obtenerCiudad(personas, DNI):
    """Retorna la ciudad donde vive una persona dado su DNI"""
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None


def obtenerProvincia(personas, ciudades, DNI):
    """Retorna la provincia donde vive una persona dado su DNI"""
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None
    
    for c in ciudades:
        if c[0] == ciudad:
            return c[1]
    return None


def contarPoblacion(personas, ciudades, provincia):
    """Cuenta cuántas personas viven en una provincia"""
    contador = 0
    for persona in personas:
        prov = obtenerProvincia(personas, ciudades, persona[1])
        if prov == provincia:
            contador += 1
    return contador


# EJE19
def digitos_repetidos(n):
    """Retorna una lista con los dígitos que se repiten en n"""
    digitos_lista = digitos(n)
    repetidos = set()
    vistos = set()
    
    for d in digitos_lista:
        if d in vistos:
            repetidos.add(d)
        else:
            vistos.add(d)
    
    return list(repetidos)


def tiene_digitos_repetidos(n):
    """Verifica si un número tiene dígitos repetidos."""
    digitos_lista = digitos(n)
    return len(digitos_lista) != len(set(digitos_lista))


def suma_digitos_repetidos(n):
    """Retorna la suma de los dígitos que se repiten en n"""
    repetidos = digitos_repetidos(n)
    return sum(repetidos)


def cantidad_digitos_repetidos(n):
    """Retorna la cantidad de dígitos diferentes que se repiten en n"""
    return len(digitos_repetidos(n))


# EJE21
def contar_palabras(texto):
    """Cuenta la cantidad de palabras en un texto."""
    return len(texto.split())


def letras_repetidas_palabra(palabra):
    """Retorna las letras que se repiten en una palabra."""
    palabra = palabra.lower()
    letras = [c for c in palabra if c.isalpha()]
    repetidas = set()
    vistas = set()
    
    for letra in letras:
        if letra in vistas:
            repetidas.add(letra)
        else:
            vistas.add(letra)
    
    return repetidas


# EJE22
def tiene_n_vocales_diferentes(palabra, n):
    """Verifica si una palabra tiene al menos n vocales diferentes"""
    vocales = set('aeiouáéíóúAEIOUÁÉÍÓÚ')
    vocales_palabra = set()
    
    for c in palabra:
        if c in vocales:
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
                vocales_palabra.add(c.lower())
    
    return len(vocales_palabra) >= n


def contar_oraciones(texto):
    """Cuenta la cantidad de oraciones en un texto (por puntos)."""
    return texto.count('.')


def palabras_por_oracion(oracion):
    """Cuenta la cantidad de palabras en una oración."""
    return len(oracion.split())


# EJE26
def frecuencia_caracteres(cadena):
    """Retorna la frecuencia de cada carácter en la cadena"""
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias


# EJE30
def siguiente_mira_y_deci(numero):
    """Genera el siguiente número en la sucesión mira y deci."""
    cadena = str(numero)
    resultado = ""
    i = 0
    
    while i < len(cadena):
        digito = cadena[i]
        contador = 1
        
        while i + contador < len(cadena) and cadena[i + contador] == digito:
            contador += 1
        
        resultado += str(contador) + digito
        i += contador
    
    return int(resultado)


def sucesion_mira_y_deci(n):
    """Calcula los primeros n números de la sucesión mira y deci."""
    if n <= 0:
        return []
    
    sucesion = [1]
    for i in range(1, n):
        sucesion.append(siguiente_mira_y_deci(sucesion[-1]))
    
    return sucesion
