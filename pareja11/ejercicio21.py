import unicodedata

def normalizar(texto):
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def tiene_tres_vocales_diferentes(palabra):
    vocales = {'a', 'e', 'i', 'o', 'u'}
    usadas = {letra for letra in palabra if letra in vocales}
    return len(usadas) >= 3


texto = ""
linea = input("Ingrese una línea (finalice con * al final): ")

while not linea.endswith('*'):
    texto += linea + " "
    linea = input()


texto += linea.rstrip('*')


texto = normalizar(texto)

palabras = texto.replace('.', ' ').split()
palabras_tres_vocales = [p for p in palabras if tiene_tres_vocales_diferentes(p)]

print("\na) Palabras con al menos 3 vocales diferentes:")
if palabras_tres_vocales:
    print(", ".join(palabras_tres_vocales))
else:
    print("No hay palabras con 3 vocales diferentes.")

oraciones = [o.strip() for o in texto.split('.') if o.strip()]
cantidad_oraciones = len(oraciones)
print(f"\nb) Cantidad de oraciones: {cantidad_oraciones}")

if cantidad_oraciones > 0:
    oraciones_largas = sum(1 for o in oraciones if len(o.split()) > 5)
    porcentaje = (oraciones_largas / cantidad_oraciones) * 100
    print(f"c) Porcentaje de oraciones con más de 5 palabras: {porcentaje:.2f}%")
else:
    print("c) No hay oraciones.")
