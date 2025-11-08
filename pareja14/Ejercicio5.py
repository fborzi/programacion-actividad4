print("Ingrese la serie de nombres: ")
lista = []
nombres = ""
corte = 0
presen = 0

while corte == 0:
    nombres = input()
    if nombres == "":
        corte += 1
        break
    else:
        lista.append(nombres)
        continue

for x in lista:
    presen += 1
    print(f"#{presen}, ", x)

# Crear una nueva lista con los nombres completamente en mayúsculas
lista_mayus = [nombre.upper() for nombre in lista]

print("\nLista con nombres en MAYÚSCULAS:")
for i, nombre in enumerate(lista_mayus, start=1):
    print(f"#{i}, {nombre}")
