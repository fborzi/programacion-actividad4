
# Devuelve los dos valores minimos de una lista de numeros.
# Si la lista tiene menos de dos elementos, devuelve None en el segundo valor.
# parametro lista: []
def dos_minimos(lista):
    largo = len(lista)
    if largo < 2:
        print("Primer valor menor: ", lista[0] if largo == 1 else "NONE", 
              ". Segundo valor menor: NONE")
        return (None,"NONE", None,"NONE")
    elif largo == 1:
        return (lista[0], None)
    
    min1 = float('inf')
    min2 = float('inf')
    
    for num in lista:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
            
    if min2 == float('inf'):
        min2 = None
    print("Primer valor menor: ", min1, ". Segundo valor menor: ", min2)
    return (min1, min2)

# Agregar nombres a una lista hasta que el usuario decida finalizar ingresando una cadena vacia.
def agregar_nombres():
    nombres = []
    while True:
        nombre = input("Introduce un nombre (o presiona Enter para dejar en blanco y finalizar): ")
        if nombre == "" or nombre == " ":
            break
        nombres.append(nombre)

    print("\nLista de nombres ingresados:")
    for n in nombres:
        print(n)


def minimo_elemento(lista):
    if not lista: 
        return None
    
    minimo = lista[0]  
    for elemento in lista[1:]:  
        if elemento < minimo:
            minimo = elemento
    print(f"El elemento mínimo es: {minimo}")
    return minimo   
    return nombres

#Convierte en mayusculas una lista de nombres.
#parametro nombres: []
def nombres_mayusculas(nombres):
    nombresMayus = []
    for nombre in nombres:
            nombre = nombre.upper()
            nombresMayus.append(nombre)

    print("\nLista de nombres en mayúsculas:", nombresMayus)
    return nombresMayus


# Retorna una lista con los dígitos que componen al número pasado por parámetro.
# parametro numero: int
def digitos(numero):
    digitos = []
    for digito in str(numero):
        digitos.append(int(digito))
    print(digitos) 
    return digitos
# Juego de Piedra, Papel o Tijera


def piedra_papel_tijera(uno, dos):
    
    uno = uno.lower()
    dos = dos.lower()

    
    if uno == dos:
        return 0

    if (uno == "piedra" and dos == "tijera") or \
       (uno == "tijera" and dos == "papel") or \
       (uno == "papel" and dos == "piedra"):
        return 1  
    else:
        return 2  
    

    def borrar_adyacentes(lista):
     if not lista:  
        return []

    resultado = [lista[0]]  

    for elemento in lista[1:]:
        if elemento != resultado[-1]: 
            resultado.append(elemento)

    return resultado
   
