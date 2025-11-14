b = [4, "palabra", [0, 1], 9.6, False]

# Verifico con un "in" si los elementos solicitados pertenecen a la lista

print(9.6 in b)        # True
print(0 in b)          # True
print(False in b)      # True
print([0, 1] in b)     # True
print(4.0 in b)        # True   → 4.0 == 4 → Python los considera iguales para "in"
print("p" in b)        # False  → "p" no está como elemento individual

print(b.index([0, 1])) 
