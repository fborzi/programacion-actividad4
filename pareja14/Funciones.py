# del Ejercicio 9
def digitos(numero):
    return [int(digito) for digito in str(numero) if digito.isdigit()]

# ejercicio 11:
def ocurrencias(lista):
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

# Ejercicio 13:
def indice_mayor(lista):
    print(f"Lista recibida: {lista}")  # Depuración
    if not lista:
        return None
    
    indice_max = 0
    mayor = lista[0]
    print(f"Inicio - índice: {indice_max}, mayor: {mayor}")  # Depuración
    
    for i in range(1, len(lista)):
        print(f"Comparando índice {i}: {lista[i]} > {mayor}?")  # Depuración
        if lista[i] > mayor:
            mayor = lista[i]
            indice_max = i
            print(f"Actualizado - índice: {indice_max}, mayor: {mayor}")  # Depuración
    
    print(f"Resultado final: {indice_max}")  # Depuración
    return indice_max

# Ejercicio 15:
# A
def obtenerCiudad(personas, DNI):
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None

# B
def obtenerProvincia(personas, ciudades, DNI):
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None
    for ciudad_info in ciudades:
        if ciudad_info[0] == ciudad:
            return ciudad_info[1]
    return None

# C
def contarPoblacion(personas, ciudades, provincia):
    contador = 0
    for persona in personas:
        if obtenerProvincia(personas, ciudades, persona[1]) == provincia:
            contador += 1
    return contador


 
# ejercicio 25

def frecuencia_caracteres(cadena):
    """
    Recibe una cadena de texto y retorna un diccionario con la frecuencia de cada carácter.
    
    Args:
        cadena (str): La cadena de texto a analizar
    
    Returns:
        dict: Diccionario con caracteres como claves y frecuencias como valores
    """
    frecuencia = {}
    for caracter in cadena:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    return frecuencia


# ejercicio 29:

def sucesion_mira_y_deci(n):
    """
    Calcula los primeros n números de la sucesión 'mira y dice'.
    
    Args:
        n (int): Cantidad de términos a generar
    
    Returns:
        list: Lista con los primeros n términos de la sucesión
    """
    if n == 0:
        return []
    
    # Iniciamos con el primer término
    terminos = []
    actual = "1"
    terminos.append(int(actual))
    
    # Generamos los siguientes n-1 términos
    for _ in range(1, n):
        siguiente = ""
        i = 0
        while i < len(actual):
            j = i
            # Contamos dígitos consecutivos iguales
            while j < len(actual) and actual[j] == actual[i]:
                j += 1
            count = j - i
            siguiente += str(count) + actual[i]
            i = j
        
        terminos.append(int(siguiente))
        actual = siguiente
    
    return terminos