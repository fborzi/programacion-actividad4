from funciones import letras_repetidas

texto = input("Ingresá un texto: ")

palabras = texto.split()
print(f"\nCantidad de palabras: {len(palabras)}\n")

for palabra in palabras:
    repetidas = letras_repetidas(palabra)
    if repetidas:
        print(f"Letras repetidas en '{palabra}': {', '.join(repetidas)}")
    else:
        print(f"En '{palabra}' no hay letras repetidas.")
