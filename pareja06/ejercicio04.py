"""
Ejercicio 4:
 Programa que pide nombres al usuario hasta que ingrese uno en blanco
 Luego imprime todos los nombres ingresados
"""

# Creamos una lista vacía para almacenar los nombres
nombres = []

print("=== INGRESO DE NOMBRES ===")
print("Ingrese nombres (Enter sin escribir nada para terminar)")
print()

# Bucle infinito que se romperá cuando se ingrese un nombre en blanco
while True:
    # Solicitamos el ingreso de un nombre
    nombre = input("Ingrese un nombre: ")
    
    # Si el nombre está vacío (solo presionó Enter), salimos del bucle
    if nombre == "":
        break
    
    # Agregamos el nombre al final de la lista usando append()
    nombres.append(nombre)

# Mostramos los resultados
print()
print("=== NOMBRES INGRESADOS ===")
print(f"Total de nombres: {len(nombres)}")
print()

# Iteramos por la lista e imprimimos cada nombre
print("Lista de nombres:")
for nombre in nombres:
    print(f"- {nombre}")

# mostrar la lista completa
print()
print(f"Lista completa: {nombres}")