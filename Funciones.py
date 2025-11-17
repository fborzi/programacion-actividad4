#Funciones ej 1
def verificar_pertenencia(lista, elementos):
    """Verifica si cada elemento pertenece a la lista y muestra el resultado."""
    for elemento in elementos:
        if elemento in lista:
            print ("el elemento", elemento, "-> pertenece a la lista.")
        else:
            print("elemento", elemento,  " -> NO pertenece a la lista.")


def obtener_indice(lista, elemento):
    """Devuelve la posición (índice) de un elemento en la lista, si existe."""
    if elemento in lista:
        print("El elemento", elemento, "se encuentra en la posición: ", lista.index(elemento))
    else:
        print(f"El elemento {elemento} no se encuentra en la lista.")
"""-------------------------------------------------------------------------------------"""      

#funcion ej 2 - contar cuantas veces está el num 5 en la lista L
def contar_cincos():

    L = [5, 6, [9, 5], 2, 5]

    cantidad = L.count(5)
    print("Cantidad de veces que aparece el 5 en la lista principal:", cantidad)


"""-------------------------------------------------------------------------------------"""  
        
    
    
    #funciones programa ej 3
def operaciones_lista_a():
    """Realiza las operaciones solicitadas sobre la lista 'a' y mostrar los resultados."""
    a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]
    print("Lista original:", a)

    # 1️ Obtener el primero y el último elemento
    print("Primer elemento:", a[0])
    print("Último elemento:", a[-1])

    # 2️ Eliminar el primer elemento
    a.pop(0)
    print("Después de eliminar el primer elemento:", a)

    # 3️ Eliminar los tres últimos elementos
    del a[-3:]
    print("Después de eliminar los tres últimos elementos:", a)

    # 4️ Insertar el valor 9 en el primer lugar
    a.insert(0, 9)
    print("Después de insertar 9 al inicio:", a)

    # 5️ Reemplazar el valor 'ix' por 4
    if 'ix' in a:
        indice_ix = a.index('ix')
        a[indice_ix] = 4
    print("Después de reemplazar 'ix' por 4:", a)

    # 6️ Agregar el valor 5 al final
    a.append(5)
    print("Después de agregar 5 al final:", a)

    # 7️ Obtener mediante rebanada los primeros 3 elementos
    primeros_tres = a[:3]
    print("Primeros tres elementos (rebanada):", primeros_tres)

    # 8️ Insertar la lista dentro de sí misma
    a.append(a)
    print("Después de insertar la lista dentro de sí misma:", a)

    # 9️ Verificar pertenencia de 'dos' y 3.0
    print("'dos' pertenece a la lista?", 'dos' in a)
    print("3.0 pertenece a la lista?", 3.0 in a)

    # 10 Contar ocurrencias de 1 y de 4
    print("Cantidad de veces que aparece 1:", a.count(1))
    print("Cantidad de veces que aparece 4:", a.count(4))

    # 1️1️ Imprimir cada elemento de la lista
    print("Elementos de la lista:")
    for elemento in a:
        print(elemento)

    # 1️2️ Imprimir cada elemento en forma inversa
    print("Elementos en orden inverso:")
    for elemento in reversed(a):
        print(elemento)
        
        
"""-----------------------------------------------------------------------------------"""


def ingresar_nombres():
    """funcion ej 4 - Pide nombres por teclado hasta que el usuario ingrese uno en blanco, 
    los guarda en una lista y los muestra al final."""
    
    nombres = []
    nombre = input("Ingrese un nombre (o presione Enter para finalizar): ")
    
    while nombre != "" :
        nombres.append(nombre)
        nombre = input("Ingrese otro nombre (o Enter para terminar): ")
    
    print("\nLista de nombres ingresados:")
    for n in nombres:
        print(n)
        
