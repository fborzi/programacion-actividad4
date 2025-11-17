# Escribí un programa que solicite el ingreso de números enteros hasta leer uno que no tenga dígitos repetidos. Se pide informar:
# Para cada número, la suma de los dígitos que se repiten en ese número.
# Para cada número, la cantidad de dígitos que se repiten en ese número.
# Al finalizar, el porcentaje de números procesados mayores que 478.
# Al finalizar, el promedio de los números procesados.

import funciones

cantidad_numeros = 0 
suma_todos = 0
cantidad_mayores_478 = 0  
continuar = True
    
print("Ingrese números enteros.El programa termina cuando ingrese un número sin dígitos repetidos.\n")
    

while continuar:
       
    numero = int(input("Ingrese un número entero: "))
    conteo = funciones.contar_digitos(numero)

    hay_repetidos = funciones.tiene_digitos_repetidos(conteo)

    if not hay_repetidos:
        print(f"\n¡El número {numero} no tiene dígitos repetidos!")
        print("Fin del programa.\n")
        continuar = False
    else:

        suma_rep, cant_rep = funciones.calcular_suma_y_cantidad_repetidos(conteo)

        funciones.mostrar_estadisticas_numero(numero, suma_rep, cant_rep)

        cantidad_numeros = cantidad_numeros + 1
        suma_todos = suma_todos + numero

        if numero > 478:
            cantidad_mayores_478 = cantidad_mayores_478 + 1

    funciones.mostrar_estadisticas_finales(cantidad_numeros, cantidad_mayores_478, suma_todos)
