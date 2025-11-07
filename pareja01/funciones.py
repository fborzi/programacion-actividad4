import unicodedata
# Devuelve los dos valores minimos de una lista de numeros.
# Si la lista tiene menos de dos elementos, devuelve None en el segundo valor.
# parametro lista: []
def dos_minimos(lista):
    largo = len(lista)
    if largo < 2:
        print("Primer valor menor: ", lista[0] if largo == 1 else "NONE", 
              ". Segundo valor menor: NONE")
        return (None,"NONE", None,"NONE")
    elif largo == 1:
        return (lista[0], None)
    
    min1 = float('inf')
    min2 = float('inf')
    
    for num in lista:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
            
    if min2 == float('inf'):
        min2 = None
    print("Primer valor menor: ", min1, ". Segundo valor menor: ", min2)
    return (min1, min2)

# Agregar nombres a una lista hasta que el usuario decida finalizar ingresando una cadena vacia.
def agregar_nombres():
    nombres = []
    while True:
        nombre = input("Introduce un nombre (o presiona Enter para dejar en blanco y finalizar): ")
        if nombre == "" or nombre == " ":
            break
        nombres.append(nombre)

    print("\nLista de nombres ingresados:")
    for n in nombres:
        print(n)


def minimo_elemento(lista):
    if not lista: 
        return None
    
    minimo = lista[0]  
    for elemento in lista[1:]:  
        if elemento < minimo:
            minimo = elemento
    print(f"El elemento mínimo es: {minimo}")
    return minimo   
    return nombres

#Convierte en mayusculas una lista de nombres.
#parametro nombres: []
def nombres_mayusculas(nombres):
    nombresMayus = []
    for nombre in nombres:
            nombre = nombre.upper()
            nombresMayus.append(nombre)

    print("\nLista de nombres en mayúsculas:", nombresMayus)
    return nombresMayus


# Retorna una lista con los dígitos que componen al número pasado por parámetro.
# parametro numero: int
def digitos(numero):
    digitos = []
    for digito in str(numero):
        digitos.append(int(digito))
    print(digitos) 
    return digitos
# Juego de Piedra, Papel o Tijera


def piedra_papel_tijera(uno, dos):
    
    uno = uno.lower()
    dos = dos.lower()

    
    if uno == dos:
        return 0

    if (uno == "piedra" and dos == "tijera") or \
       (uno == "tijera" and dos == "papel") or \
       (uno == "papel" and dos == "piedra"):
        return 1  
    else:
        return 2  
    

def borrar_adyacentes(lista):
    if not lista:  
        return []

    resultado = [lista[0]]  

    for elemento in lista[1:]:
        if elemento != resultado[-1]: 
            resultado.append(elemento)

    return resultado
   
# Retorna una lista que contiene listas formadas por cada elemento de la lista junto con el número de ocurrencias contiguas de ese elemento en la lista, con el orden en que fueron apareciendo.
# parametro lista: []
def ocurrencias(lista):
    resultado = []
    contador = 1
    elemento_actual = lista[0]

    for elemento in lista[1:]:
        if elemento == elemento_actual:
            contador += 1
        else:
            resultado.append([elemento_actual, contador])
            elemento_actual = elemento
            contador = 1

    resultado.append([elemento_actual, contador])
    print(resultado)
    return resultado


def suma_digitos(n):
    
    return sum(int(digito) for digito in str(n))


def sumatoria_digitos(lista):
    
    return [suma_digitos(num) for num in lista]


# Retorna el índice del mayor número en la lista.
# parametro lista: []
def indice_mayor(lista):
    indiceMayor = 0
    valorMayor = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > valorMayor:
            valorMayor = lista[i]
            indiceMayor = i
    print(indiceMayor)
    return indiceMayor


#retorna los índices de dos elementos cuya suma da el resultado esperado.
#parametro lista: []
#parametro resultado: int
def dos_sumandos(lista, resultado):
    longitud = len(lista)
    for i in range(longitud):
        for j in range(i + 1, longitud):
            if lista[i] + lista[j] == resultado:
                print("Índices encontrados:", i, j)
                return (i, j)
    print("No se encontraron dos sumandos que den el resultado esperado.")
    return None

