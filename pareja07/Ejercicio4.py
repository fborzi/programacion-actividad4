nombres = []

while True:
    nombre = input("Ingrese un nombre (o presione Enter para finalizar): ")
    if nombre == "":
        break
    nombres.append(nombre)

print("\nLista de nombres ingresados:")
for n in nombres:
    print(n)
