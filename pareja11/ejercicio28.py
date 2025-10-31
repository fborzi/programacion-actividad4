def cargar_peliculas():
    peliculas = {}

    titulo = input("Ingrese el título de la película ('fin' para terminar): ")

    while titulo.lower() != "fin":
        director = input("Director: ")
        anio = int(input("Año de estreno: "))

        actores = []
        print("Ingrese los actores principales (escriba 'fin' para terminar):")
        actor = input("Actor: ")
        while actor.lower() != "fin":
            actores.append(actor)
            actor = input("Actor: ")

        peliculas[titulo] = {
            "director": director,
            "anio": anio,
            "actores": actores
        }

        print()
        titulo = input("Ingrese el título de la película ('fin' para terminar): ")

    return peliculas


def cantidad_peliculas_por_director(peliculas):
    conteo = {}
    for datos in peliculas.values():
        dir = datos["director"]
        conteo[dir] = conteo.get(dir, 0) + 1

    print("Cantidad de películas dirigidas por cada director:")
    for director, cant in conteo.items():
        print(f"{director}: {cant}")

    return conteo


def director_mas_peliculas(peliculas):
    conteo = cantidad_peliculas_por_director(peliculas)
    if conteo:
        max_director = max(conteo, key=conteo.get)
        print(f"El director con más películas es {max_director} ({conteo[max_director]} películas).")
    else:
        print("No hay películas cargadas.")


def actores_de_pelicula(peliculas, titulo):
    if titulo in peliculas:
        print(f"Actores principales de '{titulo}':")
        for actor in peliculas[titulo]["actores"]:
            print(f"- {actor}")
    else:
        print(f"No existe una película con el título '{titulo}'.")


def peliculas_de_actor(peliculas, actor_buscado):
    print(f"Películas en las que participó {actor_buscado}:")
    encontradas = [titulo for titulo, datos in peliculas.items() if actor_buscado in datos["actores"]]
    if encontradas:
        for t in encontradas:
            print(f"- {t}")
    else:
        print("No participó en ninguna película registrada.")


peliculas = cargar_peliculas()

cantidad_peliculas_por_director(peliculas)
director_mas_peliculas(peliculas)

titulo = input("Ingrese un título de película para ver sus actores: ")
actores_de_pelicula(peliculas, titulo)

actor = input("Ingrese el nombre de un actor para ver sus películas: ")
peliculas_de_actor(peliculas, actor)
