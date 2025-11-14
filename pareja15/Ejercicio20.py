from funciones import letras_repetidas

texto = input("Ingresá un texto: ")

# Separar las palabras (por espacios)
palabras = texto.split()
print("Cantidad de palabras:", len(palabras))

# Analizar cada palabra
for palabra in palabras:
    repetidas = letras_repetidas(palabra)
    if repetidas:
        print("En la palabra", palabra, "las letras repetidas son:", ', '.join(repetidas))

    else:
        print("En la palabra", palabra, "no hay letras repetidas.")