#Ejercicio28
#Carga de películas
peliculas = {}

titulo = input("Ingrese el título de la película (o 'fin' para terminar): ")
while titulo.lower() != "fin":
    director = input("Ingrese el nombre del director: ")
    anio = int(input("Ingrese el año de estreno: "))
    actores = input("Ingrese los actores principales separados por comas: ").split(",")

  
    actores = [actor.strip() for actor in actores]

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": actores
    }

    titulo = input("Ingrese el título de la película (o 'fin' para terminar): ")

#a) Informar cuántas películas dirigió cada director 
directores = {}
for datos in peliculas.values():
    nombre_director = datos["director"]
    if nombre_director in directores:
        directores[nombre_director] += 1
    else:
        directores[nombre_director] = 1

print("Cantidad de películas dirigidas por cada director:")
for director, cantidad in directores.items():
    print("Director:", director, "-", cantidad, "películas")

#b) Informar cuál fue el director que dirigió más películas
if directores:
    director_mas_peliculas = max(directores, key=directores.get)
    print("El director que dirigió más películas es:", director_mas_peliculas, 
          "con", directores[director_mas_peliculas], "películas.")

#c) Dado el título de una película, listar sus actores 
titulo_buscar = input("Ingrese el título de la película para ver sus actores: ")
if titulo_buscar in peliculas:
    print("Los actores principales de", titulo_buscar, "son:", ', '.join(peliculas[titulo_buscar]["actores"]))
else:
    print("No se encontró la película con el título:", titulo_buscar)

#d) Dado el nombre de un actor, listar las películas donde participó 
actor_buscar = input("Ingrese el nombre de un actor: ")
peliculas_actor = [titulo for titulo, datos in peliculas.items() if actor_buscar in datos["actores"]]

if peliculas_actor:
    print("El actor", actor_buscar, "participó en las películas:", ', '.join(peliculas_actor))
else:
    print("El actor", actor_buscar, "no se encuentra en ninguna película registrada.")
