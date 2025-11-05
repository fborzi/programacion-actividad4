
#Ejercicio 6

def minimo_elemento(lista):

    """
    Funcion: minimo_elemento(lista)
    Parametros:
        lista: list
            Lista de elementos comparables entre sí.
    Retorna:
        El valor mínimo encontrado en la lista (mismo tipo de dato que los elementos)
        o None si la lista está vacía.
    Descripcion:
        Recorre la lista recibida, comparando elemento por elemento, y determina el
        valor más chico. En caso de lista vacía, devuelve None.

    """

    if len(lista) == 0:
        return None

    minimo = lista[0]

    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

#Ejercicio 7

def dos_minimos(lista):

    """
    Funcion: dos_minimos(lista)
    Parametros:
        lista: list
            Lista de elementos comparables entre sí.
    Retorna:
        tuple
            Una tupla formada por los dos valores mínimos hallados en la lista.
            Si la lista está vacía retorna (None, None).
            Si la lista tiene un solo elemento retorna (ese_elemento, None).
    Descripcion:
        Analiza los elementos de la lista para identificar los dos valores más pequeños.
        En el caso de lista vacía o con un único elemento, completa con None lo que
        falte para devolver siempre una tupla de dos posiciones.
    """

    if len(lista) == 0:
        return (None, None)
    elif len(lista) == 1:
        return (lista[0], None)
    else:

        if lista[0] < lista[1]:
            min1, min2 = lista[0], lista[1]
        else:
            min1, min2 = lista[1], lista[0]


        for i in range(2, len(lista)):
            n = lista[i]
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n

        return (min1, min2)



#Ejercicio 8


def piedra_papel_tijera(uno, dos):

    """
    Funcion: piedra_papel_tijera(uno, dos)
    Parametros:
        uno: str
            Elección del primer jugador. Puede ser "piedra", "papel" o "tijera".
        dos: str
            Elección del segundo jugador. Puede ser "piedra", "papel" o "tijera".
    Retorna:
        int:
            1 si gana el primer jugador,
            2 si gana el segundo jugador,
            0 si ambos jugadores eligieron la misma opción (empate).
    Descripcion:
        Compara las elecciones de ambos jugadores siguiendo las reglas del juego:
        Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
        Retorna quién gana o si hubo empate.
    """

    uno = uno.lower()
    dos = dos.lower()


    if uno == dos:
        return 0


    if (uno == "piedra" and dos == "tijera") or (uno == "tijera" and dos == "papel") or (uno == "papel" and dos == "piedra"):
        return 1
    else:
        return 2

# Ejercicio 9

def digitos(numero):
    """
    Funcion: digitos(numero)
    Parametros:
        numero: int
            Número entero (puede ser positivo o negativo).
    Retorna:
        list[int]
            Lista de dígitos enteros que componen el número recibido, sin signo.
    Descripcion:
        Convierte el número a su valor absoluto, lo transforma a cadena,
        recorre cada carácter y lo convierte nuevamente a entero, generando
        una lista con cada uno de los dígitos individuales del número.
    """
    numero = abs(numero)
    lista = []
    for digito in str(numero):
        lista.append(int(digito))
    return lista


# Ejercicio 10
def borrar_adyacentes(lista):
    """
    Funcion: borrar_adyacentes(lista)
    Parametros:
        lista: list
            Lista de caracteres (strings de longitud 1) o elementos comparables.
    Retorna:
        list
            Nueva lista sin repeticiones consecutivas de elementos adyacentes.
    Descripcion:
        Recorre la lista recibida y construye otra lista donde se eliminan
        únicamente las repeticiones consecutivas (una atrás de la otra).
        No elimina repeticiones de elementos que reaparezcan luego separados.
    """
    if not lista:
        return []

    resultado = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            resultado.append(lista[i])

    return resultado

# Ejercicio 11

