# Dada la lista b = [ 4, "palabra", [0, 1], 9.6, False ]:
# Utilizar una instrucción para determinar si los siguientes elementos pertenecen a la lista:
# 9.6 0 False [0, 1] 4.0 "p"
# Utilizar una instrucción para determinar en qué posición (índice) se encuentra el elemento [0, 1].
# b = [ 4, "palabra", [0, 1], 9.6, False ]

b = [4, "palabra", [0, 1], 9.6, False]

# a 
print(f"9.6 in list: {9.6 in b}")
print(f"0 in list: {0 in b}")
print(f"False in list: {False in b}")
print(f"[0, 1] in list: {[0, 1] in b}")
print(f"4.0 in list: {4 in b}")
print(f"'p' in list: {'p' in b}")

# b
print(f"Index of [0, 1]: {b.index([0, 1])}")