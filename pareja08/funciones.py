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