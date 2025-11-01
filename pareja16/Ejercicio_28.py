# Programa para gestionar una colección de películas

# Estructura principal: diccionario con clave = título
# Cada valor será otro diccionario con: director, año y lista de actores

peliculas = {}

# --- Carga de datos ---
while True:
    titulo = input("Ingrese el título de la película (o 'fin' para terminar): ")
    if titulo.lower() == 'fin':
        break

    director = input("Ingrese el director: ")
    anio = int(input("Ingrese el año de estreno: "))
    actores = input("Ingrese los actores principales separados por comas: ").split(',')

    # Limpiamos espacios en los nombres de actores
    actores = [actor.strip() for actor in actores]

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": actores
    }

print("\n--- Datos cargados correctamente ---\n")

# --- a) Cantidad de películas dirigidas por cada director ---
directores = {}

for datos in peliculas.values():
    director = datos["director"]
    directores[director] = directores.get(director, 0) + 1

print("Cantidad de películas por director:")
for d, cant in directores.items():
    print(f"  {d}: {cant}")

# --- b) Director con más películas ---
max_director = max(directores, key=directores.get)
print(f"\nEl director que dirigió más películas es: {max_director} ({directores[max_director]} películas)")

# --- c) Dado el título, mostrar actores ---
titulo_buscar = input("\nIngrese el título de una película para ver sus actores: ")
if titulo_buscar in peliculas:
    print("Actores principales:")
    for actor in peliculas[titulo_buscar]["actores"]:
        print("  -", actor)
else:
    print("Esa película no está registrada.")

# --- d) Dado un actor, listar películas ---
actor_buscar = input("\nIngrese el nombre de un actor para ver sus películas: ").strip()
peliculas_actor = [titulo for titulo, datos in peliculas.items() if actor_buscar in datos["actores"]]

if peliculas_actor:
    print(f"\nPelículas donde actúa {actor_buscar}:")
    for p in peliculas_actor:
        print("  -", p)
else:
    print(f"{actor_buscar} no aparece en ninguna película registrada.")
