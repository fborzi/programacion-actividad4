from collections import Counter

texto = input("Ingresá un texto: ")

# Separar palabras (por espacios)
palabras = texto.split()
print(f"Cantidad de palabras: {len(palabras)}")

for palabra in palabras:
    # Convertir a minúsculas y filtrar solo letras
    solo_letras = [c.lower() for c in palabra if c.isalpha()]
    contador = Counter(solo_letras)

    # Buscar las letras repetidas
    repetidas = [letra for letra, cant in contador.items() if cant > 1]

    if repetidas:
        print(f"Letras repetidas en '{palabra}': {', '.join(repetidas)}")
    else:
        print(f"Letras repetidas en '{palabra}': ninguna")