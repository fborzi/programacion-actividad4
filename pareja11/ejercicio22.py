ciudades = {
    "Junin": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# a)
print("a) Habitantes de Pergamino:", ciudades["Pergamino"])

# b)
ciudades["Lincoln"] = 42036
print("b) Se agregó Lincoln:", ciudades)

# c)
del ciudades["Junin"]
print("c) Se eliminó Junín:", ciudades)

# d)
ciudades["Rojas"] += 1000
print("d) Rojas ahora tiene:", ciudades["Rojas"])

# e)
ciudades["Pergamino"] = 91399
print("e) Pergamino actualizado:", ciudades["Pergamino"])

print("Diccionario final:", ciudades)
