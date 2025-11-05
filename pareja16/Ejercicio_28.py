
peliculas = {}

titulo = input("Titulo: ")
while titulo != "fin":
    director = input("Director: ")
    anio = int(input("Año: "))
    actores = input("Actores principales separados por coma: ").split(",")

    peliculas[titulo] = {"director": director, "anio": anio, "actores": actores}

    titulo = input("Titulo: ")

directores = {}
for t in peliculas:
    d = peliculas[t]["director"]
    directores[d] = directores.get(d, 0) + 1

print("Peliculas por director:", directores)

director_mayor = max(directores, key=directores.get)
print("Director con más películas:", director_mayor)

consulta_titulo = input("Ingresar titulo para ver actores: ")
if consulta_titulo in peliculas:
    print("Actores:", peliculas[consulta_titulo]["actores"])
else:
    print("No existe esa pelicula")

consulta_actor = input("Ingresar actor para ver peliculas: ")
lista = []
for t in peliculas:
    if consulta_actor in peliculas[t]["actores"]:
        lista.append(t)
print("Peliculas donde actua:", lista)

