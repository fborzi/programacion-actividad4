from funciones import cargar_peliculas, cantidad_peliculas_por_director,director_mas_peliculas, actores_de_pelicula, peliculas_de_actor

peliculas = cargar_peliculas()

cantidad_peliculas_por_director(peliculas)
director_mas_peliculas(peliculas)

titulo = input("Ingrese un título de película para ver sus actores: ")
actores_de_pelicula(peliculas, titulo)

actor = input("Ingrese el nombre de un actor para ver sus películas: ")
peliculas_de_actor(peliculas, actor)
