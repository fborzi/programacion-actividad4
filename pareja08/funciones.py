'''Devuelve los dos valores mínimos de una lista (primer y segundo mínimo) recorriéndola una sola vez.
como parametros obtiene una lista de numeros.
retorna:
None, None: si no tiene ningunnumero en la lista
None,Numero: si la lista tiene un único numero
Numero, Numero: si la lista tiene mas de un numero guarado y compara que dos numeros son mas chicos

'''
def dos_minimos(lista):
    if not lista:
        return(None,None)
    elif len(lista)==1:
        return(None,lista[0])
    if lista[0]<lista[1]:
        min1,min2=lista[0],lista[1]
    else:
        min1,min2=lista[1],lista[0]
    for elemento in lista[2:]:
        if elemento<min1:
            min2=min1
            min1=elemento
        elif elemento<min2:
            min2=elemento
    return(min1,min2)

'''Convierte un número en una lista con sus dígitos, de izquierda a derecha.
Parámetro: un número (o una cadena de dígitos). Se convierte a string y con un for se recorre toda la cadena; en el arreglo creado inicialmente vacío se usa append para almacenar cada carácter transformado a entero.
'''
def digitos(num):
    digitosT=[]
    for n in str(num):
        digitosT.append(int(n))
    return digitosT

'''Agrupa elementos iguales consecutivos de una lista y devuelve una lista de pares [valor, cantidad] indicando cuántas veces seguidas aparece cada valor.
Retorno: Tipo: lista de listas; cada elemento es una lista de dos elementos: [valor, contador].
'''
def ocurrencias(lista):
    if not lista:
        return []
    resultado=[]
    actual=lista[0]
    contador=1
    for elemento in lista[1:]:
        if elemento==actual:
            contador+=1
        else:
            resultado.append([actual,contador])
            actual=elemento
            contador=1
    resultado.append([actual,contador])
    return resultado

'''Devuelve el índice del primer elemento máximo en la lista.
parametro una lista de numeros, si la lista no tiene datos retorna None, sino compara
los numeros dentro de esa lista y lo guarda en una variable "mayor" cy su indice en otra variable
donde retorna como resultado'''
def indice_mayor(lista):
    if not lista:
        return None
    mayor=lista[0]
    indice=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
            indice=i
    return indice

'''Busca la ciudad asociada a un DNI dentro de una lista de personas.
Entrada (personas): una lista de registros con al menos 3 campos por persona: nombre(indice 0), DNI(Indice 1)
ciudad(indice 2)
Salida: la ciudad correspondiente al DNI si se encuentra; None si no hay coincidencia.
'''
def obtenerCiudad(personas, DNI):
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None  

'''Busca la provincia asociada a un DNI, usando dos listas:
- Una lista de personas con nombre, DNI y ciudad.
- Una lista de ciudades con su provincia.
Entrada:
- personas: lista de tuplas (nombre, DNI, ciudad)
- ciudades: lista de tuplas (ciudad, provincia)
- DNI: documento a buscar (string o número)
Salida:
- La provincia correspondiente al DNI si se encuentra.
- None si no hay coincidencia de DNI o ciudad.
'''
def obtenerProvincia(personas, ciudades, DNI):
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None
    for ciudad_info in ciudades:
        if ciudad_info[0].lower() == ciudad.lower():
            return ciudad_info[1]
    return None 

'''Cuenta cuántas personas viven en una provincia específica, usando su DNI para identificar la ciudad y luego la provincia.

Entrada
- personas: lista de tuplas (nombre, DNI, ciudad)
- ciudades: lista de tuplas (ciudad, provincia)
- provincia: nombre de la provincia a contar (string)

Salida
- Un número entero: cantidad de personas que viven en esa provincia.
'''
def contarPoblacion(personas, ciudades, provincia):
    contador = 0
    for persona in personas:
        prov = obtenerProvincia(personas, ciudades, persona[1])
        if prov and prov.lower() == provincia.lower():
            contador += 1
    return contador

