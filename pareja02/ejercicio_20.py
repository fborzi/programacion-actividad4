"""
EJERCICIO 20: Procesamiento de números con dígitos repetidos
Solicitar números hasta leer uno sin dígitos repetidos.
Informar suma y cantidad de dígitos repetidos, porcentaje > 478 y promedio.
"""

from funciones import (tiene_digitos_repetidos, suma_digitos_repetidos, 
                       cantidad_digitos_repetidos)

print("Ingreso de números enteros")
print("(Se detendrá al ingresar un número sin dígitos repetidos)")
print("="*60)

numeros_procesados = []
mayores_478 = 0

while True:
    try:
        numero = int(input("\nIngrese un número entero: "))
        
        if not tiene_digitos_repetidos(numero):
            print(f"\n¡El número {numero} NO tiene dígitos repetidos!")
            print("Finalizando ingreso...")
            break
        
        # Procesar el número
        suma_rep = suma_digitos_repetidos(numero)
        cant_rep = cantidad_digitos_repetidos(numero)
        
        print(f"  Suma de dígitos repetidos: {suma_rep}")
        print(f"  Cantidad de dígitos repetidos: {cant_rep}")
        
        numeros_procesados.append(numero)
        
        if numero > 478:
            mayores_478 += 1
            
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Informes finales
print("\n" + "="*60)
print("RESUMEN FINAL:")
print("="*60)

if numeros_procesados:
    total = len(numeros_procesados)
    porcentaje = (mayores_478 / total) * 100
    promedio = sum(numeros_procesados) / total
    
    print(f"Total de números procesados: {total}")
    print(f"Números mayores que 478: {mayores_478}")
    print(f"Porcentaje de números > 478: {porcentaje:.2f}%")
    print(f"Promedio de los números: {promedio:.2f}")
else:
    print("No se procesaron números con dígitos repetidos.")
