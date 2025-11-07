horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

print("Hormonas en común entre horm1 y horm2:", horm1 & horm2)
print("Hormonas en común entre horm1 y horm3:", horm1 & horm3)
print("¿horm2 es subconjunto de horm1?", horm2.issubset(horm1))

todas = horm1 | horm2 | horm3
print("\nTodas las hormonas:", todas)

print("\nListado de todas las hormonas:")
for h in todas:
    print("-", h)
