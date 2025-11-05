from funciones import indice_mayor

cantidad = int(input("¿Cuántos números va a ingresar?: "))
lista_numeros = []

for i in range(cantidad):
    numero = int(input(f"Ingresar el número {i+1}: "))
    lista_numeros.append(numero)

indice = indice_mayor(lista_numeros)

print("Lista ingresada: ", lista_numeros)
print("El índice del mayor elemento es: ", indice)
print("El mayor elemento es: ", lista_numeros[indice])