def ocurrencias(lista):

    """
    DESCRIPCIÓN GENERAL:
    Analiza una lista y agrupa cada elemento por sus repeticiones consecutivas.
    Cada vez que un elemento cambia, se guarda el elemento anterior junto con cuántas veces seguidas apareció.
    Luego retorna esas agrupaciones como una lista de pares: [elemento, cantidad].

    PARÁMETROS QUE RECIBE:
    - lista: lista con elementos (pueden ser números, caracteres, strings, etc.)

    QUÉ RETORNA:
    - Si la lista está vacía → retorna []
    - Si la lista tiene elementos → retorna una lista con sublistas del tipo: [elemento, cantidad_de_repeticiones_contiguas]

    """
    if not lista:
        return []

    resultado = []
    actual = lista[0]
    contador = 1


    for elem in lista[1:]:
        if elem == actual:
            contador += 1  
        else:
            resultado.append([actual, contador])  
            actual = elem 
            contador = 1 

    # Agregar el último grupo
    resultado.append([actual, contador])
    return resultado

# Ejercicio 12

def suma_digitos(n):
    """
    DESCRIPCIÓN GENERAL:
    Calcula la suma de todos los dígitos de un número entero positivo.

    PARÁMETROS QUE RECIBE:
    - n: int
        Número entero positivo cuyos dígitos se van a sumar.

    QUÉ RETORNA:
    - int: la suma de los dígitos de n.
      Por ejemplo, si n = 123, retorna 6 (1 + 2 + 3).
      """
    suma = 0
    while n > 0:
        suma += n % 10   # tomo el último dígito
        n = n // 10          # elimino el último dígito
    return suma


def sumatoria_digitos(lista):
    """
    DESCRIPCIÓN GENERAL:
    Procesa una lista de números enteros positivos y calcula la suma de los dígitos de cada número.
    Retorna una nueva lista donde cada elemento corresponde a la suma de los dígitos del número en la misma posición de la lista original.

    PARÁMETROS QUE RECIBE:
    - lista: list[int]
        Lista de números enteros positivos.

    QUÉ RETORNA:
    - list[int]: lista de la misma longitud que la original, donde cada elemento es la suma de los dígitos del número correspondiente."""

    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado

# Ejercicio 13

def indice_mayor(lista):
    """
    DESCRIPCIÓN GENERAL:
    Determina cuál es el elemento mayor de una lista de números y devuelve su índice dentro de la lista.

    PARÁMETROS QUE RECIBE:
    - lista: list[float|int]
        Lista de números (enteros o flotantes). Puede estar vacía.

    QUÉ RETORNA:
    - int: índice del elemento mayor en la lista.
    - None: si la lista está vacía.
   """
    if not lista:  # si la lista está vacía
        return None

    mayor = lista[0]
    indice_mayor = 0

    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice_mayor = i

    return indice_mayor

# Ejercicio 14


