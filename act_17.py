horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

interseccion_1_2 = horm1 & horm2
print(f"Hormonas compartidas entre horm1 y horm2: {interseccion_1_2}")

interseccion_1_3 = horm1 & horm3
# 2. Informar el resultado verificando la longitud (len())
if len(interseccion_1_3) == 0:
    print("Horm1 y Horm3 no comparten ninguna hormona. (La intersección es vacía).")
else:
    print(f"Horm1 y Horm3 comparten las siguientes hormonas: {interseccion_1_3}")

len_horm2 = len(horm2)
len_interseccion = len(horm2 & horm1)

es_subconjunto = len_horm2 == len_interseccion

print(f"Longitud de horm2: {len_horm2}")
print(f"Longitud de la intersección (horm2 & horm1): {len_interseccion}")
print(f"¿Son iguales las longitudes? {es_subconjunto}")

todas_las_hormonas = horm1 | horm2 | horm3
print("Conjunto de todas las hormonas únicas:")

# Iterando el conjunto:
for hormona in todas_las_hormonas:
    print(f"- {hormona}")