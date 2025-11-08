# Diccionario para almacenar películas
# Clave: título
# Valor: diccionario con director, año, actores
peliculas = {}

# Carga de datos (puede adaptarse a ingreso manual o predefinido)
# Ejemplo de datos predefinidos para probar
peliculas = {
    "Inception": {
        "director": "Christopher Nolan",
        "anio": 2010,
        "actores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
    },
    "Interstellar": {
        "director": "Christopher Nolan",
        "anio": 2014,
        "actores": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]
    },
    "The Dark Knight": {
        "director": "Christopher Nolan",
        "anio": 2008,
        "actores": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Pulp Fiction": {
        "director": "Quentin Tarantino",
        "anio": 1994,
        "actores": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    },
    "Django Unchained": {
        "director": "Quentin Tarantino",
        "anio": 2012,
        "actores": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio"]
    },
}

# 1️⃣ Cantidad de películas dirigidas por cada director
peliculas_por_director = {}
for datos in peliculas.values():
    director = datos["director"]
    peliculas_por_director[director] = peliculas_por_director.get(director, 0) + 1

print("Cantidad de películas por director:")
for director, cantidad in peliculas_por_director.items():
    print(f"{director}: {cantidad}")

# 2️⃣ Director que dirigió más películas
director_max = max(peliculas_por_director, key=lambda d: peliculas_por_director[d])
print(f"\nDirector que dirigió más películas: {director_max} ({peliculas_por_director[director_max]} películas)")

# 3️⃣ Listar actores principales de una película dada
titulo_buscar = "Inception"
if titulo_buscar in peliculas:
    print(f"\nActores principales de '{titulo_buscar}': {', '.join(peliculas[titulo_buscar]['actores'])}")
else:
    print(f"\nNo existe la película '{titulo_buscar}'")

# 4️⃣ Listar todas las películas en las que participó un actor
actor_buscar = "Leonardo DiCaprio"
peliculas_actor = [titulo for titulo, datos in peliculas.items() if actor_buscar in datos["actores"]]

print(f"\nPelículas donde participó {actor_buscar}:")
if peliculas_actor:
    for titulo in peliculas_actor:
        print(titulo)
else:
    print("No se encontraron películas con ese actor.")