#obtiene la ciudad y provincia de una persona a partir de su DNI.
#parametro personas: [] 
#parametro DNI: int
def obtenerCiudad(personas, DNI):
    for persona in personas:
        if persona[1] == DNI:
            print("Ciudad a la que pertenece:", persona[2])
            return persona[2]
    print("DNI no encontrado")
    return None


#obtiene la provincia de una persona a partir de su DNI.
#parametro personas: []
#parametro ciudades: []
#parametro DNI: int
def obtenerProvincia(personas, ciudades, DNI):
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad:
        for c in ciudades:
            if c[0] == ciudad:
                print("Provincia a la que pertenece:", c[1])
                return c[1]
    print("Ciudad no encontrada")
    return None


#cuenta la cantidad de personas que viven en una provincia determinada.
#parametro personas: [] 
#parametro ciudades: []
#parametro provincia: str
def contarPoblacion(personas, ciudades, provincia):
    cantidad = sum(1 for p in personas if obtenerProvincia([p], ciudades, p[1]) == provincia)
    print("Cantidad de personas que viven en la provincia de", provincia, ":", cantidad)
    return cantidad


# Retorna una lista conteniendo los dígitos que se repiten en n. Cada dígito deberá aparecer una única vez en la lista, aunque se repita varias veces.
# parametro n: int
def digitos_repetidos(n):
    str_n = str(n)
    repetidos = set()
    vistos = set()
    
    for digito in str_n:
        if digito in vistos:
            repetidos.add(int(digito))
        else:
            vistos.add(digito)
    print(repetidos)
    return list(repetidos)


# recibe una oracion y calcula cuantas palabras contiene
def cantidad_palabras(frase):
    palabras = frase.split()
    cantidad = len(palabras)
    print(f"Cantidad de palabras: {cantidad}")

    for palabra in palabras:
        letras_vistas = set()
        letras_repetidas = set()
        for letra in palabra.lower():
            if letra.isalpha():
                if letra in letras_vistas:
                    letras_repetidas.add(letra)
                else:
                    letras_vistas.add(letra)
        if letras_repetidas:
            print(f"Letras repetidas en '{palabra}': {', '.join(sorted(letras_repetidas))}")
        else:
            print(f"No hay letras repetidas en '{palabra}'")



habitantes = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

def informar_habitantes(ciudad):
    if ciudad in habitantes:
        return habitantes[ciudad]
    print("La ciudad ", ciudad," no existe en el registro")

def agregar_ciudad(ciudad, poblacion):
    habitantes[ciudad] = poblacion

def eliminar_ciudad(ciudad):
    if ciudad in habitantes:
        del habitantes[ciudad]

def incrementar_habitantes(ciudad, cantidad):
    if ciudad in habitantes:
        habitantes[ciudad] += cantidad

def modificar_habitantes(ciudad, nueva_cantidad):
    if ciudad in habitantes:
        habitantes[ciudad] = nueva_cantidad


class Socio:
    def __init__(self, nombre, apellido, dni, edad, cuota_al_dia):
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
            self.edad = edad
            self.cuota_al_dia = cuota_al_dia

def ingresar_socios():
    socios = {}
    while True:
        dni = input("Ingrese DNI (0 para terminar): ")
        if dni == "0":
            break
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        cuota_al_dia = input("¿Cuota al día? (s/n): ").lower() == 's'
        socios[dni] = Socio(nombre, apellido, dni, edad, cuota_al_dia)
    return socios

def cantidad_socios(socios):
    return len(socios)

def cantidad_morosos(socios):
    return sum(1 for socio in socios.values() if not socio.cuota_al_dia)

def buscar_socio(socios, dni):
    if dni in socios:
        socio = socios[dni]
        return f"Socio encontrado: {socio.nombre} {socio.apellido}"
    return "No existe un socio con ese DNI"

def agregar_socio(socios, dni, nombre, apellido, edad, cuota_al_dia):
    socios[dni] = Socio(nombre, apellido, dni, edad, cuota_al_dia)

