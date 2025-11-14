from Funciones import digitos_repetidos

# Contadores
contador_numeros = 0
contador_mayores_478 = 0
acumulador_numeros = 0

while True:
    n = int(input("Ingrese un número entero: "))
    
    repetidos = digitos_repetidos(n)

    # Si NO hay dígitos repetidos → FIN
    if len(repetidos) == 0:
        print("Número SIN dígitos repetidos. Fin del programa.")
        break

    # Procesamiento
    suma_repetidos = sum(int(x) for x in repetidos)
    cantidad_repetidos = len(repetidos)

    print(" ▶ Dígitos repetidos:", repetidos)
    print("    Suma de dígitos repetidos:", suma_repetidos)
    print("    Cantidad de dígitos repetidos:", cantidad_repetidos)
    print("--------------------------------------------")

    # Estadísticas
    contador_numeros += 1
    acumulador_numeros += n

    if n > 478:
        contador_mayores_478 += 1

# Al finalizar, mostramos estadísticas
if contador_numeros > 0:
    porcentaje = (contador_mayores_478 / contador_numeros) * 100
    promedio = acumulador_numeros / contador_numeros

    print("\n== RESULTADOS FINALES ==")
    print("Porcentaje de números > 478:", round(porcentaje, 2), "%")
    print("Promedio de los números ingresados:", round(promedio, 2))
else:
    print("No se ingresaron números con dígitos repetidos.")