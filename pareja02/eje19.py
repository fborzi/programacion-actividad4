#EJE19


from Funcioness import digitos_repetidos

print("Pruebas de la función digitos_repetidos():\n")

# Ejemplos
numeros = [11223, 12345, 111, 1234567890, 100200]

for numero in numeros:
    repetidos = digitos_repetidos(numero)
    print(f"Número: {numero}")
    if repetidos:
        print(f"Dígitos repetidos: {repetidos}")
    else:
        print("No tiene dígitos repetidos")
    print()
