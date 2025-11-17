#EJE29

print("Sistema de Gestión de Películas")
print("="*60)

# Diccionario de películas (título: [director, año, [actores]])
peliculas = {
    "El Padrino": ["Francis Ford Coppola", 1972, ["Marlon Brando", "Al Pacino", "James Caan"]],
    "Pulp Fiction": ["Quentin Tarantino", 1994, ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]],
    "El Caballero Oscuro": ["Christopher Nolan", 2008, ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]],
    "Inception": ["Christopher Nolan", 2010, ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]],
    "Forrest Gump": ["Robert Zemeckis", 1994, ["Tom Hanks", "Robin Wright", "Gary Sinise"]],
    "Matrix": ["Lana Wachowski", 1999, ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]],
    "Interstellar": ["Christopher Nolan", 2014, ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]],
}

print("\nPelículas en la colección:")
for titulo, datos in peliculas.items():
    director, año, actores = datos
    print(f"  • {titulo} ({año}) - Dir: {director}")

print("\n" + "="*60)

# a) Informar cuántas películas dirigió cada director
print("\na) Películas por director:")
peliculas_por_director = {}
for datos in peliculas.values():
    director = datos[0]
    if director in peliculas_por_director:
        peliculas_por_director[director] += 1
    else:
        peliculas_por_director[director] = 1

for director, cantidad in peliculas_por_director.items():
    print(f"   {director}: {cantidad} película(s)")

# b) Director que dirigió más películas
print("\nb) Director con más películas:")
director_max = max(peliculas_por_director.keys(), key=lambda d: peliculas_por_director[d])
print(f"   {director_max} con {peliculas_por_director[director_max]} películas")

# c) Listar actores de una película específica
print("\nc) Actores principales de 'Inception':")
titulo_buscar = "Inception"
if titulo_buscar in peliculas:
    actores = peliculas[titulo_buscar][2]
    for actor in actores:
        print(f"   - {actor}")
else:
    print(f"   Película '{titulo_buscar}' no encontrada")

# d) Películas donde participó un actor
print("\nd) Películas donde participó 'Leonardo DiCaprio':")
actor_buscar = "Leonardo DiCaprio"
peliculas_actor = []
for titulo, datos in peliculas.items():
    actores = datos[2]
    if actor_buscar in actores:
        peliculas_actor.append(titulo)

if peliculas_actor:
    for titulo in peliculas_actor:
        print(f"   - {titulo}")
else:
    print(f"   {actor_buscar} no aparece en ninguna película registrada")

# Ejemplo adicional
print("\ne) Películas donde participó 'Christian Bale':")
actor_buscar2 = "Christian Bale"
for titulo, datos in peliculas.items():
    actores = datos[2]
    if actor_buscar2 in actores:
        print(f"   - {titulo}")
