import unicodedata

def digitos_repetidos(numero):
    """
    Encuentra los dígitos que aparecen más de una vez en un número.
    
    Esta función recorre cada carácter del número y determina qué dígitos
    se repiten, retornando una lista ordenada de los dígitos repetidos.
    
    Args:
        numero (int): El número entero a analizar.
    
    Returns:
        list: Una lista ordenada de enteros con los dígitos que aparecen
              más de una vez en el número. Si no hay dígitos repetidos,
              retorna una lista vacía.
    """          
    numero = str(numero)
    repetidos = set()
    vistos = set()
    
    for x in numero:
        if not x.isdigit():
            continue
        if x in vistos:
            repetidos.add(int(x))
        else:
            vistos.add(x)
    return list(repetidos)

def letras_repetidas(palabra):
    """
    Encuentra las letras que aparecen más de una vez en una palabra.
    
    Esta función recorre cada carácter de la palabra y determina qué letras
    se repiten, retornando una lista con las letras repetidas. Solo considera
    caracteres alfabéticos e ignora la distinción entre mayúsculas y minúsculas.
    
    Args:
        palabra (str): La palabra o cadena de texto a analizar.
    
    Returns:
        list: Una lista con las letras (en minúsculas) que aparecen más de una 
              vez en la palabra. Si no hay letras repetidas, retorna una lista vacía.
              El orden de las letras en la lista corresponde al orden en que se
              detectaron como repetidas.
    """          
    palabra = palabra.lower()
    vistos = set()
    repetidos = set()
    
    for letra in palabra:
        if letra.isalpha():
            if letra in vistos:
                repetidos.add(letra)
            else:
                vistos.add(letra)           
    return list(repetidos)

def frecuencia_caracteres(cadena):
    """
    Calcula la frecuencia de aparición de cada carácter en una cadena.
    
    Esta función recorre cada carácter de la cadena y cuenta cuántas veces
    aparece cada uno, retornando un diccionario con los caracteres como claves
    y sus frecuencias como valores.
    
    Args:
        cadena (str): La cadena de texto a analizar.
    
    Returns:
        dict: Un diccionario donde las claves son los caracteres que aparecen
              en la cadena y los valores son enteros que representan cuántas
              veces aparece cada carácter.
    """          
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def sucesion_mira_y_deci(n):
    """
    La secuencia comienza con "1" y cada término siguiente describe
    el término anterior contando los dígitos consecutivos iguales. Por ejemplo:
    - 1 se lee como "un 1" → "11"
    - 11 se lee como "dos 1" → "21"
    - 21 se lee como "un 2, un 1" → "1211"
    - 1211 se lee como "un 1, un 2, dos 1" → "111221"
    
    Args:
        n (int): El número de términos de la secuencia a generar. Debe ser >= 1.
    
    Returns:
        list: Una lista de enteros que representa los primeros n términos de la
              secuencia. Si n <= 0, retorna una lista vacía.
    """          
    
    if n <= 0:
        return []

    sucesion = ["1"]

    for _ in range(1, n):
        anterior = sucesion[-1]
        nuevo = ""
        contador = 1

        for i in range(1, len(anterior)):
            if anterior[i] == anterior[i - 1]:
                contador += 1
            else:
                nuevo += str(contador) + anterior[i - 1]
                contador = 1

        nuevo += str(contador) + anterior[-1]
        sucesion.append(nuevo)

    return [int(x) for x in sucesion]

def normalizar(texto):
    """
    Normaliza un texto removiendo todos los caracteres diacríticos (acentos y tildes).
    
    Esta función convierte el texto a minúsculas y elimina todos los signos
    diacríticos (acentos, tildes, diéresis, etc.) manteniendo solo las letras
    base. Utiliza la normalización Unicode NFD para separar los caracteres base
    de sus marcas diacríticas.
    
    Args:
        texto (str): El texto a normalizar.
    
    Returns:
        str: El texto en minúsculas sin caracteres diacríticos.
    """    
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def tiene_tres_vocales_diferentes(palabra):
    """
    Verifica si una palabra contiene al menos tres vocales diferentes.
    
    Esta función analiza una palabra y determina si contiene tres o más vocales
    distintas (sin importar cuántas veces se repita cada una). Las vocales
    consideradas son: a, e, i, o, u (en minúsculas).
    
    Args:
        palabra (str): La palabra a analizar.
    
    Returns:
        bool: True si la palabra contiene al menos 3 vocales diferentes,
              False en caso contrario.
    """          
    vocales = {'a', 'e', 'i', 'o', 'u'}
    usadas = {letra for letra in palabra if letra in vocales}
    return len(usadas) >= 3 

