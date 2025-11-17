peliculas = {}


titulo = input("Ingrese el nombre de la pelicula. Para finalizar presione enter: ").lower()
while titulo != "":
    director = input("Ingrese el nombre del director de la pelicula: ").lower()
    anio_estreno = int(input("Ingrese el año de estreno de la pelicula: "))
    
    actores = []
    actor = input(f"Ingrese el nombre del actor {len(actores)+1}. Para finalizar presione enter: ").lower()
    while actor != "":
        actores.append(actor)
        actor = input(f"Ingrese el nombre del actor {len(actores)+1}. Para finalizar presione enter: ").lower()
    
    peliculas[titulo] = {
        'director': director,
        'estreno': anio_estreno,
        'actores': actores
    }
    
    print("Pelicula agregada correctamente.")
    
    titulo = input("Ingrese el nombre de la pelicula. Para finalizar presione enter: ").lower()

# a)
peliculas_por_director = {}
for pelicula in peliculas:
   if not peliculas[pelicula]['director'] in peliculas_por_director:
       peliculas_por_director[peliculas[pelicula]['director']] = 1
   else:
       peliculas_por_director[peliculas[pelicula]['director']] += 1

print("a) Peliculas dirigidas:")
director_mas_peliculas = None
for director in peliculas_por_director:
    print(f"● {director.title()}: {peliculas_por_director[director]}")
    # b)
    if peliculas_por_director[director] > peliculas_por_director[director_mas_peliculas]:
        director_mas_peliculas = director

print(f"b) Director con mas peliculas dirigidas: {director_mas_peliculas.title()} ")

# c)
print("c)")
pelicula = input("Ingrese el nombre de la pelicula para listar sus actores: ").lower()
while not pelicula in peliculas:
    pelicula = input("Pelicula no encontrada. Intentelo nievamente: ").lower()

print(f"Actores de {pelicula.title()}")
for actor in peliculas[pelicula]['actores']:
    print(f"● {actor.title()}")

# d)
print("d)")
actor = input("Ingrese el nombre del actor para listar sus peliculas: ").lower()

actor_en_peliculas = []
for p in peliculas:
    if actor in peliculas[p]['actores']:
        actor_en_peliculas.append(p)

if len(actor_en_peliculas) > 0:
    print(f"Peliculas donde participo {actor.title()}:")
    for p in actor_en_peliculas:
        print(f"● {p.title}")
else:
    print(f"El actor {actor.title()}, no participo en ninguna de las peliculas.")