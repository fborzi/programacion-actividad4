peliculas = {}

print("Ingrese 'fin' como título para finalizar.")

titulo = input("Ingrese el título de la película: ")

while titulo != 'fin':
    director = input("Director: ")
    anio = int(input("Año de estreno: "))

    print("Ingrese los actores principales (esriba 'fin' para finalizar): ")
    actores = []
    actor = input("Actor: ")

    while actor != 'fin':
        actores.append(actor)
        actor = input("Actor: ")
    
    peliculas[titulo] = {
        "director": director,
        "año": anio,
        "actores": actores
    }

    print("Pelicula registrada correctamente.")
    titulo = input("Ingrese el título de la película: ")

#1. Informar cuantas peliculas dirigio cada director.

peliculas_por_director = {}

for titulo in peliculas:
    director = peliculas[titulo]["director"]

    if director in peliculas_por_director:
        peliculas_por_director[director] += 1
    else:
        peliculas_por_director[director] = 1
print("1. Peliculas por director: ")
for director in peliculas_por_director:
    print(director, ":", peliculas_por_director[director], "pelicula/s")

#2. Informar el director que dirigio mas peliculas.

if len(peliculas_por_director) > 0:
    director_max = ""
    max_peliculas = 0 

    for director in peliculas_por_director:
        if peliculas_por_director[director] > max_peliculas:
            max_peliculas = peliculas_por_director[director]
            director_max = director
    
    print("2. Direcotr con mas peliculas:")
    print(director_max, "con", max_peliculas, "pelicula/s")
else:
    print("2. No hay directores registrados.")

#3. Listar actores de una pelicula espeifica

print("3. Buscar actores de una pelicula: ")
titulo_buscar = input("Ingrese el titulo de la pelicula: ")

if titulo_buscar in peliculas:
    print("Actores principales de: ", titulo_buscar)
    for actor in peliculas[titulo_buscar]["actores"]:
        print("-", actor)
else:
    print("No se encontro la pelicula ", titulo_buscar)

#4. Listar peliculas donde participo un actor

print("4. Buscar peliculas de un actor:")
actor_buscar = input(" Ingrese el nombre del actor: ")

peliculas_encontradas = []

for titulo in peliculas:
    if actor_buscar in peliculas[titulo]["actores"]:
        peliculas_encontradas.append(titulo)

if len(peliculas_encontradas) > 0:
    print("Peliculas donde participó:", actor_buscar)
    for titulo in peliculas_encontradas:
        print("-", titulo)
else:
    print("No se encontraron peliculas con", actor_buscar)
    