'''Dados los siguientes conjuntos de hormonas alteradas en varios pacientes, se pide:
a. Informar si horm1 y horm2 comparten alguna hormona. ¿Y horm1 con horm3?
b. ¿Es el conjunto horm2 un subconjunto de horm1?
c. Informar el conjunto de todas las hormonas (iterando por el conjunto).
>>> horm1 = set(['melanina', 'oxitocina', 'dopamina'])
>>> horm2 = set(['testosterona', 'melanina'])
>>> horm3 = set(['calcinotna', 'estradiol'])
'''
horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

print("Respuesta de pregunta uno")
print("La Hormona 1 comparte con la hormona 2: ",horm1 & horm2)
print("La hormona 1 comparte con la hormona 3:",horm1 & horm3)
print("Respuesta de pregunta dos")
print("En el conjunto Hormona 2 esta presente la hormona 1: ",horm2.issubset(horm1))
print("Respuesta de preguta tres")
todas=horm1|horm2|horm3
print("Todas las hormonas tienen: ")
for elemento in todas:
    print("-",elemento)

