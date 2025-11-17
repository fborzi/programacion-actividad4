ciudades = {
    "Junin": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# a) Informar la cantidad de habitantes que tiene Pergamino.
print("Habitantes de Pergamino", ciudades["Pergamino"])

# b) Agregar a Lincoln con 42.036 habitantes.
ciudades["Lincoln"] = 42036

# c) Eliminar a Junin
del ciudades["Junin"]

# d) Incrementar los habitantes de Rojas en 1000
ciudades["Rojas"] += 1000

# e) Modificar la cantidad de habitantes dde Pergamino por 91399
ciudades["Pergamino"] = 91399

print("Total de habitantes por ciudad:" , ciudades)