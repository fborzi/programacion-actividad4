# Escribí un programa que permita al usuario cargar datos de una colección de películas en una estructura que permita acceso directo por título. De cada película se debe almacenar: título, director, año de estreno, listado de actores principales.
# Informar cuántas películas dirigió cada director.
# Informar cuál fue el director que dirigió más películas.
# Dado el título de una película, listar todos sus actores principales.
# Dado el nombre de un actor, listar todos los títulos de películas donde participó.


class Pelicula:
    def __init__(self, titulo, director, anio, actores):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.actores = actores

def cargar_peliculas():
    peliculas = {}
    while True:
        titulo = input("Ingrese título de la película (vacío para terminar): ").strip()
        if not titulo:
            break
        
        director = input("Director: ").strip()
        anio = int(input("Año de estreno: "))
        
        actores = []
        while True:
            actor = input("Actor principal (vacío para terminar): ").strip()
            if not actor:
                break
            actores.append(actor)
            
        peliculas[titulo] = Pelicula(titulo, director, anio, actores)
    
    return peliculas

def peliculas_por_director(peliculas):
    conteo = {}
    for pelicula in peliculas.values():
        conteo[pelicula.director] = conteo.get(pelicula.director, 0) + 1
    return conteo

def director_con_mas_peliculas(conteo_directores):
    if not conteo_directores:
        return None
    return max(conteo_directores.items(), key=lambda x: x[1])[0]

def listar_actores_pelicula(peliculas, titulo):
    if titulo in peliculas:
        return peliculas[titulo].actores
    return []

def peliculas_de_actor(peliculas, actor_buscado):
    titulos = []
    for pelicula in peliculas.values():
        if actor_buscado in pelicula.actores:
            titulos.append(pelicula.titulo)
    return titulos

def main():
    # Cargar películas
    print("=== Carga de películas ===")
    peliculas = cargar_peliculas()
    
    # Mostrar películas por director
    print("\n=== Películas por director ===")
    conteo = peliculas_por_director(peliculas)
    for director, cantidad in conteo.items():
        print(f"{director}: {cantidad} películas")
    
    # Mostrar director con más películas
    director_max = director_con_mas_peliculas(conteo)
    if director_max:
        print(f"\nDirector con más películas: {director_max}")
    
    # Buscar actores de una película
    titulo = input("\nIngrese título para ver sus actores: ")
    actores = listar_actores_pelicula(peliculas, titulo)
    if actores:
        print(f"Actores en {titulo}:")
        for actor in actores:
            print(f"- {actor}")
    else:
        print("Película no encontrada")
    
    # Buscar películas de un actor
    actor = input("\nIngrese actor para ver sus películas: ")
    titulos = peliculas_de_actor(peliculas, actor)
    if titulos:
        print(f"Películas de {actor}:")
        for titulo in titulos:
            print(f"- {titulo}")
    else:
        print("No se encontraron películas para ese actor")

if __name__ == "__main__":
    main()