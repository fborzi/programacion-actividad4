# Operaciones con conjuntos (sets)

# Conjuntos de hormonas
hormona1 = set(['melanina', 'oxitocina', 'dopamina'])
hormona2 = set(['testosterona', 'melanina'])
hormona3 = set(['calcitonina', 'estradiol'])

print("\nConjuntos de hormonas:")
print(f"horm1 = {hormona1}")
print(f"horm2 = {hormona2}")
print(f"horm3 = {hormona3}")

# Informar si horm1 y horm2 comparten alguna hormona. ¿Y horm1 con horm3?
print("\nd) Verificar si comparten hormonas:")
interseccion_1_2 = hormona1 & hormona2
if interseccion_1_2:
    print(f"horm1 y horm2 SÍ comparten hormonas: {interseccion_1_2}")
else:
    print("horm1 y horm2 NO comparten hormonas")

interseccion_1_3 = hormona1 & hormona3
if interseccion_1_3:
    print(f"horm1 y horm3 SÍ comparten hormonas: {interseccion_1_3}")
else:
    print("horm1 y horm3 NO comparten hormonas")

# ¿Es el conjunto horm2 un subconjunto de horm1?
print("\ne) Verificar si horm2 es subconjunto de horm1:")
es_subconjunto = hormona2.issubset(hormona1)
if es_subconjunto:
    print("horm2 SÍ es un subconjunto de horm1")
else:
    print("horm2 NO es un subconjunto de horm1")

# Informar el conjunto de todas las hormonas (iterando)
print("\nf) Conjunto de todas las hormonas:")
todas_hormonas = hormona1 | hormona2 | hormona3
print("Todas las hormonas encontradas:")
for hormona in todas_hormonas:
    print(f"  - {hormona}")