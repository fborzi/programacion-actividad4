#Ejercicio26_A
#Version 1
print("Ingresá nombres de ciudades y su país (terminá con '0' en la ciudad).")

ciudad = input("Ciudad: ")
ciudades_totales = 0
ciudades_por_pais = {}

while ciudad.lower() != "0":
    pais = input("País: ")

    ciudades_totales += 1

    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

    ciudad = input("Ciudad: ")

print("\nCantidad total de ciudades ingresadas:", ciudades_totales)
print("Cantidad de ciudades por país:")

for pais, cantidad in ciudades_por_pais.items():
    print("-", pais, ":", cantidad)



