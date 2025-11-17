#EJEO7

from Funcioness import minimo_elemento

# Pruebas de la función
print("Pruebas de la función minimo_elemento():\n")

# Ejemplo 1: Lista de números
lista1 = [4, 8, 15, 16, 23, 42]
resultado1 = minimo_elemento(lista1)
print(f"minimo_elemento({lista1})")
print(f"Resultado: {resultado1}\n")

# Ejemplo 2: String (secuencia de caracteres)
lista2 = "PYTHON"
resultado2 = minimo_elemento(lista2)
print(f"minimo_elemento('{lista2}')")
print(f"Resultado: '{resultado2}'\n")

# Ejemplo 3: Lista vacía
lista3 = []
resultado3 = minimo_elemento(lista3)
print(f"minimo_elemento({lista3})")
print(f"Resultado: {resultado3}\n")

# Ejemplo 4: Lista de strings
lista4 = ["manzana", "banana", "cereza", "durazno"]
resultado4 = minimo_elemento(lista4)
print(f"minimo_elemento({lista4})")
print(f"Resultado: {resultado4}")
