"""
EJERCICIO 26: Frecuencia de caracteres
Implementar la función frecuencia_caracteres(cadena) que retorna
la cantidad de veces que aparece cada carácter.
"""

from funciones import frecuencia_caracteres

print("Análisis de frecuencia de caracteres")
print("="*60)

# Ejemplo 1
texto1 = "programacion"
frecuencias1 = frecuencia_caracteres(texto1)
print(f"\nTexto: '{texto1}'")
print("Frecuencias:")
for caracter, cantidad in sorted(frecuencias1.items()):
    print(f"  '{caracter}': {cantidad}")

# Ejemplo 2
texto2 = "Mississippi"
frecuencias2 = frecuencia_caracteres(texto2)
print(f"\nTexto: '{texto2}'")
print("Frecuencias:")
for caracter, cantidad in sorted(frecuencias2.items()):
    print(f"  '{caracter}': {cantidad}")

# Ejemplo 3: Con espacios y puntuación
texto3 = "Hola, mundo!"
frecuencias3 = frecuencia_caracteres(texto3)
print(f"\nTexto: '{texto3}'")
print("Frecuencias:")
for caracter, cantidad in sorted(frecuencias3.items()):
    if caracter == ' ':
        print(f"  '[espacio]': {cantidad}")
    else:
        print(f"  '{caracter}': {cantidad}")

# Modo interactivo
print("\n" + "="*60)
texto_usuario = input("Ingrese un texto para analizar: ")
frecuencias_usuario = frecuencia_caracteres(texto_usuario)

print("\nFrecuencias de caracteres:")
for caracter, cantidad in sorted(frecuencias_usuario.items()):
    if caracter == ' ':
        print(f"  '[espacio]': {cantidad}")
    elif caracter == '\n':
        print(f"  '[salto de línea]': {cantidad}")
    else:
        print(f"  '{caracter}': {cantidad}")
