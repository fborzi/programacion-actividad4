def contar_cinco(L):
    """cuenta la cantidad de cincos encontrados
      tanto en la lista o sublistas"""
    contador = 0
    for x in L:
        try:
            for sub_x in x:
                contador += contar_cinco([sub_x])
        except TypeError:
            if x == 5:
                contador += 1
    return contador
def minimo_elemento(lista):
    """verifica un listado de numeros 1x1 a ver cual es el
     de menor valor"""
    if not lista:
        return None
    minimo = lista[0]
    for palabra in lista:
        if palabra < minimo:
            minimo = palabra
    return minimo
def piedra_papel_tijera(uno, dos):
    """es un simple juego de piedra papel o tijera.
     papel le gana a piedra, piedra le gana a tijera
     y tijera le gana a papel"""
    uno = uno.lower()
    dos = dos.lower()
    if uno == dos:
        return 0
    if uno == "papel":
        if dos == "piedra":
            return 1
    if uno == "piedra":
        if dos == "tijera":
            return 1
    if uno == "tijera":
        if dos == "papel":
            return 1
    if dos == "papel":
        if uno == "piedra":
            return 2
    if dos == "piedra":
        if uno == "tijera":
            return 2
    if dos == "tijera":
        if uno == "papel":
            return 2
def borrar_adyacentes(lista):
    """elimina de una lista los datos repetidos, retornando
    la misma lista sin dichos datos repetidos"""
    nueva = [lista[0]]
    for elemento in lista[1:]:
        if elemento != nueva[-1]:
            nueva.append(elemento)
    return nueva
def suma_digitos(n):
    """suma los datos encontrados con mas de 2 digitos,
    retornando el resultado"""
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma
def sumatoria_digitos(lista):
    """retorna una lista con datos pero utiliza la
    funcion anterior para simplificar los datos con mas
    de 2 digitos"""
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado
def dos_sumandos(lista, resultado):
    """retorna 2 numeros de una lista que sumandolos den x resultado"""
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return "no hay numeros que sumen el objetivo"
def digitos_repetidos(n):
    """retorna una lista con los numeros que se repiten mas de 1 vez"""
    n = str(abs(n))
    vistos = set()
    repetidos = set()
    for d in n:
        if d in vistos:
            repetidos.add(int(d))
        else:
            vistos.add(d)
    return list(repetidos)
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