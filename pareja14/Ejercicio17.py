horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcitonina', 'estradiol'])

# verificar si comparten alguna hormona:
print("¿horm1 y horm2 comparten alguna hormona?", bool(horm1 & horm2))
print("horm1 y horm3 comparten alguna hormona?", bool(horm1 & horm3))

# verificacion de horm2 si es subconjunto de horm1
print("¿horm2 es subconjunto de horm1?", horm2.issubset(horm1))

# conjunto de todas las hormonas:
todas_las_hormonas = horm1 | horm2 | horm3 #une todos los conjuntos

print("todas las hormonas:")
for hormona in todas_las_hormonas:
    print("-", hormona)
