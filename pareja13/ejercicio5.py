from ejercicio4 import cargar_nombres
#Nombre con mayuscula
nombres = cargar_nombres()
nombres_m = [n.upper() for n in nombres]

print ("Lista de nombres en mayusucula:")
for n in nombres_m:
    print("-",n)
