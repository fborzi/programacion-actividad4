cantidad_numeros = 0
suma_total = 0
mayores478 = 0

numero = int(input("Ingrese números enteros (se detendrá cuando ingrese uno sin dígitos repetidos):"))
digitos = str(abs(numero))
tiene_repetidos = len(digitos) != len(set(digitos))

while tiene_repetidos: 
    cantidad_numeros += 1
    suma_total += numero

    #A: suma digitos repetidos
    suma_rep = 0 
    digitos_contados = set()

    for digito in digitos: 
        if digitos.count(digito) > 1 and digito not in digitos_contados:
            suma_rep += int(digito) * digitos.count(digito)
            digitos_contados.add(digito)
    print("Suma de digitos repetidos: " , suma_rep)

    #B: 
    repetidos = set()
    for digito in digitos:
        if digitos.count(digito) > 1:
            repetidos.add(digito)
        
    cant_rep = len(repetidos)
    print("La cantidad de digitos diferentes que se repiten son: ", cant_rep)

    #C: Contar si s mayor que 478

    if numero > 478:
        mayores478 += 1

# informe final

if cantidad_numeros > 0:
    #C
    porcentaje = (mayores478 / cantidad_numeros) * 100
    print("Porcentaje de números mayores que 478: ", porcentaje)

    #D
    promedio = suma_total / cantidad_numeros
    print('Promedios de números procesados: ', promedio)
    print('Total de números procesados: ', cantidad_numeros)
else:
    print("No se procesaron números con digitos repetidos")
    
