def cargar_nombres(): 
    #Lista vacia para almacenar nombres
    nombres = []

    nombre=input('Ingrese un nombre:')
    #Ingreso de nombres
    while nombre != "":
        nombres.append(nombre)
        nombre = input("Ingrese otro nombre : ")


    print ("Lista de nombres ingresados:") #Mostrar los nombres ingresados
    for n in nombres:
        print("-",n)
    return nombres 