from Funciones import tiene_3_vocales_diferentes, limpiar_palabra

print("Ingrese líneas de texto. Finaliza cuando una línea termine en '*'.\n")

texto = ""
palabras_con_vocales = []
cantidad_oraciones = 0
oraciones_mas_5_palabras = 0

# Ingreso del texto
while True:
    linea = input()
    texto = texto + " " + linea

    largo = len(linea)
    if largo > 0 and linea[largo - 1] == "*":
        break

# Procesamos oraciones
oraciones = texto.split(".")

for oracion in oraciones:
    oracion = oracion.strip()
    if oracion == "":
        continue

    # *** NUEVO ***
    tiene_letra = False
    for letra in oracion:
        if letra.lower() >= "a" and letra.lower() <= "z":
            tiene_letra = True
    if not tiene_letra:
        continue
    # *************

    cantidad_oraciones = cantidad_oraciones + 1


    palabras = oracion.split()

    if len(palabras) > 5:
        oraciones_mas_5_palabras = oraciones_mas_5_palabras + 1

    # Revisar cada palabra
    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)

        if tiene_3_vocales_diferentes(palabra_limpia):
            palabras_con_vocales.append(palabra_limpia)


# ---- Resultados ----
print("\n------------------------------------")
print("Palabras con al menos 3 vocales diferentes:")

if len(palabras_con_vocales) > 0:
    for p in palabras_con_vocales:
        print(" -", p)
else:
    print("No hubo.")

print("\nCantidad de oraciones:", cantidad_oraciones)

if cantidad_oraciones > 0:
    porcentaje = (oraciones_mas_5_palabras * 100) / cantidad_oraciones
    print("Porcentaje de oraciones con más de 5 palabras:", porcentaje, "%")
else:
    print("No hubo oraciones.")