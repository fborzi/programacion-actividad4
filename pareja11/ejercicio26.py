# a) 
def contar_ciudades():
    ciudades_por_pais = {}
    total = 0

    ciudad = input("Ingrese una ciudad (o 'zz' para terminar): ")

    while ciudad.lower() != "zz":
        pais = input(f"Ingrese el país de {ciudad}: ")

        total += 1
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

        ciudad = input("Ingrese otra ciudad (o 'zz' para terminar): ")

    print(f"Cantidad total de ciudades: {total}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"{pais}: {cantidad}")
        
 
print("ejemplo a)")
contar_ciudades() 
 
        
# b)

def contar_ciudades_lista():
    ciudades = []

    ciudad = input("Ingrese una ciudad (o 'zz' para terminar): ")

    while ciudad.lower() != "zz":
        pais = input(f"Ingrese el país de {ciudad}: ")
        ciudades.append([ciudad, pais])
        ciudad = input("Ingrese otra ciudad (o 'zz' para terminar): ")

    total = len(ciudades)
    ciudades_por_pais = {}

    for ciudad, pais in ciudades:
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

    print(f"Cantidad total de ciudades: {total}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"{pais}: {cantidad}")
        
        
print("ejemplo b)")
contar_ciudades_lista()                