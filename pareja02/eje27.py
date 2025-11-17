#EJE27

print("="*60)
print("VERSIÓN 1: Sin almacenar ciudades")
print("="*60)

# Diccionario para contar ciudades por país
ciudades_por_pais_v1 = {}
total_ciudades_v1 = 0

print("\nIngrese ciudades y países (ciudad 'zz' para terminar):")

while True:
    ciudad = input("Ciudad: ")
    if ciudad.lower() == "zz":
        break
    
    pais = input("País: ")
    
    # Contar
    total_ciudades_v1 += 1
    if pais in ciudades_por_pais_v1:
        ciudades_por_pais_v1[pais] += 1
    else:
        ciudades_por_pais_v1[pais] = 1

print(f"\nTotal de ciudades ingresadas: {total_ciudades_v1}")
print("\nCiudades por país:")
for pais, cantidad in ciudades_por_pais_v1.items():
    print(f"  {pais}: {cantidad} ciudad(es)")

print("\n" + "="*60)
print("VERSIÓN 2: Almacenando en lista")
print("="*60)

# Lista para almacenar [ciudad, país]
ciudades_lista = []

print("\nIngrese ciudades y países (ciudad 'zz' para terminar):")

# Datos de ejemplo para demostración
datos_ejemplo = [
    ["Colonia", "Uruguay"],
    ["Granada", "España"],
    ["Inverness", "Escocia"],
    ["Salto", "Uruguay"],
    ["Piriápolis", "Uruguay"],
    ["Aberdeen", "Escocia"]
]

print("\n(Usando datos de ejemplo para demostración)")
ciudades_lista = datos_ejemplo.copy()

# Mostrar lista
print("\nLista de ciudades:")
for ciudad, pais in ciudades_lista:
    print(f"  {ciudad} - {pais}")

# Procesar la lista para contar por país
ciudades_por_pais_v2 = {}
for ciudad, pais in ciudades_lista:
    if pais in ciudades_por_pais_v2:
        ciudades_por_pais_v2[pais] += 1
    else:
        ciudades_por_pais_v2[pais] = 1

print(f"\nTotal de ciudades ingresadas: {len(ciudades_lista)}")
print("\nCiudades por país:")
for pais, cantidad in ciudades_por_pais_v2.items():
    print(f"  {pais}: {cantidad} ciudad(es)")
