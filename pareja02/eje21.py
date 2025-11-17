#EJE21

from Funcioness import contar_palabras, letras_repetidas_palabra

print("Análisis de texto")
print("="*60)

texto = input("Ingrese un texto: ")

# Contar palabras
cantidad_palabras = contar_palabras(texto)
print(f"\nCantidad de palabras en el texto: {cantidad_palabras}")

# Analizar cada palabra
print("\nLetras repetidas por palabra:")
print("-"*60)

palabras = texto.split()
for palabra in palabras:
    letras_rep = letras_repetidas_palabra(palabra)
    
    # Filtrar solo letras
    palabra_limpia = ''.join(c for c in palabra if c.isalpha())
    
    if letras_rep:
        print(f"'{palabra_limpia}': {sorted(letras_rep)}")
    else:
        print(f"'{palabra_limpia}': (sin letras repetidas)")

print("\n" + "="*60)
print("Ejemplo con el texto: 'Serenos estaban los bosques...'")
print("="*60)
texto_ejemplo = "Serenos estaban los bosques"
palabras_ejemplo = texto_ejemplo.split()

print(f"Cantidad de palabras: {len(palabras_ejemplo)}")
print("\nLetras repetidas:")
for palabra in palabras_ejemplo:
    letras_rep = letras_repetidas_palabra(palabra)
    if letras_rep:
        print(f"  '{palabra}': {sorted(letras_rep)}")
    else:
        print(f"  '{palabra}': (sin letras repetidas)")