def socio_mayor_edad(socios):
    if not socios:
        return "No hay socios registrados"
    mayor = max(socios.values(), key=lambda x: x.edad)
    return mayor.dni

def dar_baja_socio(socios, dni):
    if dni not in socios:
        return "El socio no existe"
    if not socios[dni].cuota_al_dia:
        return "No se puede dar de baja. El socio tiene cuotas pendientes"
    del socios[dni]
    return "Socio dado de baja exitosamente"

def pagar_cuota(socios, dni):
    if dni in socios:
        socios[dni].cuota_al_dia = True
        return "Cuota registrada como pagada"
    return "Socio no encontrado"



def version_sin_almacenamiento():
    """Versión que no almacena las ciudades"""
    total_ciudades = 0
    ciudades_por_pais = {}
    
    while True:
        ciudad = input("Ingrese nombre de la ciudad (zz para terminar): ").strip()
        if ciudad.lower() == "zz":
            break
            
        pais = input("Ingrese país: ").strip()
        total_ciudades += 1
        
        # Actualizar contador del país
        ciudades_por_pais[pais] = ciudades_por_pais.get(pais, 0) + 1
    return total_ciudades, ciudades_por_pais

def version_con_almacenamiento():
    """Versión que almacena las ciudades en una lista"""
    ciudades = []
    
    while True:
        ciudad = input("Ingrese nombre de la ciudad (zz para terminar): ").strip()
        if ciudad.lower() == "zz":
            break
            
        pais = input("Ingrese país: ").strip()
        ciudades.append([ciudad, pais])
    
    # Procesar la lista para obtener estadísticas
    ciudades_por_pais = {}
    for ciudad, pais in ciudades:
        ciudades_por_pais[pais] = ciudades_por_pais.get(pais, 0) + 1
    
    return len(ciudades), ciudades_por_pais

def mostrar_resultados(total, por_pais):
    """Muestra los resultados de cualquiera de las dos versiones"""
    print(f"\nTotal de ciudades ingresadas: {total}")
    print("\nCiudades por país:")
    for pais, cantidad in por_pais.items():
        print(f"{pais}: {cantidad}")


    # Cuenta cuántas veces aparece cada dígito en un numero.
    # Parámetro: numero (int) - El número a analizar
def contar_digitos(numero):
    numero_str = str(numero)
    conteo = {}
    for digito in numero_str:
        if digito in conteo:
            conteo[digito] = conteo[digito] + 1
        else:
            conteo[digito] = 1
            print(conteo)
    return conteo


    # Verifica si hay algún dígito que se repita.
    # Parámetro: conteo_digitos (dict) - Diccionario con el conteo de cada dígito
    # Retorna: True si hay repetidos, False si no hay
def tiene_digitos_repetidos(conteo_digitos):
    for cantidad in conteo_digitos.values():
        if cantidad > 1:
            return True
    print("No hay dígitos repetidos.")
    return False


    # Calcula la suma y cantidad de dígitos que se repiten.
    # Parámetro: conteo_digitos (dict) - Diccionario con el conteo de cada dígito
def calcular_suma_y_cantidad_repetidos(conteo_digitos):
    suma_repetidos = 0  
    cantidad_repetidos = 0
    
    # Recorrer el diccionario
    for digito, cantidad in conteo_digitos.items():
        if cantidad > 1:
            suma_repetidos = suma_repetidos + int(digito)
            cantidad_repetidos = cantidad_repetidos + 1
    print(f"Suma de dígitos repetidos: {suma_repetidos}, Cantidad de dígitos repetidos: {cantidad_repetidos}")
    return suma_repetidos, cantidad_repetidos

    # Calcula el porcentaje de números mayores a 478.
    # Parámetros: cantidad_mayores (int), total (int)
def calcular_porcentaje(cantidad_mayores, total):
    if total == 0:
        print("No se procesaron números, porcentaje es 0.")
        return 0
    
    porcentaje = (cantidad_mayores * 100) / total
    print(f"Porcentaje de números mayores que 478: {porcentaje}%")
    return porcentaje

