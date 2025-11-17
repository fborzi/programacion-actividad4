peliculas = {}
cont = 1000

for i in range (cont):
    titulo = input("titulo de la pelicula (0 para terminar): ")
    if titulo == "0":
        break
    director = input("director: ")
    anio = input("año de estreno: ")
    actores = input("actores principales (separados por coma): ").split(",")

    peliculas[titulo] = [director, anio, [a.strip() for a in actores]]

directores = {}
for datos in peliculas.values():
    director = datos[0]
    directores[director] = directores.get(director, 0) + 1

print("\npeliculas por director: ")
for d, c in directores.items():
    print(f"{d}: {c}")

mas_dirigio = max(directores, key=directores.get)
print(f"\nel director con mas peliculas es: {mas_dirigio}")

titulo_buscar = input("\ningrese un titulo para ver sus actores: ")
if titulo_buscar in peliculas:
    print("actores: ", peliculas[titulo_buscar][2])
else:
    print("pelicula no encontrada.")

actor_buscar = input("\ningrese un actor para ver sus peliculas: ").strip()
print(f"\npeliculas donde actuo {actor_buscar}:")
for t, datos in peliculas.items():
    if actor_buscar in datos[2]:
        print("-", t)