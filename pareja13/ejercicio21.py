from funciones import tiene_tres_vocales_diferentes, normalizar

texto = ""
print("Ingresá el texto (finalizá con una línea terminada en '*'):")

while True:
    linea = input()
    texto += " " + linea
    if linea.endswith('*'):
        break

# Sacamos el asterisco final
texto = texto[:-1]

# --- Cálculo de palabras con al menos 3 vocales diferentes ---
palabras = texto.split()
palabras_vocales = [p for p in palabras if tiene_tres_vocales_diferentes(p)]

# --- Cálculo de oraciones ---
oraciones = [o.strip() for o in texto.split('.') if o.strip()]
total_oraciones = len(oraciones)

# --- Oraciones con más de 5 palabras ---
oraciones_largas = [o for o in oraciones if len(o.split()) > 5]
porcentaje_largas = (len(oraciones_largas) / total_oraciones * 100) if total_oraciones > 0 else 0

# --- Resultados ---
print("\n--- Resultados ---")
print("Palabras con al menos 3 vocales diferentes:")
if palabras_vocales:
    for palabra in palabras_vocales:
        print("-", palabra)
else:
    print("Ninguna palabra cumple la condición.")

print(f"\nCantidad total de oraciones: {total_oraciones}")
print(f"Porcentaje de oraciones con más de 5 palabras: {porcentaje_largas:.2f}%")
