# Función a 
# Dada la lista de personas y un DNI,
# devuelve la ciudad donde vive esa persona.
def obtenerCiudad(personas, DNI):
    # Recorremos la lista de personas
    for persona in personas:
        # Si el DNI coincide, devolvemos la ciudad (posición 2)
        if persona[1] == DNI:
            return persona[2]
    # Si no se encuentra el DNI, devolvemos None
    return None


# Función b 
# Dadas las listas de personas y ciudades, y un DNI,
# devuelve la provincia donde vive esa persona.
# Utiliza la función obtenerCiudad del inciso anterior.
def obtenerProvincia(personas, ciudades, DNI):
    # Primero obtenemos la ciudad donde vive la persona
    ciudad = obtenerCiudad(personas, DNI)
    
    # Si la ciudad no existe, devolvemos None
    if ciudad is None:
        return None
    
    # Recorremos la lista de ciudades para encontrar la provincia
    for c in ciudades:
        # Si el nombre de la ciudad coincide, devolvemos la provincia
        if c[0] == ciudad:
            return c[1]
    
    # Si no se encuentra la ciudad en la lista, devolvemos None
    return None


# Función c
# Dadas las listas de personas y ciudades, y una provincia,
# cuenta cuántas personas viven en esa provincia.
# Utiliza la función obtenerProvincia.
def contarPoblacion(personas, ciudades, provincia):
    contador = 0  # Inicializamos el contador en 0
    
    # Recorremos todas las personas
    for persona in personas:
        # Obtenemos el DNI de cada persona
        dni = persona[1]
        # Obtenemos la provincia donde vive
        prov = obtenerProvincia(personas, ciudades, dni)
        # Si la provincia coincide con la buscada, aumentamos el contador
        if prov == provincia:
            contador += 1
    
    # Al final, devolvemos la cantidad total
    return contador







def digitos_repetidos(n):
    # Convertimos el número a cadena para poder recorrer sus dígitos
    n = str(n)
    repetidos = []
    
    for digito in n:
        # Si el dígito aparece más de una vez y no lo agregamos antes, lo guardamos
        if n.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)
    
    return repetidos


def digitos_repetidos(n):
    """Retorna una lista con los dígitos repetidos de n."""
    n_str = str(abs(n))
    repetidos = []
    for dig in n_str:
        if n_str.count(dig) > 1 and dig not in repetidos:
            repetidos.append(dig)
    return [int(x) for x in repetidos]


def letras_repetidas(palabra):
    """Retorna una lista con las letras que se repiten en una palabra (ignorando mayúsculas y sin contar símbolos o dígitos)."""
    palabra = palabra.lower()
    letras = [c for c in palabra if c.isalpha()]  # Solo letras
    repetidas = []
    for letra in letras:
        if letras.count(letra) > 1 and letra not in repetidas:
            repetidas.append(letra)
    return repetidas



import unicodedata

def normalizar(texto):
    """Elimina acentos y pasa el texto a minúsculas."""
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def tiene_tres_vocales_diferentes(palabra):
    """Devuelve True si la palabra tiene al menos 3 vocales diferentes."""
    palabra = normalizar(palabra)
    vocales = {'a', 'e', 'i', 'o', 'u'}
    encontradas = set([letra for letra in palabra if letra in vocales])
    return len(encontradas) >= 3
