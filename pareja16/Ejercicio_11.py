
from funciones import ocurrencias

texto = input("Ingresar elementos separados por espacios: ")


lista = texto.split()

resultado = ocurrencias(lista)

print("Lista original: ", lista)
print("Lista con ocurrencias: ", resultado)
