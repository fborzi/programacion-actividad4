# Análisis de texto

print("\nIngrese un texto de una o más líneas.")
print("Finalice una línea con '*' para terminar.\n")

texto_completo = ""
fin_lectura = False

# Leer líneas hasta encontrar una que termine con '*'
while not fin_lectura:
    linea = input()
    if linea.endswith('*'):
        texto_completo += linea[:-1]  # Agregar sin el asterisco
        fin_lectura = True
    else:
        texto_completo += linea + " "

print("Resultafos del Analisis")

# Palabras con al menos 3 vocales diferentes
print("\ne) Palabras con al menos 3 vocales diferentes:")
palabras = texto_completo.split()
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

palabras_con_3_vocales = []
for palabra in palabras:
    # Limpiar signos de puntuación
    palabra_limpia = ''.join(c for c in palabra if c.isalpha())
    
    # Contar vocales únicas (ignorando mayúsculas y acentos)
    vocales_encontradas = set()
    for caracter in palabra_limpia.lower():
        if caracter in 'aeiou':
            vocales_encontradas.add(caracter)
        elif caracter in 'áéíóú':
            # Normalizar vocales con acento
            normalizacion = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
            vocales_encontradas.add(normalizacion[caracter])
    
    if len(vocales_encontradas) >= 3:
        palabras_con_3_vocales.append(palabra)

if palabras_con_3_vocales:
    print("Palabras encontradas:")
    for palabra in palabras_con_3_vocales:
        print(f"  - {palabra}")
else:
    print("No se encontraron palabras con al menos 3 vocales diferentes")

# Cantidad de oraciones en el texto
print("\nf) Cantidad de oraciones:")
cantidad_oraciones = texto_completo.count('.')
print(f"Total de oraciones: {cantidad_oraciones}")

# Porcentaje de oraciones con más de cinco palabras
print("\ng) Porcentaje de oraciones con más de 5 palabras:")
if cantidad_oraciones > 0:
    oraciones = texto_completo.split('.')
    oraciones_mas_5_palabras = 0
    
    for oracion in oraciones:
        palabras_oracion = oracion.strip().split()
        if len(palabras_oracion) > 5:
            oraciones_mas_5_palabras += 1
    
    porcentaje = (oraciones_mas_5_palabras / cantidad_oraciones) * 100
    print(f"Porcentaje: {porcentaje:.2f}%")
else:
    print("No hay oraciones en el texto")