def dos_sumandos(lista, resultado):

    """
    DESCRIPCIÓN GENERAL:
    Busca en una lista dos elementos distintos cuya suma sea igual al valor especificado.
    Retorna los índices de estos dos elementos si se encuentra una combinación válida.

    PARÁMETROS QUE RECIBE:
    - lista: list[float|int]
        Lista de números donde se buscarán los dos sumandos.
    - resultado: float|int
        Valor que se desea obtener como suma de dos elementos de la lista.

    QUÉ RETORNA:
    - list[int]: lista de dos elementos con los índices de los números que suman 'resultado'.
    - None: si no existe ninguna combinación de dos elementos cuya suma sea igual a 'resultado'.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # empieza desde i+1 para no usar el mismo número dos veces
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None  # si no se encuentran dos números que sumen el resultado

# Ejercicio 15

def obtenerCiudad(personas, DNI):
    """
    DESCRIPCIÓN GENERAL:
    Busca en una lista de personas la ciudad de residencia de quien posee un DNI específico.

    PARÁMETROS QUE RECIBE:
    - personas: list[list]
        Lista de personas, donde cada persona se representa como una lista con al menos tres elementos:
        [nombre, DNI, ciudad, ...].
    - DNI: int
        Documento de identidad de la persona cuya ciudad se desea conocer.

    QUÉ RETORNA:
    - str: nombre de la ciudad donde reside la persona con el DNI especificado.
    - None: si no se encuentra ninguna persona con el DNI proporcionado.
    """
    for persona in personas:
        if persona[1] == DNI:  # persona[1] es el DNI
            return persona[2]  # persona[2] es la ciudad
    return None  # Si no se encuentra el DNI

def obtenerProvincia(personas, ciudades, DNI):
    """
    DESCRIPCIÓN GENERAL:
    Determina la provincia de residencia de una persona a partir de su DNI,
    usando la relación entre personas y la lista de ciudades con sus provincias.
    PARÁMETROS QUE RECIBE:
    - personas: list[list]
        Lista de personas, donde cada persona se representa como una lista con al menos tres elementos:
        [nombre, DNI, ciudad, ...].
    - ciudades: list[list]
        Lista de ciudades, donde cada ciudad se representa como [nombre_ciudad, provincia].
    - DNI: int
        Documento de identidad de la persona cuya provincia se desea conocer.

    QUÉ RETORNA:
    - str: nombre de la provincia donde reside la persona con el DNI especificado.
    - None: si no se encuentra la persona con el DNI proporcionado o si la ciudad no está en la lista de ciudades.
    """
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None  # el DNI no existe en la lista de personas

    for c in ciudades:
        if c[0] == ciudad:  # c[0] es el nombre de la ciudad
            return c[1]     # c[1] es la provincia
    return None  # si la ciudad no está en la lista de ciudades


def contarPoblacion(personas, ciudades, provincia):
    """
    DESCRIPCIÓN GENERAL:
    Calcula cuántas personas viven en una provincia determinada
    utilizando la relación entre las listas de personas y ciudades.

    PARÁMETROS QUE RECIBE:
    - personas: list[list]
        Lista de personas, donde cada persona se representa como [nombre, DNI, ciudad, ...].
    - ciudades: list[list]
        Lista de ciudades, donde cada ciudad se representa como [nombre_ciudad, provincia].
    - provincia: str
        Nombre de la provincia cuya población se desea contar.

    QUÉ RETORNA:
    - int: cantidad de personas que residen en la provincia especificada.
    """
    contador = 0

    for persona in personas:
        DNI = persona[1]
        prov = obtenerProvincia(personas, ciudades, DNI)
        if prov == provincia:
            contador += 1
    return contador

#Ejercicio 18

def digitos_repetidos(n):
    """La funcion recibe un numero como argumento y retorna una lista compuesta por los digitos
       repetidos en el numero recibido."""
    s = str(n)

    repetidos = []
    for d in s:
        # Si el dígito aparece más de una vez y no está ya en la lista, lo agregamos
        if s.count(d) > 1 and d not in repetidos:
            repetidos.append(d)
    return repetidos


#Ejercicio 25
"""
    Calcula la frecuencia de aparición de cada carácter en la cadena recibida.

    Parámetros:
    cadena (str): Texto en el que se computarán las frecuencias de cada carácter.

    Retorna:
    dict: Un diccionario donde las claves son los caracteres encontrados en la cadena
          y los valores son enteros que indican cuántas veces aparece cada carácter.
    """

def frecuencia_caracteres(cadena):
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

# Ejemplo de uso
texto = "hola mundo"
resultado = frecuencia_caracteres(texto)
print(resultado)

#Ejercicio 29
def sucesion_mira_y_deci(n):
    """
    Recibe un número n y retorna una lista con los primeros n términos
    de la sucesión "mirá y decí".
    La sucesión arranca en 1, y cada término se genera describiendo
    cuántas veces aparece seguido cada dígito del término anterior.
    """
    lista = [1]
    while len(lista) < n:
        anterior = str(lista[-1])
        nuevo = ""
        i = 0
        while i < len(anterior):
            dig = anterior[i]
            cant = 1
            while i+1 < len(anterior) and anterior[i+1] == dig:
                cant += 1
                i += 1
            nuevo += str(cant) + dig
            i += 1
        lista.append(int(nuevo))
    return lista

# Ejemplo de uso:
print(sucesion_mira_y_deci(9))

