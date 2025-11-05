
from funciones import suma_digitos, sumatoria_digitos

cantidad = int(input("Decidir la cantidad de numeros a ingresr: : "))
lista_numeros = []

for i in range(cantidad):
    numero = int(input(f"Ingresar el número {i+1}: "))
    lista_numeros.append(numero)

print("Suma de dígitos de cada número: ")
for numero in lista_numeros:
    print(f"{numero} → {suma_digitos(numero)}")

print("Sumatoria de dígitos de toda la lista: ")
print(sumatoria_digitos(lista_numeros))
