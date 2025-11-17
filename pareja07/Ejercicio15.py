
def obtenerCiudad(personas, DNI):
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None


def obtenerProvincia(personas, ciudades, DNI):
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad is None:
        return None
    for c in ciudades:
        if c[0] == ciudad:
            return c[1]
    return None


def contarPoblacion(personas, ciudades, provincia):
    contador = 0
    for persona in personas:
        prov = obtenerProvincia(personas, ciudades, persona[1])
        if prov == provincia:
            contador += 1
    return contador


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

print(obtenerCiudad(personas, 40173542))             
print(obtenerProvincia(personas, ciudades, 26782345)) 
print(contarPoblacion(personas, ciudades, "Córdoba")) 
