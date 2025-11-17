from funciones import digitos_repetidos

numeros = []
mayores_478 = 0

n = int(input("ingrese un numero entero: "))
repetidos = digitos_repetidos(n)

while repetidos:
    numeros.append(n)
    if n > 478:
        mayores_478 += 1
    
    # a)
    suma_repetidos = sum(repetidos)
    
    # b)
    cantidad_repetidos = len(repetidos)
    
    print(f"numero ingresado: {n}")
    print(f"a) suma de digitos repetidos: {suma_repetidos}")
    print(f"b) cantidad de digitos repetidos: {cantidad_repetidos}")
    
    n = int(input("ingrese otro numero: "))
    repetidos = digitos_repetidos(n)
    

# c)
if numeros:
    porcentaje = (mayores_478 / len(numeros)) * 100
    
    # d)
    promedio = sum(numeros) / len(numeros)
    
    print(f"c) porcentaje de numeros mayores a 478: {porcentaje}%")
    print(f"d) promedio de los numeros precesados: {promedio}")
else:
    print("no se procesaron numeros con digitos repetidos")            
