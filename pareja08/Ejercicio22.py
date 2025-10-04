habitantes = { "Junin": 102023, "Rojas": 28654, "Pergamino": 80569 }

# a)
print(f"Habitantes de Pergamino: {habitantes['Pergamino']}")

# b)
habitantes["Lincoln"] = 42036

# c)
del habitantes["Junin"]

# d)
habitantes["Rojas"] += 1000

# e)
habitantes['Pergamino'] = 91399

print(habitantes)