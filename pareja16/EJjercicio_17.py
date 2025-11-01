
horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

# ¿Comparten alguna hormona?
print("Horm1 y Horm2 comparten:", horm1 & horm2)
print("Horm1 y Horm3 comparten:", horm1 & horm3)

# ¿Horm2 es subconjunto de Horm1?
print("Horm2 es subconjunto de Horm1:", horm2.issubset(horm1))

# Conjunto de todas las hormonas (uniendo todos)
todas = horm1 | horm2 | horm3
print("Todas las hormonas:")
for h in todas:
    print("-", h)
