
lista = []

ciudad = input("Ingresar ciudad: ")

while ciudad != "zz":
    pais = input("Ingresar país de esa ciudad: ")

    lista.append([ciudad, pais])

    ciudad = input("Ingresar ciudad: ")

print("Total de ciudades ingresadas:", len(lista))


pais_ciudades = {}

for item in lista:
    pais = item[1]

    if pais in pais_ciudades:
        pais_ciudades[pais] += 1
    else:
        pais_ciudades[pais] = 1

print("Ciudades por país:", pais_ciudades)


