"""
TECNICATURA SUPERIOR EN DESARROLLO DE SOFTWARE
PROGRAMACIÓN - 2025
Docente: Borzi Franco

TRABAJO PRÁCTICO IV - Archivo de Funciones
Este archivo contiene todas las funciones utilizadas en los ejercicios del TP4
"""


# ============================================================================
# EJERCICIO 6: Mínimo elemento
# ============================================================================
def minimo_elemento(lista):
    """
    Encuentra el elemento mínimo de una lista.
    
    Parámetros:
        lista: Una lista de elementos comparables entre sí
        
    Retorna:
        El elemento mínimo de la lista, o None si la lista está vacía
    """
    # Si la lista está vacía, retornamos None
    if len(lista) == 0:
        return None
    
    # Asumimos que el primer elemento es el mínimo
    minimo = lista[0]
    
    # Recorremos la lista completa
    for elemento in lista:
        # Si encontramos un elemento menor, lo guardamos como nuevo mínimo
        if elemento < minimo:
            minimo = elemento
    
    # Retornamos el mínimo encontrado
    return minimo


#============================================================================
# Ejercicio 8:
# Juego de Piedra, Papel o Tijera
# ============================================================================


def piedra_papel_tijera(uno, dos):
    """
    Determina el ganador del juego Piedra, Papel o Tijera.
    
    Reglas:
    - Piedra vence a Tijera (la rompe)
    - Tijera vence a Papel (lo corta)
    - Papel vence a Piedra (la envuelve)
    
    Parámetros:
        uno: Elección del jugador 1 ('piedra', 'papel' o 'tijera')
        dos: Elección del jugador 2 ('piedra', 'papel' o 'tijera')
        
    Retorna:
        1 si gana el jugador 1
        2 si gana el jugador 2
        0 si hay empate
    """
    # Convertimos ambas elecciones a minúsculas para ignorar mayúsculas/minúsculas
    uno = uno.lower()
    dos = dos.lower()
    
    # Si ambos eligieron lo mismo, es empate
    if uno == dos:
        return 0
    
    # Verificamos los casos en que gana el jugador 1
    if (uno == "piedra" and dos == "tijera") or \
       (uno == "tijera" and dos == "papel") or \
       (uno == "papel" and dos == "piedra"):
        return 1
    
    # En cualquier otro caso, gana el jugador 2
    return 2

#============================================================================
# Ejercicio 10:
# Función que elimina caracteres adyacentes repetidos
# ============================================================================


def borrar_adyacentes(lista):
    """
    Elimina caracteres adyacentes repetidos de una lista.
    Mantiene solo una ocurrencia de cada grupo de caracteres repetidos consecutivos.
    
    Parámetros:
        lista: Lista de caracteres (strings de longitud 1)
        
    Retorna:
        Nueva lista sin caracteres adyacentes repetidos
    """
    # Si la lista está vacía o tiene un solo elemento, la retornamos tal cual
    if len(lista) <= 1:
        return lista
    
    # Creamos una nueva lista que contendrá el resultado
    resultado = []
    
    # Agregamos el primer elemento (siempre se incluye)
    resultado.append(lista[0])
    
    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(lista)):
        # Solo agregamos el elemento si es diferente al anterior
        if lista[i] != lista[i - 1]:
            resultado.append(lista[i])
    
    return resultado

# ============================================================================
# EJERCICIO 12: Suma de dígitos y sumatoria de dígitos
# ============================================================================
def digitos(n):
    """
    Convierte un número entero en una lista de sus dígitos.

    Args:
        n (int): Número entero positivo o negativo.

    Returns:
        list: Lista de dígitos como enteros.

    Ejemplo:
        >>> digitos(18413)
        [1, 8, 4, 1, 3]
    """
    # Convertimos el número a string para poder recorrer cada carácter
    # Por ejemplo: 18413 → "18413"
    cadena = str(n)

    # Recorremos cada carácter de la cadena y lo convertimos a entero
    # Usamos una lista por comprensión para hacerlo en una sola línea
    # Por ejemplo: "1" → 1, "8" → 8, etc.
    lista_digitos = [int(d) for d in cadena]

    # Retornamos la lista de dígitos
    return lista_digitos


def suma_digitos(n):
    """
    Retorna la suma de los dígitos de un número entero.
    
    Args:
        n: Número entero positivo
    
    Returns:
        Suma de los dígitos
    """
    return sum(digitos(n))


def sumatoria_digitos(lista):
    """
    Retorna una lista con la suma de los dígitos de cada número.
    
    Args:
        lista: Lista de números enteros positivos
    
    Returns:
        Lista con las sumas de dígitos
    
    Ejemplo:
        >>> sumatoria_digitos([154, 27890, 111, 43])
        [10, 26, 3, 7]
    """
    return [suma_digitos(n) for n in lista]

# ============================================================================
# EJERCICIO 14: Dos sumandos
# ============================================================================
def dos_sumandos(lista, resultado):
    """
    Retorna los índices de dos elementos cuya suma da el resultado esperado.
    
    Args:
        lista: Lista de números
        resultado: Número objetivo
    
    Returns:
        Lista con dos índices o None si no se encuentra
    
    Ejemplo:
        >>> dos_sumandos([2, 7, 11, 15], 17)
        [0, 3]
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None

# ============================================================================
# EJERCICIO 18: Digitos repetidos
# ============================================================================
def digitos_repetidos(n):
    """
    Recibe un número entero y retorna una lista con los dígitos que se repiten.
    Cada dígito aparece una sola vez en la lista, aunque se repita varias veces.

    Args:
        n (int): Número entero positivo

    Returns:
        list: Lista de dígitos repetidos (sin duplicados)

    Ejemplo:
        >>> digitos_repetidos(112233)
        [1, 2, 3]
    """
    # Convertimos el número a string para poder recorrer sus dígitos
    cadena = str(n)

    # Creamos dos conjuntos: uno para los dígitos vistos y otro para los repetidos
    vistos = set()
    repetidos = set()

    # Recorremos cada carácter de la cadena
    for d in cadena:
        if d in vistos:
            # Si ya lo vimos, lo agregamos al conjunto de repetidos
            repetidos.add(int(d))
        else:
            # Si es la primera vez que lo vemos, lo agregamos a 'vistos'
            vistos.add(d)

    # Convertimos el conjunto de repetidos en lista y lo retornamos
    return list(repetidos)

# ============================================================================
# EJERCICIO 20: Análisis de palabras
# ============================================================================
def contar_palabras(texto):
    """
    Cuenta la cantidad de palabras en un texto.
    
    Args:
        texto: String con el texto
    
    Returns:
        Cantidad de palabras
    """
    return len(texto.split())


def letras_repetidas_palabra(palabra):
    """
    Retorna las letras que se repiten en una palabra.
    
    Args:
        palabra: String con la palabra
    
    Returns:
        Set con las letras repetidas
    """
    palabra = palabra.lower()
    letras = [c for c in palabra if c.isalpha()]
    repetidas = set()
    vistas = set()
    
    for letra in letras:
        if letra in vistas:
            repetidas.add(letra)
        else:
            vistas.add(letra)
    
    return repetidas
