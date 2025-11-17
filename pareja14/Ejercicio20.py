signos = ".,;:!?¿¡\"'()[]{}"

texto = input("ingrese un texto: ")
for s in signos:
    texto = texto.replace(s, "")
texto = texto.lower()
palabras = texto.split()

print("la cantidad de palabras en el texto es de: ", len(palabras))

for palabra in palabras:
    letras_vistas = set()
    letras_repetidas = set()

    for letra in palabra:
        if letra.isalpha():
            if letra in letras_vistas:
                letras_repetidas.add(letra)
            else:
                letras_vistas.add(letra)

    if letras_repetidas:
        repetidas = ", ".join(letras_repetidas)
        print(f'en "{palabra}", las letras repetidas son: {repetidas}')
    else:
        print(f'en "{palabra}", no hay letras repetidas')