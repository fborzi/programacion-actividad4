#Ejercicio26_B
#Version 2
print("Ingresá nombres de ciudades y su país (terminá con '0' en la ciudad).")

lista_ciudades = []

ciudad = input("Ciudad: ")

while ciudad.lower() != "0":
    pais = input("País: ")
    lista_ciudades.append([ciudad, pais])
    ciudad = input("Ciudad: ")

# Procesamiento
ciudades_por_pais = {}

for ciudad, pais in lista_ciudades:
    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

print("\nCantidad total de ciudades ingresadas:", len(lista_ciudades))
print("Cantidad de ciudades por país:")

for pais, cantidad in ciudades_por_pais.items():
    print("-", pais, ":", cantidad)