# Calcula el promedio de los números procesados.
def calcular_promedio(suma_total, cantidad):
    if cantidad == 0:
        return 0
    
    promedio = suma_total / cantidad
    print(f"Promedio de los números procesados: {promedio}")
    return promedio

#Muestra las estadísticas de un número específico.

def mostrar_estadisticas_numero(numero, suma_rep, cant_rep):
    print(f"\nAnalizando el número: {numero}")
    print(f"Suma de dígitos repetidos: {suma_rep}")
    print(f"Cantidad de dígitos que se repiten: {cant_rep}")
    print()


def mostrar_estadisticas_finales(cant_numeros, cant_mayores, suma_total):
    if cant_numeros > 0:
        print("ESTADÍSTICAS FINALES:")
        porcentaje = calcular_porcentaje(cant_mayores, cant_numeros)
        print(f"\nPorcentaje de números mayores que 478: {porcentaje:.2f}%")
        promedio = calcular_promedio(suma_total, cant_numeros)
        print(f"\nPromedio de los números procesados: {promedio:.2f}")
        print(f"\nTotal de números procesados: {cant_numeros}")
        
        
# Normaliza una palabra quitando acentos
def normalizar(palabra):
    return ''.join(c for c in unicodedata.normalize('NFD', palabra)
                   if unicodedata.category(c) != 'Mn').lower()

# Retorna True si la palabra tiene al menos 3 vocales diferentes
def tiene_tres_vocales_diferentes(palabra):
    palabra = normalizar(palabra)
    vocales = {'a', 'e', 'i', 'o', 'u'}
    encontradas = set()

    for letra in palabra:
        if letra in vocales:
            encontradas.add(letra)
    
    return len(encontradas) >= 3

# Cuenta oraciones en un texto
def contar_oraciones(texto):
    return texto.count('.')

# Cuenta palabras en una oración
def contar_palabras(oracion):
    return len(oracion.split())


def procesar_palabras():
    texto = ""
    print("Ingrese texto (finalice con una línea que termine en '*'):")

    while True:
            linea = input()
            texto += " " + linea  # acumulamos todo el texto
            if linea.endswith('*'):
                texto = texto.rstrip('*')  # quitamos el *
                break

    # Procesar palabras
    palabras = texto.replace('.', ' ').split()
    palabras_validas = [p for p in palabras if tiene_tres_vocales_diferentes(p)]

    # Contar oraciones
    total_oraciones = contar_oraciones(texto)

    # Calcular porcentaje de oraciones con más de 5 palabras
    oraciones = texto.split('.')
    oraciones_con_mas_5 = sum(1 for o in oraciones if contar_palabras(o) > 5)

    porcentaje_mas_5 = (oraciones_con_mas_5 * 100 / total_oraciones) if total_oraciones > 0 else 0


    print("\nPalabras con al menos 3 vocales diferentes:")
    for p in palabras_validas:
        print(p)

    print("\nCantidad total de oraciones:", total_oraciones)
    print(f"Porcentaje de oraciones con más de cinco palabras: {porcentaje_mas_5:.2f}%")
    
    
#recibe una cadena de texto y retorna la cantidad de veces que aparecen cada uno de los caracteres de la cadena 
def frecuencia_caracteres(cadena):
    frecuencia = {}
    for caracter in cadena:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    print(frecuencia)
    return frecuencia



def sucesion_mira_y_deci(n):
    if n <= 0:
        return []

    lista = ["1"] 

    for _ in range(n - 1):
        actual = lista[-1]
        nuevo = ""
        count = 1

        # Recorremos el número actual para generar el siguiente
        for i in range(1, len(actual)):
            if actual[i] == actual[i - 1]:
                count += 1
            else:
                nuevo += str(count) + actual[i - 1]
                count = 1

        # Agregar el último grupo leido
        nuevo += str(count) + actual[-1]
        lista.append(nuevo)

    # Convertimos a enteros
    print([int(x) for x in lista])
    return [int(x) for x in lista]
