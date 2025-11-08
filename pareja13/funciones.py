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


# --- Ejemplos de uso ---
ciudades = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Córdoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquín", "Córdoba"]
]

personas = [
    ["Juan Perez", 26782345, "Carlos Paz"],
    ["María Gomez", 40173542, "Rosario"],
    ["Ana Ríos", 9216378, "Cosquín"]
]