'''Verifica si un número tiene dígitos repetidos
Entrada: n: un número entero
Salida: True si algún dígito se repite
'''
def tiene_digitos_repetidos(n):
    digitos = str(n)
    return len(set(digitos)) < len(digitos)

'''Suma los valores de los dígitos que se repiten, multiplicados por la cantidad de veces que aparecen.
Entrada:
n: un número entero
Salida:
Un número entero: la suma total de los dígitos repetidos, considerando cuántas veces aparecen.
'''
def suma_digitos_repetidos(n):
    from collections import Counter
    digitos = Counter(str(n))
    return sum(int(d) * digitos[d] for d in digitos if digitos[d] > 1)

'''Cuenta cuántos dígitos distintos se repiten en un número
Entrada:
n: un número entero
Salida:
Un número entero: cantidad de dígitos únicos que aparecen más de una vez.
'''
def cantidad_digitos_repetidos(n):
    from collections import Counter
    digitos = Counter(str(n))
    return sum(1 for d in digitos if digitos[d] > 1)

'''Cuenta cuántas veces aparece cada carácter en una cadena.
Entrada: cadena: un string 
Salida: Un diccionario con cada carácter como clave y su cantidad como valor.
'''
def frecuencia_caracteres(cadena):
    frecuencia = {}
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

'''Carga productos en un diccionario, solicitando los datos por consola hasta que se ingrese -1 como código.
Entrada:
No recibe parámetros.
Solicita por consola los siguientes datos por cada producto:
- código: entero único
- tipo: texto (convertido a minúsculas)
- descripción: texto libre
- stock_actual: entero
- stock_minimo: entero
- precio_unitario: número decimal

Salida:
Devuelve un diccionario con estructura
'''
def cargar_productos():
    productos = {}
    while True:
        codigo = int(input("Código de producto (-1 para terminar): "))
        if codigo == -1:
            break
        tipo = input("Tipo de producto: ").lower()
        descripcion = input("Descripción: ")
        stock_actual = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio_unitario = float(input("Precio unitario: "))
        productos[codigo] = {
            "tipo": tipo,
            "descripcion": descripcion,
            "stock_actual": stock_actual,
            "stock_minimo": stock_minimo,
            "precio_unitario": precio_unitario
        }
    return productos
'''Ejecuta 6 consultas específicas sobre un diccionario de productos previamente cargado, mostrando
 resultados por consola.
 Entrada:
 productos: diccionario
 Salida: No devuelve datos. Imprime directamente los resultados de cada consulta
'''
def resolver_consultas(productos):
    # a. ¿Se puede vender el producto 124?
    print("\na. ¿Se puede vender el producto 124?")
    if 124 in productos and productos[124]["stock_actual"] > 0:
        print("  Sí, hay stock disponible.")
    else:
        print("  No, no hay stock disponible o el producto no existe.")

    # b. Productos por debajo del stock mínimo
    print("\nb. Productos por debajo del stock mínimo:")
    for codigo, datos in productos.items():
        if datos["stock_actual"] < datos["stock_minimo"]:
            print(f"  Código: {codigo} | Descripción: {datos['descripcion']}")

    # c. Cantidad de productos lácteos
    lacteos = sum(1 for datos in productos.values() if datos["tipo"] == "lácteo")
    print(f"\nc. Cantidad de productos lácteos: {lacteos}")

    # d. Producto de almacén con menor stock actual
    almacen = [(codigo, datos) for codigo, datos in productos.items() if datos["tipo"] == "almacén"]
    if almacen:
        menor = min(almacen, key=lambda x: x[1]["stock_actual"])
        print(f"\nd. Producto de almacén con menor stock: Código {menor[0]} | {menor[1]['descripcion']}")
    else:
        print("\nd. No hay productos de almacén registrados.")

    # e. Descripción del producto 3148
    print("\ne. Descripción del producto 3148:")
    if 3148 in productos:
        print(f"  {productos[3148]['descripcion']}")
    else:
        print("  No existe el producto con código 3148.")

    # f. Tipo con menor cantidad total de unidades disponibles
    tipo_unidades = {}
    for datos in productos.values():
        tipo = datos["tipo"]
        tipo_unidades[tipo] = tipo_unidades.get(tipo, 0) + datos["stock_actual"]
    if tipo_unidades:
        tipo_menor = min(tipo_unidades.items(), key=lambda x: x[1])
        print(f"\nf. Tipo con menor cantidad de unidades disponibles: {tipo_menor[0]} ({tipo_menor[1]} unidades)")
    else:
        print("\nf. No hay productos registrados.")

