"""
EJERCICIO 22: Análisis de texto multilínea
Solicitar texto de múltiples líneas (termina con *).
Calcular palabras con 3+ vocales, cantidad de oraciones y porcentaje de oraciones con >5 palabras.
"""

from funciones import tiene_n_vocales_diferentes, contar_oraciones, palabras_por_oracion

print("Análisis de texto multilínea")
print("(Finalice una línea con * para terminar)")
print("="*60)

# Leer texto multilínea
lineas = []
while True:
    linea = input()
    lineas.append(linea)
    if linea.endswith('*'):
        break

# Unir todas las líneas
texto_completo = ' '.join(lineas)
# Quitar el asterisco final
texto_completo = texto_completo.rstrip('*').strip()

print("\n" + "="*60)
print("RESULTADOS:")
print("="*60)

# a) Palabras con al menos 3 vocales diferentes
print("\na) Palabras con al menos 3 vocales diferentes:")
palabras = texto_completo.replace('.', ' ').replace(',', ' ').split()
palabras_3_vocales = []

for palabra in palabras:
    # Limpiar la palabra de signos de puntuación
    palabra_limpia = ''.join(c for c in palabra if c.isalpha())
    if palabra_limpia and tiene_n_vocales_diferentes(palabra_limpia, 3):
        palabras_3_vocales.append(palabra_limpia)

if palabras_3_vocales:
    for palabra in palabras_3_vocales:
        print(f"  - {palabra}")
else:
    print("  (No hay palabras con 3 o más vocales diferentes)")

# b) Cantidad de oraciones
cantidad_oraciones = contar_oraciones(texto_completo)
print(f"\nb) Cantidad de oraciones: {cantidad_oraciones}")

# c) Porcentaje de oraciones con más de 5 palabras
if cantidad_oraciones > 0:
    oraciones = texto_completo.split('.')
    oraciones = [o.strip() for o in oraciones if o.strip()]
    
    oraciones_mas_5 = 0
    for oracion in oraciones:
        if palabras_por_oracion(oracion) > 5:
            oraciones_mas_5 += 1
    
    porcentaje = (oraciones_mas_5 / cantidad_oraciones) * 100
    print(f"\nc) Oraciones con más de 5 palabras: {oraciones_mas_5}")
    print(f"   Porcentaje: {porcentaje:.2f}%")
else:
    print("\nc) No hay oraciones para analizar")
