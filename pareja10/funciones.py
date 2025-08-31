def minimo_elemento(lista):
    """"
    Devuelve el mínimo elemento de la lista o None si la lista está vacía
    Lanza TypeError si los elementos no son comparables entre sí
    """
    if not lista:
        return None
    minimo = lista[0]
    for elemento in lista[1:]:
        if elemento < minimo:
            minimo = elemento
    return minimo

def dos_minimos(lista):
    """
    Devuelve una tupla con los dos menores valores de lista en orden ascendente
    Si la lista tiene menos de dos elementos, retorna None por cada elemento faltante
    """
    it = iter(lista)
    try:
        min1 = next(it)
    except StopIteration:
        return (None, None)
    min2 = None
    for x in it:
        if x < min1:
            min2 = min1
            min1 = x
        elif min2 is None or x < min2:
            min2 = x
    return (min1, min2)

def piedra_papel_tijera(uno, dos):
    uno = str(uno).strip().lower()
    dos = str(dos).strip().lower()
    validos = {'piedra', 'papel', 'tijera'}
    if uno not in validos or dos not in validos:
        raise ValueError("Entrada inválida: debe ser 'piedra', 'papel' o 'tijera'")
    if uno == dos:
        return 0
    vence = {'piedra': 'tijera', 'tijera': 'papel', 'papel': 'piedra'}
    return 1 if vence[uno] == dos else 2

def digitos(numero):
    s = str(numero).strip()
    if s.startswith('-'):
        s = s[1:]
    if not s.isdigit():
        raise ValueError("El parámetro debe representar un entero")
    return [int(ch) for ch in s]

def borrar_adyacentes(lista):
    if not lista:
        return []
    resultado = [lista[0]]
    for elem in lista[1:]:
        if elem != resultado[-1]:
            resultado.append(elem)
    return resultado

def suma_digitos(n):
    if not isinstance(n, int):
        raise ValueError("n debe ser un entero")
    n = abs(n)
    return 0 if n == 0 else sum(int(d) for d in str(n))

def sumatoria_digitos(lista):
    if not hasattr(lista, "__iter__"):
        raise ValueError("Se espera una lista iterable de enteros")
    return [suma_digitos(int(x)) for x in lista]

def indice_mayor(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía")
    mayor_idx = 0
    mayor_val = lista[0]
    for i, v in enumerate(lista[1:], start=1):
        if v > mayor_val:
            mayor_val = v
            mayor_idx = i
    return mayor_idx

def dos_sumandos(lista, resultado):
    if not hasattr(lista, "__iter__"):
        raise ValueError("Se espera una lista de números")
    seen = {}
    for i, val in enumerate(lista):
        comp = resultado - val
        if comp in seen:
            return [seen[comp], i]
        seen[val] = i
    return None
