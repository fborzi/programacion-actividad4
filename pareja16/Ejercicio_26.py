# Versión 1: Sin almacenar las ciudades

def ciudades_por_pais():
    ciudades_por_pais = {}
    total_ciudades = 0

    while True:
        ciudad = input("Ingrese el nombre de la ciudad (zz para finalizar): ")
        if ciudad.lower() == "zz":
            break

        pais = input("Ingrese el país al que pertenece: ")

        # Incrementar el contador para el país
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

        total_ciudades += 1

    # Resultados
    print(f"\nCantidad total de ciudades ingresadas: {total_ciudades}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"- {pais}: {cantidad}")

# Ejecución
ciudades_por_pais()


# Versión 2: Almacenando las ciudades en una lista

def ciudades_y_paises():
    lista_ciudades = []

    # Carga de datos
    while True:
        ciudad = input("Ingrese el nombre de la ciudad (zz para finalizar): ")
        if ciudad.lower() == "zz":
            break

        pais = input("Ingrese el país al que pertenece: ")
        lista_ciudades.append([ciudad, pais])

    # Procesamiento
    ciudades_por_pais = {}
    for ciudad, pais in lista_ciudades:
        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] += 1
        else:
            ciudades_por_pais[pais] = 1

    # Resultados
    print(f"\nCantidad total de ciudades ingresadas: {len(lista_ciudades)}")
    print("Cantidad de ciudades por país:")
    for pais, cantidad in ciudades_por_pais.items():
        print(f"- {pais}: {cantidad}")

# Ejecución
ciudades_y_paises()
