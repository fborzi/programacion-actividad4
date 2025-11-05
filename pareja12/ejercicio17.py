horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testorterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])
"""
#A: infromar si la horm1 y horm2 comparten alguna hormona
horm_compartida = []
for i in horm1:
    if i in horm2:
        horm_compartida.append(i)
        print('la hormona 1 y la hormona 2 compraten ', horm_compartida)
    elif i in horm3:
        horm_compartida.append(i)
        print('la hormona 1 y la hormona 3 compraten ', horm_compartida)

#B: horm2 es un subconjunto de horm1
if horm2 in horm1:
    print('Hormona 2 es un subconjunto de hormona 1')
else:
    print('Hormona 2 no es un subconjunto de hormona 1')
"""
#C: infromar el conjunto de todas las hormonas
lista = list(set(horm1).union(horm2, horm3))
for i in lista:
    print(i)