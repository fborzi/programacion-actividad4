ciudad_pais = []

ciudad = input("Ingrese el nombre de la ciudad. Ingrese 'zz' para finalizar: ")
while ciudad != 'zz':
    pais = input("Ingrese el nombre del pais al que pertenece la coudad: ")
    
    ciudad_pais.append([ciudad.lower(), pais.lower()])
    
    ciudad = input("Ingrese el nombre de la ciudad. Ingrese 'zz' para finalizar: ")

ciudades_por_pais = {}
for elem in ciudad_pais:
    if elem[1] in ciudades_por_pais:
        ciudades_por_pais[elem[1]] += 1
    else:
        ciudades_por_pais[elem[1]] = 1

for pais in ciudades_por_pais:
    print(f"Ciudades en {pais.capitalize()}: {ciudades_por_pais[pais]}.")