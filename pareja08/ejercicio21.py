'''
21. Escribí un programa que solicite el ingreso de un texto formado por una o más líneas. El ingreso finalizará cuando se lea una línea terminada con un '*'
Calcular e informar:
a. Las palabras que tienen al menos 3 vocales diferentes (ignorando diferencias de acentos y mayúsculas).
b. La cantidad de oraciones en el texto (una oración finaliza siempre con un '.').
c. El porcentaje de oraciones con más de cinco palabras.'''
texto = ""
print("Ingresá líneas de texto. Finalizá con una línea que termine en '*':")

while True:
    linea = input()
    texto += linea + " "
    if linea.endswith("*"):
        break

texto = texto.lower()
texto = texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

palabras = texto.replace("*", "").replace(".", "").split()
vocales = "aeiou"
print("\n Palabras con al menos 3 vocales diferentes:")
for palabra in palabras:
    distintas = ""
    for letra in palabra:
        if letra in vocales and letra not in distintas:
            distintas += letra
    if len(distintas) >= 3:
        print("-", palabra)

cantidad_oraciones = texto.count(".")
print("\n Cantidad de oraciones:", cantidad_oraciones)

oraciones = texto.split(".")
oraciones_con_mas_de_5 = 0

for oracion in oraciones:
    palabras_en_oracion = oracion.strip().split()
    if len(palabras_en_oracion) > 5:
        oraciones_con_mas_de_5 += 1

if cantidad_oraciones > 0:
    porcentaje = (oraciones_con_mas_de_5 / cantidad_oraciones) * 100
else:
    porcentaje = 0

print("Porcentaje de oraciones con más de cinco palabras:", round(porcentaje, 2), "%")