'''Procesa un pedido de productos, actualiza el stock y calcula el monto total de venta
Entrada:- productos: diccionario

Salida:
- monto_total: suma de los precios unitarios de los productos vendidos.
- vendidos: lista de códigos que fueron efectivamente vendidos (stock > 0).
'''
def procesar_pedido(productos, pedido):
    monto_total = 0
    vendidos = []
    for codigo in pedido:
        if codigo in productos and productos[codigo]["stock_actual"] > 0:
            monto_total += productos[codigo]["precio_unitario"]
            productos[codigo]["stock_actual"] -= 1
            vendidos.append(codigo)
    return monto_total, vendidos
'''Genera los primeros n términos de la sucesión “mirá y decí”, comenzando desde "1".
Entrada:
- n: número entero positivo que indica cuántos términos generar.

Salida:
- Una lista de strings, donde cada elemento es un término de la sucesión.
'''
def sucesion_mira_y_deci(n):
    def describir(numero):
        resultado = ""
        i = 0
        while i < len(numero):
            contador = 1
            while i + 1 < len(numero) and numero[i] == numero[i + 1]:
                contador += 1
                i += 1
            resultado += str(contador) + numero[i]
            i += 1
        return resultado

    sucesion = ["1"]
    for _ in range(n - 1):
        siguiente = describir(sucesion[-1])
        sucesion.append(siguiente)
    return sucesion


def minimo_elemento(lista: list | str | None): # Ejercicio 6
    """
    Devuelve el menor elemento de la lista.
    
    Args:
        lista (list | str | None): Lista de elementos a evaluar.
    
    Returns:
        int: El menor elemento encontrado.
        str: El menor elemento encontrado.
        None: Si la lista esta vacia o es None.
    
    Examples:
        >>> minimo_elemento([4, 8, 15, 16, 23, 42])
        4
        >>> minimo_elemento("PYTHON")
        'H'
        >>> minimo_elemento([])
        None
        >>> minimo_elemento(None)
        None
    """
    if lista == [] or lista == None:
        return None
    else:
        return min(lista)


def piedra_papel_tijera(uno: str, dos: str): # Ejercicio 8
    """
    Define al ganador del juego.
    
    Args:
        uno (str): Eleccion del jugador uno
        dos (str): Eleccion del jugador dos
    
    Returns:
        int: Jugador ganador.
    
    Raises:
        ValueError: El valor ingresado no corresponde a un elemento existente.
    
    Examples:
        >>> piedra_papel_tijera("piedra", "tijera")
        1
        >>> piedra_papel_tijera("piedra", "papel")
        2
        >>> piedra_papel_tijera("tijera", "tijera")
        0
        >>> piedra_papel_tijera("lagarto", "cuchara")
        ValueError: Se ingreso un elemento invalido.
    """
    elementos = ["piedra", "papel", "tijera"]
    uno = uno.lower()
    dos = dos.lower()
    ind1 = None
    ind2 = None
    dif = None
    
    if not (uno in elementos and dos in elementos):
        raise ValueError("Se ingreso un elemento invalido.")
        
    else:
        for i, elem in enumerate(elementos):
            if uno == elem:
                ind1 = i
            if dos == elem:
                ind2 = i
        
        dif = ind1 - ind2
        if dif == 0:
            return 0
        elif dif == -1 or dif == 2:
            return 2
        elif dif == -2 or dif == 1:
            return 1


