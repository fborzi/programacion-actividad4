# Ingreso del texto
texto = input("Ingrese un texto: ")

# Separamos palabras
palabras = texto.split()

# Abecedario (solo letras)
letras_validas = "abcdefghijklmnopqrstuvwxyz"

print("Cantidad de palabras:", len(palabras))
print("----------------------------------------")

for palabra in palabras:
    palabra_limpia = ""

    # Pasamos letras a minúsculas y filtramos símbolos
    for c in palabra.lower():
        if c in letras_validas:  
            palabra_limpia += c
    
    repetidas = []

    # Buscamos letras repetidas
    for letra in palabra_limpia:
        if palabra_limpia.count(letra) > 1 and letra not in repetidas:
            repetidas.append(letra)

    # Mostramos resultados
    if len(repetidas) > 0:
        print(f"En '{palabra}' las letras repetidas son: {repetidas}")
    else:
        print(f"En '{palabra}' no hay letras repetidas.")
