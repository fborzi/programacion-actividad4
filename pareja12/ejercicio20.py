"""
EJERCICIO 20
Escribí un programa que solicite el ingreso de un string e informe:
La cantidad de palabras que hay en todo el texto 
(las palabras se separan por espacios).
Para cada palabra, las letras que se repiten
 (ignorando diferencias de mayúsculas). 
 Sólo se deben informar letras (excluyendo dígitos y símbolos). 
 Ejemplo: para el string “Serenos estaban los bosques…” 
 se informará que hay 4 palabras en total y que las letras repetidas 
 en “serenos” son la “s” y la “e”, en “estaban” es la “a”, 
 en “bosques” es la “s”.
"""
texto = input("Ingrese un texto: ")
palabras = texto.split()

#1. Informar la cantidad de palabras
cantidad_palabras = len(palabras)
print("Cantidad de palabras:", cantidad_palabras)
print()

#2. Para cada palabra, informar las letras repetidas
print("Letras repetidas en cada palabras:")
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

for palabra in palabras:
    palabra_min = palabra.lower()

    contador = {}

    for caracter in palabra_min:
        if caracter in alfabeto:
            if caracter in contador:
                contador[caracter] = contador[caracter] + 1
            else:
                contador[caracter] = 1

    repetidas = []

    for letra in contador:
        if contador[letra] > 1:
            repetidas.append(letra)

    if len(repetidas) > 0:
        print("En", palabra, "las letras repetidas son:", repetidas)
    else:
        print("En", palabra, "no hay letras repetidas.")