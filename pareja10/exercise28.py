movies = {}

while True:
    title = input("Enter movie title (or 'end' to finish): ").strip()
    if title.lower() == "end":
        break

    director = input("Enter director's name: ").strip()
    year = int(input("Enter release year: "))
    actorsInput = input("Enter main actors (separated by commas): ")
    actors = [actor.strip() for actor in actorsInput.split(",") if actor.strip() != ""]

    movies[title] = {
        "director": director,
        "year": year,
           "actors": actors
    }

print("\n--- REPORTS ---")

directorCount = {}
for data in movies.values():
    director = data["director"]
    directorCount[director] = directorCount.get(director, 0) + 1

print("\nMovies directed by each director:")
for director, count in directorCount.items():
    print(f"{director}: {count}")

if directorCount:
    topDirector = max(directorCount, key=directorCount.get)
    print("\nDirector with the most movies:", topDirector)
else:
    print("\nNo directors registered.")

searchTitle = input("\nEnter a movie title to list its actors: ").strip()
if searchTitle in movies:
    print("Actors in", searchTitle + ":")
    for actor in movies[searchTitle]["actors"]:
        print("-", actor)
else:
   print("That movie is not in the collection.")

searchActor = input("\nEnter an actor's name to list their movies: ").strip()
foundMovies = [title for title, data in movies.items() if searchActor in data["actors"]]

if foundMovies:
    print("\nMovies featuring", searchActor + ":")
    for title in foundMovies:
        print("-", title)
else:
    print("\nNo movies found for that actor.")