#EJE05
"Lista para almacenar los nombres"
nombres = []

print("Ingreso de nombres")
print("(Presione Enter sin escribir nada para terminar)")
print("-" * 50)

while True:
    nombre = input("Ingrese un nombre: ")
    
    # Si el nombre está en blanco, terminar
    if nombre == "":
        break
    
    # Agregar el nombre a la lista
    nombres.append(nombre)

# Imprimir los nombres ingresados
print("\n" + "="*50)
print(f"Se ingresaron {len(nombres)} nombres:")
print("="*50)

if nombres:
    for i, nombre in enumerate(nombres, 1):
        print(f"{i}. {nombre}")
else:
    print("No se ingresaron nombres.")
