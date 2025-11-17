'''Producir una nueva lista con los nombres de la lista generada en el ejercicio anterior, donde los nombres hayan sido convertidos completamente a mayúsculas.
'''
nombres=["Gustavo","Gaston","Alfredo","Federico","Enzo","Santiago"]
#Transformar los nombres guardados en el array nombres
nombreMayuscula=[]
for nombre in nombres:
    nombreMayuscula.append(nombre.upper())
#Mostrar los cambios 
for name in nombreMayuscula:
    print(name)