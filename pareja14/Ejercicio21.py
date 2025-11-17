def normalizar_vocales(s):
    mapeo = {
        'á': 'a', 'à': 'a', 'ä': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ë': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'ï': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ö': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'ü': 'u', 'û': 'u'
    }
    resultado = []
    for c in s:
        if c in mapeo:
            resultado.append(mapeo[c])
        else:
            resultado.append(c)
    return ''.join(resultado)

def limpiar_palabra(palabra):
    inicio = 0
    fin = len(palabra) - 1
    while inicio <= fin and not palabra[inicio].isalpha():
        inicio += 1
    while fin >= inicio and not palabra[fin].isalpha():
        fin -= 1
    if inicio > fin:
        return ''
    return palabra[inicio:fin+1]

def main():
    lineas = []
    fin = False
    print("Ingrese el texto línea por línea. Termine con una línea que termine con '*':")
    while not fin:
        linea = input()
        if linea.endswith('*'):
            linea = linea.rstrip('*')
            lineas.append(linea)
            fin = True
        else:
            lineas.append(linea)
    
    texto = ' '.join(lineas)
    
    # Encontrar palabras con al menos 3 vocales diferentes
    tokens = texto.split()
    palabras_limpias = []
    for token in tokens:
        palabra_limpia = limpiar_palabra(token)
        if palabra_limpia:
            palabras_limpias.append(palabra_limpia)
    
    palabras_3_vocales = []
    for palabra in palabras_limpias:
        palabra_norm = normalizar_vocales(palabra.lower())
        vocales = set()
        for letra in palabra_norm:
            if letra in 'aeiou':
                vocales.add(letra)
        if len(vocales) >= 3:
            palabras_3_vocales.append(palabra)
    
    # Dividir en oraciones
    oraciones = [oracion.strip() for oracion in texto.split('.') if oracion.strip()]
    num_oraciones = len(oraciones)
    
    # Contar oraciones con más de 5 palabras
    oraciones_largas = 0
    for oracion in oraciones:
        palabras_en_oracion = [limpiar_palabra(token) for token in oracion.split()]
        palabras_en_oracion = [p for p in palabras_en_oracion if p]
        if len(palabras_en_oracion) > 5:
            oraciones_largas += 1
    
    porcentaje = (oraciones_largas / num_oraciones) * 100 if num_oraciones > 0 else 0
    
    # Resultados
    print("\nResultados:")
    print("Palabras con al menos 3 vocales diferentes:", palabras_3_vocales)
    print("Cantidad de oraciones:", num_oraciones)
    print("Porcentaje de oraciones con más de cinco palabras: {:.2f}%".format(porcentaje))

if __name__ == "__main__":
    main()