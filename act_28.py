peliculas = {}

while True:
    titulo = input("Ingrese el título de la película (o 'fin' para terminar): ")
    if titulo.lower() == "fin":
        break

    director = input("Ingrese el director: ")
    anio = int(input("Ingrese el año de estreno: "))

    actores = []
    print("Ingrese los actores principales (escriba 'listo' para terminar):")
    while True:
        actor = input("Actor: ")
        if actor.lower() == "listo":
            break
        actores.append(actor)

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": actores
    }

directores = {}
for datos in peliculas.values():
    d = datos["director"]
    if d not in directores:
        directores[d] = 0
    directores[d] += 1

print("\nCantidad de películas por director:")
for d, cant in directores.items():
    print(d, "dirigió", cant, "películas")

if len(directores) > 0:
    max_director = max(directores, key=directores.get)
    print("\nEl director con más películas es:", max_director, "con", directores[max_director], "películas.")
else:
    print("\nNo se cargaron películas.")

titulo_buscar = input("\nIngrese el título de una película para ver sus actores: ")
if titulo_buscar in peliculas:
    print("Actores principales de", titulo_buscar + ":")
    for a in peliculas[titulo_buscar]["actores"]:
        print("-", a)
else:
    print("No existe una película con ese título.")

actor_buscar = input("\nIngrese el nombre de un actor para ver sus películas: ")
encontradas = []
for titulo, datos in peliculas.items():
    if actor_buscar in datos["actores"]:
        encontradas.append(titulo)

if len(encontradas) > 0:
    print("Películas en las que actúa", actor_buscar + ":")
    for t in encontradas:
        print("-", t)
else:
    print("No se encontraron películas con ese actor.")