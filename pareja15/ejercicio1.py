# Operaciones con listas
b = [4, "palabra", [0, 1], 9.6, False]
#Determinar si los elementos pertenecen a la lista
print("\na) Verificar pertenencia de elementos:")
elementos_a_verificar = [9.6, 0, False, [0, 1], 4.0, "p"]

for elemento in elementos_a_verificar:
    if elemento in b:
        print(f"{elemento} -> SÍ pertenece a la lista")
    else:
        print(f"{elemento} -> NO pertenece a la lista")

#Determinar en qué posición está el elemento [0, 1]
print("\nb) Posición del elemento [0, 1]:")
posicion = b.index([0, 1])
print(f"El elemento [0, 1] está en la posición (índice): {posicion}")