# ============================================
# PARTE 1: LEER EL TEXTO
# ============================================
print("Ingrese el texto (finalice una línea con '*' para terminar):")

texto_completo = ""
linea = input()

# Seguir leyendo líneas hasta que una termine con *
while not linea.endswith('*'):
    texto_completo = texto_completo + linea + " "
    linea = input()

# Agregar la última línea pero sin el *
texto_completo = texto_completo + linea[:-1]

print("\n--- RESULTADOS ---\n")


# ============================================
# PUNTO 1: Palabras con al menos 3 vocales diferentes
# ============================================
# Separar el texto en palabras (sin puntos ni comas)
texto_sin_puntos = texto_completo.replace('.', ' ')
texto_sin_puntos = texto_sin_puntos.replace(',', ' ')
palabras = texto_sin_puntos.split()

print("1. Palabras con al menos 3 vocales diferentes:")

for palabra in palabras:
    # Convertir a minúsculas para no diferenciar mayúsculas
    palabra_minuscula = palabra.lower()
    
    # Cambiar vocales con acento por vocales normales
    palabra_minuscula = palabra_minuscula.replace('á', 'a')
    palabra_minuscula = palabra_minuscula.replace('é', 'e')
    palabra_minuscula = palabra_minuscula.replace('í', 'i')
    palabra_minuscula = palabra_minuscula.replace('ó', 'o')
    palabra_minuscula = palabra_minuscula.replace('ú', 'u')
    
    # Buscar qué vocales tiene esta palabra
    vocales_encontradas = []
    
    for letra in palabra_minuscula:
        if letra == 'a' and 'a' not in vocales_encontradas:
            vocales_encontradas.append('a')
        elif letra == 'e' and 'e' not in vocales_encontradas:
            vocales_encontradas.append('e')
        elif letra == 'i' and 'i' not in vocales_encontradas:
            vocales_encontradas.append('i')
        elif letra == 'o' and 'o' not in vocales_encontradas:
            vocales_encontradas.append('o')
        elif letra == 'u' and 'u' not in vocales_encontradas:
            vocales_encontradas.append('u')
    
    # Si tiene 3 o más vocales diferentes, mostrarla
    if len(vocales_encontradas) >= 3:
        print(f"   - {palabra}")


# ============================================
# PUNTO 2: Cantidad de oraciones
# ============================================
cantidad_oraciones = 0

for caracter in texto_completo:
    if caracter == '.':
        cantidad_oraciones = cantidad_oraciones + 1

print(f"\n2. Cantidad de oraciones: {cantidad_oraciones}")


# ============================================
# PUNTO 3: Porcentaje de oraciones con más de 5 palabras
# ============================================
if cantidad_oraciones > 0:
    # Separar el texto en oraciones
    oraciones = texto_completo.split('.')
    
    oraciones_largas = 0  # Oraciones con más de 5 palabras
    
    for oracion in oraciones:
        oracion = oracion.strip()  # Quitar espacios al inicio y final
        
        if oracion != "":  # Si la oración no está vacía
            palabras_en_oracion = oracion.split()
            
            if len(palabras_en_oracion) > 5:
                oraciones_largas = oraciones_largas + 1
    
    porcentaje = (oraciones_largas / cantidad_oraciones) * 100
    print(f"3. Porcentaje de oraciones con más de 5 palabras: {porcentaje:.2f}%")
else:
    print("3. No hay oraciones en el texto.")