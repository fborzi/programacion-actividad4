def dos_minimos(lista):
    """Retorna los dos valores menores de la lista"""
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        lista_ordenada = sorted(lista)
        return (lista_ordenada[0], lista_ordenada[1])

def digitos(numero):
    """Retorna la lista con los dígitos que forman al número"""
    return [int(d) for d in str(abs(numero))]

def ocurrencias(lista):
    """Retorna la lista con cada elemento y su número de ocurrencias contiguas"""
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

def indice_mayor(lista):
    """Retorna el índice donde se encuentra el mayor número de la lista"""
    if not lista:
        return None
    return lista.index(max(lista))

def obtenerCiudad(personas, DNI):
    """Retorna la ciudad donde vive una persona según lo que dice su DNI"""
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None

def obtenerProvincia(personas, ciudades, DNI):
    """Retorna la provincia donde vive una persona según lo que dice su DNI"""
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None
    
    for ciudad_info in ciudades:
        if ciudad_info[0] == ciudad:
            return ciudad_info[1]
    return None


def contarPoblacion(personas, ciudades, provincia):
    """Cuenta cuántas personas viven en una provincia"""
    contador = 0
    for persona in personas:
        dni = persona[1]
        if obtenerProvincia(personas, ciudades, dni) == provincia:
            contador += 1
    return contador

def frecuencia_caracteres(cadena):
    """Retorna un diccionario con la frecuencia de cada carácter en la cadena"""
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def sucesion_mira_y_deci(n):
    """Calcula los primeros n números de la sucesión 'mira y di'"""
    if n <= 0:
        return []
    
    sucesion = [1]
    
    for _ in range(n - 1):
        numero_actual = str(sucesion[-1])
        siguiente = ""
        
        i = 0
        while i < len(numero_actual):
            digito = numero_actual[i]
            contador = 1
            
            while i + contador < len(numero_actual) and numero_actual[i + contador] == digito:
                contador += 1
            
            siguiente += str(contador) + digito
            i += contador
        
        sucesion.append(int(siguiente))
    
    return sucesion