"""------------------------------------------------------------------------------------"""
#funcion ejercicio 5 - Convertir los nombres en Mayus
def nombres_mayusculas():
    
    
    # Pedimos nuevamente los nombres (igual que en el ejercicio 4)
    nombres = []
    nombre = input("Ingrese un nombre (o presione Enter para finalizar): ")
    
    while nombre != "" :
        nombres.append(nombre)
        nombre = input("Ingrese otro nombre (o Enter para terminar): ")
    
    # Creamos una nueva lista con los nombres en mayúsculas
    nombres_mayus = [n.upper() for n in nombres]
    
    print("\nLista original:")
    print(nombres)
    
    print("\nLista en mayúsculas:")
    for n in nombres_mayus:
        print(n)
        
    """-----------------------------------------------------------------------------------"""
    # funcion ej 6 - devolver el minimo de una lista o None si esta vcia

def minimo_elemento(lista):
    """Devuelve el mínimo elemento de una lista o None si está vacía."""
    
    if not lista:  # Si la lista está vacía
        return None
    
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

"""----------------------------------------------------------------------------------------"""
# funcion ej 7 - Devuelve los 2 valores minimos de una lista. Si la lista tiene menos de 2 elmtos, 
# conpleta con None los datos faltntes

def dos_minimos(lista):

    # Si la lista está vacía
    if not lista:
        return (None, None)
    
    # Si tiene un solo elemento
    if len(lista) == 1:
        return (lista[0], None)
    
    # Copiamos la lista y la ordenamos para no modificar la original
    ordenada = sorted(lista)
    
    # Retornamos los dos primeros elementos
    return (ordenada[0], ordenada[1])

"""---------------------------------------------------------------------------------------"""
#funcion ej 8 - Piedra, papel o tijera
def piedra_papel_tijera(uno, dos):
    
    # Convertir a minúsculas para ignorar mayúsculas/minúsculas
    uno = uno.lower()
    dos = dos.lower()
    
    # Caso de empate
    if uno == dos:
        return 0
    
    # Combinaciones ganadoras del jugador 1
    if (uno == "piedra" and dos == "tijera") or \
       (uno == "tijera" and dos == "papel") or \
       (uno == "papel" and dos == "piedra"):
        return 1
    
    # Si no es empate ni gana el jugador 1, gana el jugador 2
    return 2

"""------------------------------------------------------------------------------------"""
#Funcion ej 9 - Transformar numeros en una lista
def digitos(numero):
    
    # Convertimos el número a string para recorrerlo fácilmente
    numero_str = str(abs(numero))  # abs() evita problemas con números negativos
    lista_digitos = [int(d) for d in numero_str]
    
    return lista_digitos

"""------------------------------------------------------------------------------------"""
#funcion ej10- eliminar datos repetidos adyacentes de una lista
def borrar_adyacentes(lista):
    
    if not lista:  #  lista vacía
        return []
    
    resultado = [lista[0]]  
    
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            resultado.append(lista[i])
    
    return resultado

"""---------------------------------------------------------------------------------------"""
#funcion ej11 - Eliminar adyacentes pero que retorne el elemento y cuantas veces aparece
def ocurrencias(lista):
    
    if not lista:
        return []
    
    resultado = []
    actual = lista[0]
    contador = 1
    
    for i in range(1, len(lista)):
        if lista[i] == actual:
            contador += 1
        else:
            resultado.append([actual, contador])
            actual = lista[i]
            contador = 1
    
    # Agregar el último grupo
    resultado.append([actual, contador])
    
    return resultado

"""-------------------- ---------------------------------------------------------------"""
#funcion ej12 - Devuelve una lista con la suma de los digitos de cada numero 

def sumatoria_digitos(lista):
    
    resultado = []
    
    for numero in lista:
        # Convertimos el número a string y sumamos los dígitos
        suma = sum(int(d) for d in str(numero))
        resultado.append(suma)
    
    return resultado

"""------------------------------------------------------------------------------------"""
# funcion ej 13 - devuelve el indice del mayor n° de la lista

def indice_mayor(lista):
    
    if not lista:  # lista vacía
        return None
    
    mayor = lista[0]
    indice = 0
    
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    
    return indice

