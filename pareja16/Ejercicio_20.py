
texto = input("Ingresar un texto: ")

# separo en palabras usando espacio como separador
palabras = texto.split()

print("Cantidad de palabras:", len(palabras))
print()

for palabra in palabras:
    # trabajar solo con letras, sin dígitos ni símbolos
    solo_letras = ""
    for c in palabra:
        if c.isalpha():
            solo_letras += c

    # pasar a minúsculas
    solo_letras = solo_letras.lower()

    repetidas = []
    for letra in solo_letras:
        if solo_letras.count(letra) > 1 and letra not in repetidas:
            repetidas.append(letra)

    # salida para esa palabra
    if len(repetidas) > 0:
        print("En '" + palabra + "' se repiten:", repetidas)
    else:
        print("En '" + palabra + "' no hay letras repetidas")