def contar_ciudades():
    """
    Solicita al usuario ingresar ciudades agrupadas por país y cuenta cuántas
    ciudades se ingresaron en total y por cada país.
    
    Esta función interactiva permite al usuario ingresar múltiples ciudades
    organizadas por país. El usuario puede ingresar tantas ciudades como desee
    para cada país, y tantos países como desee. La entrada termina cuando el
    usuario escribe 'zz' como ciudad.
    
    Flujo de la función:
        1. Solicita el nombre de una ciudad
        2. Si la ciudad no es 'zz', solicita el país correspondiente
        3. Registra la ciudad bajo ese país
        4. Repite hasta que el usuario ingrese 'zz'
        5. Muestra el total de ciudades y el desglose por país
    
    Args:
        Ninguno. La función obtiene datos mediante input() del usuario.
    
    Returns:
        None. La función imprime los resultados directamente.
    """    
    ciudades_por_pais = {}
    total = 0

    ciudad = input("Ingrese una ciudad (o 'zz' para terminar): ")

    while ciudad.lower() != "zz":
        pais = input(f"Ingrese el país de {ciudad}: ")

        total += 1
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

        ciudad = input("Ingrese otra ciudad (o 'zz' para terminar): ")

    print(f"Cantidad total de ciudades: {total}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"{pais}: {cantidad}")
        
def contar_ciudades_lista():
    """
    Solicita al usuario ingresar ciudades con sus países y cuenta cuántas
    ciudades se ingresaron en total y por cada país.
    
    Esta función interactiva permite al usuario ingresar múltiples ciudades
    junto con sus países correspondientes. A diferencia de contar_ciudades(),
    esta versión almacena las ciudades en una lista de tuplas (ciudad, país)
    antes de realizar el conteo, lo que permite procesar los datos posteriormente.
    
    Flujo de la función:
        1. Solicita el nombre de una ciudad
        2. Si la ciudad no es 'zz', solicita el país correspondiente
        3. Almacena la tupla (ciudad, país) en una lista
        4. Repite hasta que el usuario ingrese 'zz'
        5. Procesa la lista para contar ciudades por país
        6. Muestra el total de ciudades y el desglose por país
    
    Args:
        Ninguno. La función obtiene datos mediante input() del usuario.
    
    Returns:
        None. La función imprime los resultados directamente.
    """    
    ciudades = []

    ciudad = input("Ingrese una ciudad (o 'zz' para terminar): ")

    while ciudad.lower() != "zz":
        pais = input(f"Ingrese el país de {ciudad}: ")
        ciudades.append([ciudad, pais])
        ciudad = input("Ingrese otra ciudad (o 'zz' para terminar): ")

    total = len(ciudades)
    ciudades_por_pais = {}

    for ciudad, pais in ciudades:
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

    print(f"Cantidad total de ciudades: {total}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"{pais}: {cantidad}")

def cargar_productos():
    """
    Solicita al usuario ingresar información de productos y los almacena en un diccionario.
    
    Esta función interactiva permite al usuario cargar múltiples productos con sus
    características: tipo, descripción, stock actual, stock mínimo y precio unitario.
    Cada producto se identifica con un código único y la carga finaliza cuando el
    usuario ingresa -1 como código.
    
    Flujo de la función:
        1. Solicita el código del producto
        2. Si el código no es -1, solicita todos los datos del producto:
           - Tipo de producto
           - Descripción
           - Stock actual
           - Stock mínimo
           - Precio unitario
        3. Almacena el producto en el diccionario con el código como clave
        4. Repite hasta que el usuario ingrese -1
        5. Retorna el diccionario con todos los productos
    
    Args:
        Ninguno. La función obtiene datos mediante input() del usuario.
    
    Returns:
        dict: Un diccionario donde las claves son códigos de productos (int) y
              los valores son diccionarios con la siguiente estructura:
              {
                  "tipo": str,
                  "descripcion": str,
                  "stock": int,
                  "stock_min": int,
                  "precio": float
              }
    """
    productos = {}

    codigo = int(input("Ingrese el código del producto (-1 para terminar): "))

    while codigo != -1:
        tipo = input("Tipo de producto: ")
        descripcion = input("Descripción: ")
        stock = int(input("Stock actual: "))
        stock_min = int(input("Stock mínimo: "))
        precio = float(input("Precio unitario: "))

        productos[codigo] = {
            "tipo": tipo,
            "descripcion": descripcion,
            "stock": stock,
            "stock_min": stock_min,
            "precio": precio
        }

        codigo = int(input("Ingrese el código del producto (-1 para terminar): "))

    return productos


def puede_vender(productos, codigo):
    """
    Verifica si es posible vender una unidad de un producto específico.
    
    Esta función comprueba si un producto existe en el inventario y si tiene
    stock disponible para realizar una venta. Informa al usuario si la venta
    es posible o no mediante un mensaje impreso.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo el campo "stock".
        codigo (int): El código del producto que se desea vender.
    
    Returns:
        None. La función imprime un mensaje indicando si se puede vender o no.
    """    
    if codigo in productos and productos[codigo]["stock"] > 0:
        print(f"Se puede vender una unidad del producto {codigo}.")
    else:
        print(f"No se puede vender el producto {codigo}.")


def productos_bajo_stock(productos):
    """
    Muestra todos los productos cuyo stock actual está por debajo del stock mínimo.
    
    Esta función recorre el inventario de productos e identifica aquellos que tienen
    un nivel de stock por debajo del stock mínimo recomendado, imprimiendo una lista
    con el código y descripción de cada producto en esta condición.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo los campos:
                         - "stock": int (stock actual)
                         - "stock_min": int (stock mínimo recomendado)
                         - "descripcion": str (descripción del producto)
    
    Returns:
        None. La función imprime directamente los resultados.
    """    
    print("Productos por debajo del stock mínimo:")
    for cod, datos in productos.items():
        if datos["stock"] < datos["stock_min"]:
            print(f"Código: {cod} - {datos['descripcion']}")


def contar_lacteos(productos):
    """
    Cuenta cuántos productos de tipo "lácteo" hay en el inventario.
    
    Esta función recorre el diccionario de productos y cuenta aquellos cuyo
    tipo sea "lácteo" (sin distinción entre mayúsculas y minúsculas), luego
    imprime el resultado en un mensaje descriptivo.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo el campo:
                         - "tipo": str (tipo o categoría del producto)
    
    Returns:
        None. La función imprime directamente el resultado.
    """    
    cantidad = sum(1 for datos in productos.values() if datos["tipo"].lower() == "lácteo")
    print(f"El supermercado comercializa {cantidad} productos lácteos.")


def almacen_menor_stock(productos):
    """
    Encuentra y muestra el producto de tipo "almacén" con menor stock.
    
    Esta función busca entre todos los productos de tipo "almacén" (case-insensitive)
    y determina cuál tiene el menor nivel de stock, mostrando su información.
    Si no hay productos de almacén, informa que no existen.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo los campos:
                         - "tipo": str (tipo o categoría del producto)
                         - "stock": int (cantidad en inventario)
                         - "descripcion": str (descripción del producto)
    
    Returns:
        None. La función imprime directamente el resultado.
    """    
    min_stock = None
    producto_min = None
    for cod, datos in productos.items():
        if datos["tipo"].lower() == "almacén":
            if min_stock is None or datos["stock"] < min_stock:
                min_stock = datos["stock"]
                producto_min = (cod, datos["descripcion"])
    if producto_min:
        print(f"Producto de almacén con menor stock: {producto_min}")
    else:
        print("No hay productos de almacén.")


def descripcion_por_codigo(productos, codigo):
    """
    Busca y muestra la descripción de un producto dado su código.
    
    Esta función verifica si existe un producto con el código especificado
    en el inventario y muestra su descripción. Si el producto no existe,
    informa al usuario que no se encontró.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo el campo:
                         - "descripcion": str (descripción del producto)
        codigo (int): El código del producto a buscar.
    
    Returns:
        None. La función imprime directamente el resultado.
    """    
    if codigo in productos:
        print(f"Descripción del producto {codigo}: {productos[codigo]['descripcion']}")
    else:
        print(f"No existe producto con código {codigo}.")


def tipo_menor_stock_total(productos):
    """
    Identifica el tipo de producto con menor cantidad total de stock en el inventario.
    
    Esta función agrupa los productos por tipo, suma el stock total de cada tipo,
    y determina cuál tiene la menor cantidad acumulada de stock. Útil para identificar
    qué categoría de productos necesita mayor atención en términos de reabastecimiento.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con
                         la información del producto, incluyendo los campos:
                         - "tipo": str (tipo o categoría del producto)
                         - "stock": int (cantidad en inventario)
    
    Returns:
        None. La función imprime directamente el resultado.
    """    
    tipos = {}
    for datos in productos.values():
        tipo = datos["tipo"]
        tipos[tipo] = tipos.get(tipo, 0) + datos["stock"]
    tipo_min = min(tipos, key=tipos.get)
    print(f"Tipo con menor cantidad total en stock: {tipo_min}")


def procesar_pedido(productos, pedido):
    """
    Procesa un pedido de productos, actualizando el inventario y calculando el total.
    
    Esta función recibe una lista de códigos de productos solicitados, verifica
    que cada producto exista y tenga stock disponible, actualiza el inventario
    decrementando el stock, calcula el monto total del pedido, y genera un
    resumen con los productos vendidos.
    
    Args:
        productos (dict): Diccionario de productos donde las claves son códigos
                         de productos (int) y los valores son diccionarios con:
                         - "stock": int (cantidad en inventario)
                         - "precio": float (precio unitario del producto)
        pedido (list): Lista de códigos de productos (int) solicitados en el pedido.
                      Puede contener códigos duplicados para múltiples unidades.
    
    Returns:
        None. La función imprime directamente los resultados y modifica el
        diccionario productos in-place.
    """    
    total = 0
    vendidos = []

    for codigo in pedido:
        if codigo in productos and productos[codigo]["stock"] > 0:
            productos[codigo]["stock"] -= 1
            total += productos[codigo]["precio"]
            vendidos.append(codigo)

    print(f"Total a pagar: ${total:.2f}")
    print(f"Productos efectivamente vendidos: {vendidos}")
    
def cargar_peliculas():
    """
    Permite al usuario cargar información de películas de forma interactiva.
    
    Esta función solicita al usuario ingresar múltiples películas con sus datos:
    título, director, año de estreno y actores principales. Cada película se
    almacena en un diccionario que se retorna al finalizar la carga. El proceso
    continúa hasta que el usuario ingresa 'fin' como título.
    
    Flujo de la función:
        1. Solicita el título de la película
        2. Si no es 'fin', solicita:
           - Director
           - Año de estreno
           - Lista de actores principales (uno por uno hasta ingresar 'fin')
        3. Almacena la película en el diccionario con el título como clave
        4. Repite hasta que se ingrese 'fin' como título
        5. Retorna el diccionario completo de películas
    
    Args:
        Ninguno. La función obtiene todos los datos mediante input() del usuario.
    
    Returns:
        dict: Diccionario donde las claves son títulos de películas (str) y
              los valores son diccionarios con la siguiente estructura:
              {
                  "director": str,
                  "anio": int,
                  "actores": list[str]
              }
    """          
    peliculas = {}

    titulo = input("Ingrese el título de la película ('fin' para terminar): ")

    while titulo.lower() != "fin":
        director = input("Director: ")
        anio = int(input("Año de estreno: "))

        actores = []
        print("Ingrese los actores principales (escriba 'fin' para terminar):")
        actor = input("Actor: ")
        while actor.lower() != "fin":
            actores.append(actor)
            actor = input("Actor: ")

        peliculas[titulo] = {
            "director": director,
            "anio": anio,
            "actores": actores
        }

        print()
        titulo = input("Ingrese el título de la película ('fin' para terminar): ")

    return peliculas


def cantidad_peliculas_por_director(peliculas):
    """
    Cuenta cuántas películas ha dirigido cada director en el catálogo.
    
    Esta función recibe un diccionario de películas y agrupa la información
    por director, contando cuántas películas ha dirigido cada uno. Luego
    muestra el resultado y retorna el diccionario con los conteos.
    
    Args:
        peliculas (dict): Diccionario donde las claves son títulos de películas (str)
                         y los valores son diccionarios con la información de cada
                         película, incluyendo el campo:
                         - "director": str (nombre del director)
    
    Returns:
        dict: Diccionario donde las claves son nombres de directores (str) y
              los valores son enteros que representan la cantidad de películas
              dirigidas por cada director.
    """          
    conteo = {}
    for datos in peliculas.values():
        dir = datos["director"]
        conteo[dir] = conteo.get(dir, 0) + 1

    print("Cantidad de películas dirigidas por cada director:")
    for director, cant in conteo.items():
        print(f"{director}: {cant}")

    return conteo


def director_mas_peliculas(peliculas):
    """
    Identifica y muestra el director con más películas en el catálogo.
    
    Esta función utiliza la función cantidad_peliculas_por_director() para obtener
    el conteo de películas por director, y luego determina cuál director tiene
    la mayor cantidad de películas. Si no hay películas cargadas, informa al usuario.
    
    Args:
        peliculas (dict): Diccionario donde las claves son títulos de películas (str)
                         y los valores son diccionarios con la información de cada
                         película, incluyendo el campo:
                         - "director": str (nombre del director)
    
    Returns:
        None. La función imprime directamente el resultado.
    """    
    conteo = cantidad_peliculas_por_director(peliculas)
    if conteo:
        max_director = max(conteo, key=conteo.get)
        print(f"El director con más películas es {max_director} ({conteo[max_director]} películas).")
    else:
        print("No hay películas cargadas.")


def actores_de_pelicula(peliculas, titulo):
    """
    Muestra los actores principales de una película específica.

    Esta función busca una película dentro del diccionario proporcionado.
    Si el título existe, imprime en pantalla los nombres de los actores
    principales asociados a esa película. Si no se encuentra el título,
    informa que la película no existe en el registro.

    Args:
        peliculas (dict): Diccionario donde las claves son títulos de películas (str)
                          y los valores son diccionarios con la clave "actores"
                          que contiene una lista de nombres de actores (list[str]).
        titulo (str): Título de la película que se desea consultar.

    Returns:
        None. La función imprime directamente los resultados en consola.
    """
    if titulo in peliculas:
        print(f"Actores principales de '{titulo}':")
        for actor in peliculas[titulo]["actores"]:
            print(f"- {actor}")
    else:
        print(f"No existe una película con el título '{titulo}'.")


def peliculas_de_actor(peliculas, actor_buscado):
    """
    Muestra las películas en las que participó un actor específico.

    Esta función recorre el diccionario de películas para buscar en cuáles
    de ellas aparece el actor indicado. Si el actor figura en alguna película,
    se imprimen los títulos encontrados. En caso contrario, informa que el actor
    no participó en ninguna película registrada.

    Args:
        peliculas (dict): Diccionario donde las claves son títulos de películas (str)
                          y los valores son diccionarios con la clave "actores"
                          que contiene una lista de nombres de actores (list[str]).
        actor_buscado (str): Nombre del actor que se desea buscar.

    Returns:
        None. La función imprime directamente los resultados en consola.
    """
    print(f"Películas en las que participó {actor_buscado}:")
    encontradas = [titulo for titulo, datos in peliculas.items() if actor_buscado in datos["actores"]]
    if encontradas:
        for t in encontradas:
            print(f"- {t}")
    else:
        print("No participó en ninguna película registrada.")                                                