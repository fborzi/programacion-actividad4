"""
 Ejercicio 28: Diccionario para almacenar las películas
 Clave: título | Valor: diccionario con director, año y actores
"""
peliculas = {}

# === CARGA DE DATOS ===
print("=== CARGA DE PELÍCULAS ===")
while True:
    titulo = input("Título de la película (vacío para terminar): ").strip()
    if titulo == "":
        break

    director = input("Director: ").strip()
    año = int(input("Año de estreno: "))
    actores = input("Actores principales (separados por coma): ").split(",")

    # Guardamos los datos en el diccionario
    peliculas[titulo] = {
        "director": director,
        "año": año,
        "actores": [actor.strip() for actor in actores]
    }

print("\n=== DATOS CARGADOS ===")
print(f"Películas registradas: {len(peliculas)}")

# === a. Cantidad de películas por director ===
print("\n=== a. Películas por director ===")
conteo_directores = {}
for datos in peliculas.values():
    d = datos["director"]
    conteo_directores[d] = conteo_directores.get(d, 0) + 1

for director, cantidad in conteo_directores.items():
    print(f"{director}: {cantidad} película(s)")

# === b. Director con más películas ===
print("\n=== b. Director con más películas ===")
if conteo_directores:
    max_director = max(conteo_directores.items(), key=lambda x: x[1])
    print(f"{max_director[0]} dirigió {max_director[1]} película(s)")

# === c. Actores principales de una película ===
print("\n=== c. Actores de una película ===")
titulo_buscar = input("Ingresá el título de la película: ").strip()
if titulo_buscar in peliculas:
    actores = peliculas[titulo_buscar]["actores"]
    print(f"Actores principales de '{titulo_buscar}': {', '.join(actores)}")
else:
    print("Película no encontrada.")

# === d. Películas donde actúa un actor ===
print("\n=== d. Películas por actor ===")
actor_buscar = input("Ingresá el nombre del actor: ").strip()
pelis_actor = [titulo for titulo, datos in peliculas.items() if actor_buscar in datos["actores"]]

if pelis_actor:
    print(f"Películas donde actúa {actor_buscar}:")
    for t in pelis_actor:
        print(f"- {t}")
else:
    print(f"No se encontraron películas con el actor {actor_buscar}.")
