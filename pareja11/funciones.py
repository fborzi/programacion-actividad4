def digitos_repetidos(numero):
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
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def sucesion_mira_y_deci(n):
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