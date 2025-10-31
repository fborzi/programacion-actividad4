"""
EJERCICIO 18: Operaciones con conjuntos (hormonas)
Trabajar con conjuntos de hormonas alteradas en pacientes.
"""

# Conjuntos de hormonas
horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcitonina', 'estradiol'])

print("Conjuntos de hormonas alteradas:")
print(f"horm1: {horm1}")
print(f"horm2: {horm2}")
print(f"horm3: {horm3}")

print("\n" + "="*60)

# a) Verificar si comparten hormonas
print("\na) ¿Comparten hormonas?")

# horm1 y horm2
interseccion_1_2 = horm1 & horm2
if interseccion_1_2:
    print(f"   horm1 y horm2 SÍ comparten hormonas: {interseccion_1_2}")
else:
    print("   horm1 y horm2 NO comparten hormonas")

# horm1 y horm3
interseccion_1_3 = horm1 & horm3
if interseccion_1_3:
    print(f"   horm1 y horm3 SÍ comparten hormonas: {interseccion_1_3}")
else:
    print("   horm1 y horm3 NO comparten hormonas")

# b) Verificar si horm2 es subconjunto de horm1
print("\nb) ¿Es horm2 un subconjunto de horm1?")
es_subconjunto = horm2.issubset(horm1)
print(f"   {es_subconjunto}")
if not es_subconjunto:
    print(f"   (horm2 tiene '{horm2 - horm1}' que no está en horm1)")

# c) Conjunto de todas las hormonas
print("\nc) Conjunto de todas las hormonas:")
todas_hormonas = horm1 | horm2 | horm3
print("   Iterando por el conjunto:")
for hormona in todas_hormonas:
    print(f"   - {hormona}")

print(f"\n   Total de hormonas diferentes: {len(todas_hormonas)}")
