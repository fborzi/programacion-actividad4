
from funciones import borrar_adyacentes

texto = input("Ingresar caracteres sin espacio (ej: aabbccdd): ")

lista = list(texto) 

resultado = borrar_adyacentes(lista)

print("Lista original: ", lista)
print("Lista con adyacentes borrados: ", resultado)

