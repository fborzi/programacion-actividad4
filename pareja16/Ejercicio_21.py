import unicodedata

def normalizar(texto):
    """
    Quita acentos y convierte a minúsculas.
    """
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

texto_completo = ""

# Lectura del texto hasta línea que termine con '*'
while True:
    linea = input("Ingresá una línea (terminá con * para finalizar): ")
    texto_completo += " " + linea
    if linea.strip().endswith('*'):
        break

# Eliminar el asterisco final
texto_completo = texto_completo.replace('*', '')

# Normalizar (quitar acentos, pasar a minúsculas)
texto_normalizado = normalizar(texto_completo)

# ---- 1. Palabras con al menos 3 vocales diferentes ----
vocales = {'a', 'e', 'i', 'o', 'u'}
palabras = texto_normalizado.split()
palabras_con_3_vocales = []

for palabra in palabras:
    letras_vocales = {letra for letra in palabra if letra in vocales}
    if len(letras_vocales) >= 3:
        palabras_con_3_vocales.append(palabra)

# ---- 2. Cantidad de oraciones ----
oraciones = [o.strip() for o in texto_normalizado.split('.') if o.strip() != '']
cantidad_oraciones = len(oraciones)

# ---- 3. Porcentaje de oraciones con más de 5 palabras ----
oraciones_largas = 0
for oracion in oraciones:
    cant_palabras = len(oracion.split())
    if cant_palabras > 5:
        oraciones_largas += 1

if cantidad_oraciones > 0:
    porcentaje_largas = (oraciones_largas / cantidad_oraciones) * 100
else:
    porcentaje_largas = 0

# ---- Resultados ----
print("\n--- RESULTADOS ---")
print(f"Palabras con al menos 3 vocales diferentes: {', '.join(palabras_con_3_vocales) if palabras_con_3_vocales else 'ninguna'}")
print(f"Cantidad de oraciones: {cantidad_oraciones}")
print(f"Porcentaje de oraciones con más de 5 palabras: {porcentaje_largas:.2f}%")
