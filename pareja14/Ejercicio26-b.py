ciudades = []
cont = 1000

for i in range (cont):
    ciudad = input("ingrese el nombre de la ciudad (zz para terminar): ")
    if ciudad.lower() == "zz":
        break
    pais = input("ingrese el pais de la ciudad: ")
    ciudades.append([ciudad, pais])

total_ciudades = len(ciudades)

ciudades_por_pais = {}
for ciudad, pais in ciudades:
    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

print("\ncantidad total de ciudades ingresadas: ", total_ciudades)
print("cantidad de ciudades por pais: ")
for pais, cantidad in ciudades_por_pais.items():
    print(f"{pais}: {cantidad}")