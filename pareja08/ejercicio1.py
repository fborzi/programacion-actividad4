#Dada la lista b = [ 4, "palabra", [0, 1], 9.6, False ]:
#A) Utilizar una instrucción para determinar si los siguientes elementos pertenecen a la lista:
#9.6 0 False [0, 1] 4.0 "p"
#B) Utilizar una instrucción para determinar en qué posición (índice) se encuentra el elemento [0, 1].
from funciones import pertenecer
b=[4, "palabra", [0,1], 9.6, False]
verificar=[9.6, 0, [0,1], 4.0, False, "p"]
encontrados=[]
noPertenecen=[]

for elemento in verificar:
    if pertenecer(elemento,b):
        encontrados.append(elemento)
    else:
        noPertenecen.append(elemento)

if len(encontrados)==len(b):
    print("Se encontraron todos los elementos ")
    print(encontrados)
else:
    print("No se encontraron todos los elementos")
    print("Solo estos:", encontrados)
    print("Los que no se encontraron fueron: ", noPertenecen)
            