"""-------------------------------------------------------------------------------------"""
#funcion ej 14 - Devuelve lista con el resultado de la suma de los indices de dos elemtnos
def dos_sumandos(lista, resultado):
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    
    # Si no se encuentra ninguna combinación
    return []


"""--------------------------------------------------------------------------------------"""
#Funciones ej 15 - lista personas y lista datos provincisa

def obtenerCiudad(personas, DNI):
    """Devuelve la ciudad donde vive la persona con el DNI """
    for persona in personas:
        nombre, dni, ciudad = persona
        if dni == DNI:
            return ciudad
    return None


def obtenerProvincia(personas, ciudades, DNI):
    """Devuelve la provincia donde vive la persona con el DNI dado.
    Usa la función obtenerCiudad()."""
    ciudad_persona = obtenerCiudad(personas, DNI)
    if ciudad_persona is None:
        return None
    
    for ciudad, provincia in ciudades:
        if ciudad == ciudad_persona:
            return provincia
    return None


def contarPoblacion(personas, ciudades, provincia):
    """Devuelve cuántas personas viven en la provincia dada.
    Usa la función obtenerProvincia()."""
    contador = 0
    for persona in personas:
        _, dni, _ = persona
        provincia_persona = obtenerProvincia(personas, ciudades, dni)
        if provincia_persona == provincia:
            contador += 1
    return contador

"""--------------------------------------------------------------------------------------"""
#Funciones ej  18 - digitos_repetidos(n)
def digitos_repetidos(n):
    # pasamos el número a string para recorrer digitos
    n = str(n)
    
    repetidos = []
    
    for digito in n:
        if n.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)
    
    return repetidos
"""--------------------------------------------------------------------------------------"""
#Funciones ej 21 -

def limpiar_palabra(palabra):
    palabra = palabra.lower()
    letras_validas = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    resultado = ""
    for letra in palabra:
        if letra in letras_validas:
            resultado = resultado + letra
    return resultado


def tiene_3_vocales_diferentes(palabra):
    palabra = palabra.lower()
    vocales = "aeiouáéíóú"
    usadas = ""

    for letra in palabra:
        if letra in vocales:
            # normalizamos vocales con tilde
            if letra == "á":
                letra = "a"
            if letra == "é":
                letra = "e"
            if letra == "í":
                letra = "i"
            if letra == "ó":
                letra = "o"
            if letra == "ú":
                letra = "u"

            if letra not in usadas:
                usadas = usadas + letra

    if len(usadas) >= 3:
        return True
    else:
        return False
    
"""--------------------------------------------------------------------------------------"""
#Funciones ej 24 - cargas de socios

def cargar_socios(socios):
    dni = int(input("Ingrese DNI (0 para terminar): "))
    if dni == 0:
        return
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    cuota = input("¿Cuota al día? (s/n): ").lower() == "s"

    socios[dni] = [nombre, apellido, edad, cuota]

    cargar_socios(socios) 
"""---------------------------------------------------"""
#eje 25 - 
def frecuencia_caracteres(cadena):
    frecuencias = {}

    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    return frecuencias

"""---------------------------------"""
#ejercicio 26
def cargar_ciudades_sin_lista(dic_paises, contador=0):
    ciudad = input("Ciudad(ponga zz para terminar): ")
    if ciudad.lower() == "zz":
        return contador
    
    pais = input("País: ")

    # contamos total
    contador += 1

    # contamos por país
    dic_paises[pais] = dic_paises.get(pais, 0) + 1

    return cargar_ciudades_sin_lista(dic_paises, contador)
"""-------------------------------------"""
#ejercio 29
def sucesion_mira_y_deci(n):
    resultado = ["1"]
    for _ in range(1, n):
        anterior = resultado[-1]
        nuevo = ""
        contador = 1
        for i in range(1, len(anterior)):
            if anterior[i] == anterior[i - 1]:
                contador += 1
            else:
                nuevo += str(contador) + anterior[i - 1]
                contador = 1
        nuevo += str(contador) + anterior[-1]
        resultado.append(nuevo)
    return [int(x) for x in resultado]