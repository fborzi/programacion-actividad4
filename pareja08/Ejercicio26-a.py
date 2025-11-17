ciudades_por_pais = {}

ciudad = input("Ingrese el nombre de la ciudad. Ingrese 'zz' para finalizar: ").lower()
while ciudad != 'zz':
    pais = input("Ingrese el nombre del pais al que pertenece la coudad: ").lower()
    
    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1
    
    ciudad = input("Ingrese el nombre de la ciudad. Ingrese 'zz' para finalizar: ").lower()

total_ciudades = 0
for pais in ciudades_por_pais:
    print(f"Ciudades en {pais.capitalize()}: {ciudades_por_pais[pais]}.")
    total_ciudades += ciudades_por_pais[pais]

print(f"Ciudades totales: {total_ciudades}.")