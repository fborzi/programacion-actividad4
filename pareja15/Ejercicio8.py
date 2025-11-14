from funciones import piedra_papel_tijera

print(piedra_papel_tijera('papel', 'tijera'))    #gana la tijera, o sea 2
print(piedra_papel_tijera('piedra', 'piedra'))   #empate, o sea 0
print(piedra_papel_tijera('PIEDRA', 'TiJeRa'))   #gana la piedra, o sea 1, mayusculas y minusculas no importan
