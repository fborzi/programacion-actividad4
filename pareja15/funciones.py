def dos_minimos(lista):
    """Retorna los dos valores menores de la lista"""
    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:
        min1, min2 = None, None
        for num in lista:
            if min1 is None or num < min1:
                min2 = min1
                min1 = num
            elif min2 is None or num < min2:
                min2 = num
        return (min1, min2)

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
    # Crear un diccionario ciudad -> provincia para acceso rápido
    ciudad_a_provincia = {ciudad: prov for ciudad, prov in ciudades}
    contador = 0
    for persona in personas:
        ciudad = persona[2]
        if ciudad_a_provincia.get(ciudad) == provincia:
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
#Ejercicio 6 
"""Función que recibe una lista y devuelve el elemento mínimo de la lista. Si la lista está vacía, devuelve None.
 @param lista: Lista de elementos comparables.
 return: El elemento mínimo de la lista o None si la lista está vacía.
"""
def minimo_elemento(lista):
    if not lista:
        return None   
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

#Ejercicio8
"""Función que simula el juego de piedra, papel o tijera.
 @param uno: Elección del primer jugador ('piedra', 'papel' o 'tijera').
 @param dos: Elección del segundo jugador ('piedra', 'papel' o 'tijera').
 return: 1 si gana el primer jugador, 2 si gana el segundo jugador, 0 en caso de empate.
"""
def piedra_papel_tijera(uno, dos):
    uno = uno.lower()
    dos = dos.lower()
    
    if uno == dos:
        return 0
    
    if (uno == 'piedra' and dos == 'tijera') or \
       (uno == 'tijera' and dos == 'papel') or \
       (uno == 'papel' and dos == 'piedra'):
        return 1
    
    return 2

#Ejercicio10
"""Función que elimina los elementos adyacentes repetidos en una lista.
     @param lista: Lista de elementos.
     return: Nueva lista sin elementos adyacentes repetidos.
"""
def borrar_adyacentes(lista):
    if not lista:
        return []
    
    resultado = [lista[0]]
    
    for elemento in lista[1:]:
        if elemento != resultado[-1]:
            resultado.append(elemento)
    
    return resultado

#Ejercicio12
"""Función que retorna una lista con la suma de los dígitos de cada número en la lista dada.
     @param lista: Lista de números enteros.
     return: Nueva lista con la suma de los dígitos de cada número."""
# Función que suma los dígitos de un número
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10   
        n //= 10          
    return suma

# Función que aplica la suma de dígitos a cada número de la lista
def sumatoria_digitos(lista):
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado

#Ejercicio14
def dos_sumandos(lista, resultado):
    """Función que encuentra dos índices en una lista cuya suma de elementos es igual al resultado dado.
     @param lista: Lista de números enteros.
     @param resultado: Número entero que es la suma objetivo.
     return: Lista con los dos índices si se encuentran, o lista vacía si no se encuentran."""
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)): 
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return []  

#Ejercicio18

def digitos_repetidos(n):
    """Función que recibe un número entero y devuelve una lista con los dígitos que se repiten en ese número.
     @param n: Número entero.
     return: Lista de dígitos repetidos en el número."""
    n_str = str(n)
    
    repetidos = [] 
    for digito in n_str:
        if n_str.count(digito) > 1 and digito not in repetidos:
            repetidos.append(int(digito))
    
    return repetidos

#Ejercicio20
def letras_repetidas(palabra):
    """Función que recibe una palabra y devuelve una lista con las letras que se repiten en esa palabra.
     @param palabra: Cadena de texto.
     return: Lista de letras repetidas en la palabra."""
    palabra = palabra.lower()  
    repetidas = []             

    for letra in palabra:
        if letra.isalpha():  
            if palabra.count(letra) > 1 and letra not in repetidas:
                repetidas.append(letra)
    return repetidas


