# Definición de los conjuntos
horm1 = {'melanina', 'oxitocina', 'dopamina'}
horm2 = {'testosterona', 'melanina'}
horm3 = {'calcinotna', 'estradiol'}

# 1. Verificar si horm1 y horm2 comparten alguna hormona
comparten_horm1_horm2 = horm1.intersection(horm2)
print("Horm1 y Horm2 comparten:", comparten_horm1_horm2 if comparten_horm1_horm2 else "ninguna hormona")

# 2. Verificar si horm1 y horm3 comparten alguna hormona
comparten_horm1_horm3 = horm1.intersection(horm3)
print("Horm1 y Horm3 comparten:", comparten_horm1_horm3 if comparten_horm1_horm3 else "ninguna hormona")

# 3. Verificar si horm2 es subconjunto de horm1
es_subconjunto = horm2.issubset(horm1)
print("¿Horm2 es subconjunto de Horm1?:", es_subconjunto)

# 4. Obtener todas las hormonas (unión de los conjuntos)
todas_hormonas = horm1.union(horm2, horm3)
print("Conjunto total de hormonas:")
for hormona in todas_hormonas:
    print("-", hormona)
