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