def borrar_adyacentes(lista: list): # Ejercicio 10
    """
    Devuelve una lista que elimina elementos repetidos adyacentes a partir de una lista de elementos de 1 de longitud.
    
    Args:
        lista (list): Lista de elementos a evaluar.
    
    Returns:
        list: Lista de elementos sin adyacentes repetidos.
    
    Raises:
        ValueError: La lista debe contener elementos de un unico caracter.
    
    Examples:
        >>> borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a'])
        ['a', '*', 'b', '=', 'c', 'a']
        >>> borrar_adyacentes(['asd', 'a', '1'])
        ValueError: La lista debe contener elementos de un unico caracter.
    """
    lista_res = []
    lista_res.append(lista[0])
    
    for i in lista:
        if len(i) != 1:
            raise ValueError("La lista debe contener elementos de un unico caracter")
        if not i == lista_res[-1]:
            lista_res.append(i)
            
    return lista_res


def suma_digitos(n: int): # Ejercicio 12-a
    """
    Devuelve la sumatoria de los digitos del numero.
    
    Args:
        n (int): Numero a evaluar.
    
    Returns:
        int: Sumatoria de los digitos.
    
    Raises:
        ValueError: El elemento debe ser de tipo entero.
        ValueError: El numero debe ser positivo.
    
    Examples:
        >>> suma_digitos(92738)
        29
        >>> suma_digitos(154)
        10
        >>> suma_digitos(154.0)
        ValueError: El elemento debe ser de tipo entero.
        >>> suma_digitos(-219)
        ValueError: El numero debe ser positivo.
    """
    if not isinstance(n, int):
        raise ValueError("El elemento debe ser de tipo entero.")
    if n < 0:
        raise ValueError("El numero debe ser positivo.")
        
    n = str(n)
    res = 0
    for i in n:
        res += int(i)
    
    return res


def sumatoria_digitos(lista: list): # Ejercicio 12-b
    """
    Devuelve una lista de numeros cuyos digitos han sido sumados.
    
    Args:
        lista (list): Lista de elementos a evaluar.
    
    Returns:
        list: Lista de numeros.
    
    Examples:
        >>> sumatoria_digitos([154, 27890, 111, 43])
        [10, 26, 3, 7]
        >>> sumatoria_digitos([8383, 747, 27]
        [22, 18, 9]
    """
    lista_res = []
    for i in lista:
        lista_res.append(suma_digitos(i))

    return lista_res


def dos_sumandos(lista: list, resultado: float): # Ejercicio 14
    """
    Devuelve una lista con los dos indices donde su suma es igual al resultado
    
    Args:
        lista (list): Lista de numeros a evaluar.
        resultado (float): Resultado esperado.
    
    Returns:
        list: Dos indices
        None: Si ninguna combinacion de indices satisface el resultado.
        
    Examples:
        >>> dos_sumandos([2, 7, 11, 15], 17)
        [0, 3]
        >>> dos_sumandos([8383, 387, 27], 774)
        [1, 1]
        >>> dos_sumandos([873, 7, 12, 5], 20)
        None
    """
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]


def digitos_repetidos(n: float): # Ejercicio 18
    """
    Devuelve una lista de numeros unicos a partir de otro.
    
    Args:
        n (float): Numero a evaluar.
    
    Returns:
        set: Valores unicos.
    
    Raises:
        ValueError: El valor debe ser un numero.
        
    Examples:
        >>> digitos_repetidos(-36783.5)
        {3, 5, 6, 7, 8}
        >>> digitos_repetidos(73)
        {3. 7}
        >>> digitos_repetidos("gsg")
        ValueError: El valor debe ser un numero.
    """
    if not isinstance(n, int or float):
        raise ValueError("El valor debe ser un numero.")
    
    res = set()
    n = str(abs(n))
    n = n.replace(".", "")
    for i in n:
        res.add(int(i))
    
    return list(res)