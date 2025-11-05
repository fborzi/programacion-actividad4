
texto = ""
linea = input("Ingresar linea (terminar con *): ")

# mientras NO termine con *
while linea[-1] != "*":
    texto += linea + " "
    linea = input()

# saco el * de la última línea
texto += linea[:-1] + " "

# pasamos a minúsculas
texto = texto.lower()

# 1) palabras con 3 vocales distintas
vocales = "aeiou"
palabras = texto.replace(".", "").split()

print("Palabras con al menos 3 vocales diferentes:")

for palabra in palabras:
    distintas = set()
    for letra in palabra:
        if letra in vocales:
            distintas.add(letra)
    if len(distintas) >= 3:
        print(palabra)

# 2) cantidad de oraciones
oraciones = texto.count(".")

print("Cantidad total de oraciones:", oraciones)

# 3) porcentaje de oraciones con más de 5 palabras
oraciones_texto = texto.split(".")

largas = 0
for oracion in oraciones_texto:
    o = oracion.strip()
    if o != "":
        if len(o.split()) > 5:
            largas += 1

if oraciones > 0:
    porcentaje = (largas * 100) / oraciones
else:
    porcentaje = 0

print("Porcentaje de oraciones con más de 5 palabras:", porcentaje, "%")

