from funciones import letras_repetidas

texto = input("ingrese un texto: ")

palabras = texto.split()

print(f"cantidad total de palabras: {len(palabras)}")

for palabra in palabras:
    rep = letras_repetidas(palabra)
    if rep:
        print(f"en '{palabra}' las letras repetidas son: {', '.join(rep)}")
    else:
        print(f"en '{palabra}' no hay letras repetidas")    