
#Ejercicio 6

def minimo_elemento(lista):

    """La función recibe como parámetro una lista de elementos comparables
      entre sí y devuelve el mínimo valor encontrado en dicha lista
      o None si la lista fuera vacía
      @Param: Lista de elementos
      @return: None (lista vacia). valor minimo (lista con elementos)
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

    """La función recibe una lista como argumento y compara sus elementos, devolviendo
    sus dos elementos menores. Si la lista esta vacia o si tiene menos de dos elementos
    devuelve None por cada elemento faltante."""

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
    Esta función recibe dos cadenas que representan las elecciones de dos jugadores 
    en el juego Piedra, Papel o Tijera. 

    Retorna:
    - 1 si gana el primer jugador
    - 2 si gana el segundo jugador
    - 0 si hay empate (ambos eligieron el mismo elemento)
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
    Recibe un número entero y retorna una lista con sus dígitos.
    @Parametro numero entero
    @ retorno lista de numeros eneteros

    """
    numero = abs(numero)
    lista = []
    for digito in str(numero):
        lista.append(int(digito))
    return lista


# Ejercicio 10
def borrar_adyacentes(lista):
    """
    Recibe una lista de caracteres y retorna otra lista eliminando
    repeticiones consecutivas de caracteres adyacentes.

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
    Recibe una lista y retorna otra lista que contiene listas con cada elemento
    junto con el número de ocurrencias contiguas de ese elemento.

    """
    if not lista:
        return []

    resultado = []
    actual = lista[0]
    contador = 1

    # Recorrer desde el segundo elemento
    for elem in lista[1:]:
        if elem == actual:
            contador += 1  # Mismo elemento consecutivo
        else:
            resultado.append([actual, contador])  # Guardar el anterior
            actual = elem  # Cambiar al nuevo elemento
            contador = 1  # Reiniciar contador

    # Agregar el último grupo
    resultado.append([actual, contador])
    return resultado

# Ejercicio 12

def suma_digitos(n):
    """
    Recibe un número entero y retorna la suma de sus dígitos.

    """
    suma = 0
    while n > 0:
        suma += n % 10   # tomo el último dígito
        n = n // 10          # elimino el último dígito
    return suma


def sumatoria_digitos(lista):
    """
    Recibe una lista de números enteros positivos y retorna otra lista
    con la suma de los dígitos de cada número.

    """
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado

# Ejercicio 13

def indice_mayor(lista):
    """
    Recibe una lista de números y retorna el índice del mayor elemento.

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
    Recibe una lista de números y otro número (resultado).
    Retorna una lista con dos índices de elementos cuya suma da el resultado.

    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # empieza desde i+1 para no usar el mismo número dos veces
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None  # si no se encuentran dos números que sumen el resultado

# Ejercicio 15

def obtenerCiudad(personas, DNI):
    """
    Recibe la lista de personas y un DNI, y retorna la ciudad donde vive la persona.

    """
    for persona in personas:
        if persona[1] == DNI:  # persona[1] es el DNI
            return persona[2]  # persona[2] es la ciudad
    return None  # Si no se encuentra el DNI

def obtenerProvincia(personas, ciudades, DNI):
    """
    Recibe las listas de personas y ciudades, y un DNI.
    Retorna la provincia donde vive la persona.
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
    Recibe las listas de personas y ciudades y una provincia.
    Retorna cuántas personas viven en esa provincia.
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

    s = str(n)

    repetidos = []
    for d in s:
        # Si el dígito aparece más de una vez y no está ya en la lista, lo agregamos
        if s.count(d) > 1 and d not in repetidos:
            repetidos.append(d)
    return repetidos


#Ejercicio 25
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

def sucesion_mira_y_deci(n):
    if n <= 0:
        return []
    
    # Primer término de la sucesión
    sucesion = ["1"]
    
    # Generamos los siguientes n-1 términos
    for _ in range(n - 1):
        anterior = sucesion[-1]
        nuevo = ""
        contador = 1
        
        # Recorremos los dígitos del número anterior
        for i in range(1, len(anterior)):
            if anterior[i] == anterior[i - 1]:
                contador += 1
            else:
                # Agregamos el conteo y el dígito
                nuevo += str(contador) + anterior[i - 1]
                contador = 1
        
        # Agregamos el último grupo de dígitos
        nuevo += str(contador) + anterior[-1]
        sucesion.append(nuevo)
    
    # Convertimos los elementos a enteros si se desea, o los dejamos como strings
    # return [int(x) for x in sucesion]
    return [int(x) if x.isdigit() else x for x in sucesion]

# Ejemplo de uso:
print(sucesion_mira_y_deci(9))

