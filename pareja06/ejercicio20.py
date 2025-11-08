"""
EJERCICIO 20: Análisis de palabras en un texto
Solicitar un string e informar cantidad de palabras y letras repetidas por palabra.
"""

from funciones import contar_palabras, letras_repetidas_palabra
print("=== ANÁLISIS DE TEXTO ===")
print()

# Solicitamos el ingreso de un string
texto = input("Ingrese un texto: ")

# a) Contar la cantidad de palabras (separadas por espacios)
palabras = texto.split()  # split() divide el texto por espacios
cantidad_palabras = len(palabras)
print()
print(f"a) Cantidad de palabras: {cantidad_palabras}")
print()

# b) Para cada palabra, encontrar las letras que se repiten
print("b) Letras repetidas en cada palabra:")
print()

for palabra in palabras:
    # Convertimos la palabra a minúsculas para ignorar diferencias de mayúsculas
    palabra_lower = palabra.lower()
    
    # Conjunto para almacenar letras repetidas
    letras_repetidas = set()
    
    # Conjunto para almacenar letras ya vistas
    letras_vistas = set()
    
    # Recorremos cada carácter de la palabra
    for caracter in palabra_lower:
        # Solo procesamos si es una letra (excluyendo dígitos y símbolos)
        if caracter.isalpha():
            # Si ya vimos esta letra antes, es repetida
            if caracter in letras_vistas:
                letras_repetidas.add(caracter)
            else:
                letras_vistas.add(caracter)
    
    # Mostramos el resultado para esta palabra
    if len(letras_repetidas) > 0:
        # Convertimos el conjunto a lista ordenada para mejor visualización
        letras_ordenadas = sorted(list(letras_repetidas))
        print(f"   '{palabra}': {', '.join(letras_ordenadas)}")
    else:
        print(f"   '{palabra}': no tiene letras repetidas")

print()
print("=" * 50)

# === EJEMPLO DEL ENUNCIADO ===
print()
print("EJEMPLO DEL ENUNCIADO:")
print()

texto_ejemplo = "Serenos estaban los bosques"
print(f"Texto: '{texto_ejemplo}'")
print()

palabras_ejemplo = texto_ejemplo.split()
print(f"Cantidad de palabras: {len(palabras_ejemplo)}")
print()
print("Letras repetidas:")

for palabra in palabras_ejemplo:
    palabra_lower = palabra.lower()
    letras_repetidas = set()
    letras_vistas = set()
    
    for caracter in palabra_lower:
        if caracter.isalpha():
            if caracter in letras_vistas:
                letras_repetidas.add(caracter)
            else:
                letras_vistas.add(caracter)
    
    if len(letras_repetidas) > 0:
        letras_ordenadas = sorted(list(letras_repetidas))
        print(f"   '{palabra}': {', '.join(letras_ordenadas)}")
    else:
        print(f"   '{palabra}': no tiene letras repetidas")