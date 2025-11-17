def suma_digitos(n):
#calcula la suma de los digitos de un numero entero

    #convertir el numero a cadena y sumar cada digito
    return sum(int(digito) for digito in str(n))

def sumatoria_digitos(lista):

    #usar la comprension de lista aplicando la anterior a cada elemento
    return [suma_digitos (num) for num in lista]

print (sumatoria_digitos(["200","300","40000","78569"]))