#  Función frecuencia_caracteres

from funciones import frecuencia_caracteres

# Pruebas de la función frecuencia_caracteres
print("\nPruebas de la función frecuencia_caracteres():")

cadena1 = "hola mundo"
resultado1 = frecuencia_caracteres(cadena1)
print(f"\nCadena: '{cadena1}'")
print(f"Frecuencias: {resultado1}")

cadena2 = "programming"
resultado2 = frecuencia_caracteres(cadena2)
print(f"\nCadena: '{cadena2}'")
print(f"Frecuencias: {resultado2}")

cadena3 = "aaaaabbbcc"
resultado3 = frecuencia_caracteres(cadena3)
print(f"\nCadena: '{cadena3}'")
print(f"Frecuencias: {resultado3}")

# Mostrar de forma más legible
print("\n" + "=" * 50)
print("Frecuencias detalladas para la primera cadena:")
print("=" * 50)
for caracter, frecuencia in resultado1.items():
    print(f"'{caracter}': {frecuencia} veces")