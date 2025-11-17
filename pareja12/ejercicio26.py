print("="*50)
print("VERSION 1: Procesamiento directo.")
print("="*50)
print("Ingrese 0 como ciudad para finaizar")

cantidad_total = 0
ciudades_por_pais = {}

ciudad = input("Ciudad: ")

while ciudad != "0":
    pais = input("Pais: ")

    cantidad_total += 1

    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1
    
    ciudad = input("Ciudad: ") 

print("Cantidad total de ciudades ingresadas: ", cantidad_total)
print("Cantidad de ciudades por país:")
for pais in ciudades_por_pais:
    print(pais ,":", ciudades_por_pais[pais], "ciudad/es.")

print("="*50)
print("VERSION 2: Almacenando ciudades y procesando despues.")
print("="*50)
print("Ingrese 'zz'  como ciudad para finalizar")

lista_ciudades= []

ciudad = input("Ciudad: ")

while ciudad != "zz":
    pais = input("Pais: ")

    lista_ciudades.append([ciudad, pais])

    ciudad = input("Ciudad: ")

cantidad_total = len(lista_ciudades)
ciudades_por_pais = {}
for elemento in lista_ciudades:
    ciudad = elemento[0]
    pais = elemento[1]

    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

print("Cantidad total de ciudades ingresadas:", cantidad_total)
print("Ciudades almacenadas:")
for elemento in lista_ciudades:
    print(elemento[0], elemento[1])

print("Cantidad de ciudades por pais:")
for pais in ciudades_por_pais:
    print(pais, ":", ciudades_por_pais[pais] ,"ciudad/es")