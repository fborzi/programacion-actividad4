def contar_cinco(L):
    """cuenta la cantidad de cincos encontrados
      tanto en la lista o sublistas"""
    contador = 0
    for x in L:
        try:
            for sub_x in x:
                contador += contar_cinco([sub_x])
        except TypeError:
            if x == 5:
                contador += 1
    return contador
def minimo_elemento(lista):
    """verifica un listado de numeros 1x1 a ver cual es el
     de menor valor"""
    if not lista:
        return None
    minimo = lista[0]
    for palabra in lista:
        if palabra < minimo:
            minimo = palabra
    return minimo
def piedra_papel_tijera(uno, dos):
    """es un simple juego de piedra papel o tijera. 
     papel le gana a piedra, piedra le gana a tijera
     y tijera le gana a papel"""
    uno = uno.lower()
    dos = dos.lower()
    if uno == dos:
        return 0
    if uno == "papel":
        if dos == "piedra":
            return 1
    if uno == "piedra":
        if dos == "tijera":
            return 1
    if uno == "tijera":
        if dos == "papel":
            return 1
    if dos == "papel":
        if uno == "piedra":
            return 2
    if dos == "piedra":
        if uno == "tijera":
            return 2
    if dos == "tijera":
        if uno == "papel":
            return 2
def borrar_adyacentes(lista):
    """elimina de una lista los datos repetidos, retornando
    la misma lista sin dichos datos repetidos"""
    nueva = [lista[0]]
    for elemento in lista[1:]:
        if elemento != nueva[-1]:
            nueva.append(elemento)
    return nueva
def suma_digitos(n):
    """suma los datos encontrados con mas de 2 digitos,
    retornando el resultado"""
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma
def sumatoria_digitos(lista):
    """retorna una lista con datos pero utiliza la
    funcion anterior para simplificar los datos con mas
    de 2 digitos"""
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado
def dos_sumandos(lista, resultado):
    """retorna 2 numeros de una lista que sumandolos den x resultado"""
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return "No hay dos números que sumen el objetivo"