productos = {}

print("=====================================")
print("Carga de productos")
print("=====================================")

codigo = input("Ingrese el codigo de producto (ingrese -1 para terminar): ")

while codigo != "-1":
    tipo = input("Tipo (lácteo/almacen/verduleria/limpieza/carniceria/otros): ")
    descripcion = input("Descripcion: ")
    stock_actual = int(input("Stock actual: "))
    stock_minimo = int(input("Strock minimo: "))
    precio = float(input("Precio unitario: "))

    productos[codigo] = [tipo, descripcion, stock_actual, stock_actual, precio]

    codigo = input("Ingrese el codigo de producto (ingrese -1 para terminar): ")
print("=====================================")
print("CONSULTAS")
print("=====================================")

#A: Determinar si es posible vender una unidad del producto con código 124
print("=====================================")
print("¿se puede vender una unidad del producto código 124?")
print("=====================================")

if "124" in productos:
    stock_actual = productos["124"][2]
    if stock_actual > 0:
        print(" Sí, hay stock disponible")
    else: 
        print(" No, no hay stock disponible")
else:
    print(" No existe ese producto")

#B: codigo y descripcion de productos por debajo del stock minimo 
print("=====================================")
print("Productos por debajo del stock mínimo")
print("=====================================")

encontrados = False 
for codigo in productos:
    stock_actual = productos[codigo][2]
    stock_minimo = productos[codigo][3]
    descripcion = productos[codigo][1]

    if stock_actual < stock_minimo:
        print("Codigo: ", codigo, "- Descripción: ", descripcion)
        encontrados = True 
    
if not encontrados:
    print(" No hay productos por debajo del stock mínimo")
    

#C: cantidad de productos lácteos
print("=====================================")
print("Cantidad de productos lácteos")
print("=====================================")

cantidad_lacteos = 0
for codigo in productos:
    tipo = productos[codigo][0]
    if tipo == "lacteo"
    cantidad_lacteos +=1

print("Hay: ", cantidad_lacteos, "productos lácteos")

#D: producto de almacen con menor stock actual 
print("=====================================")
print("Productos de almacén con menor stock")
print("=====================================")

menor_stock = None 
codigo_menor = None 

for codigo in productos: 
    tipo = productos[codigo][0]
    stock_actual = productos[codigo][2]

    if tipo == 'almacen':
        if menor_stock == None or stock_actual < menor_stock:
            menor_stock = stock_actual
            codigo_menor = codigo

if codigo_menor != None:
    descripcion = productos[codigo_menor][1]
    print('Código: ', codigo_menor, '- Descripción:', descripcion, 'Stock:', menor_stock)
else:
    print("No hay productos de almacén")

#E: Descripcion del producto con codigo 3148
print("=====================================")
print("Descripción del producto código 3148")
print("=====================================")

if "3148" in productos: 
    descripcion = productos["3148"][1]
    print(descripcion)
else: 
    print("No existe ese producto")

#F: tipo de producto con menor cantidad de unidades disponibles
print("=====================================")
print("Tipo de producto con menor cantidad de unidades")
print("=====================================")

#acumul el stock en diccionario
stock_tipo = {}

for codigo in productos:
    tipo = productos[codigo][0]
    stock_actual = productos[codigo][2]

    if tipo in stock_tipo:
        stock_tipo[tipo] += stock_actual
    else:
        stock_tipo[tipo] = stock_actual
    

#busca el tipo con menor stock
tipo_menor = None 
stock_menor = None

for tipo in stock_tipo:
    if stock_menor == None or stock_tipo[tipo] < stock_menor:
        stock_menor = stock_tipo[tipo]
        tipo_menor = tipo
    
if tipo_menor != None:
    print(tipo_menor," con ", stock_menor, " unidades totales")
else:
    print("No hay productos cargados")

#G: procesar un pedido
print("=====================================")
print("Prosesar pedido \n Ingrese productos a comprar (código vacío para terminar)")
print("=====================================")

pedido = []
codigo = input("Código: ")

while codigo != "":
    pedido.append(codigo)
    codigo = input("Código: ")

#procesar el pedido
monto_total = 0 
productos_vendidos = []

for codigo in pedido:
    if codigo in productos:
        stock_actual = productos[codigo][2]
        precio = productos[codigo][4]
        descripcion = productos[codigo][1]
    
        if stock_actual > 0:
            monto_total += precio
            productos_vendidos.append(codigo) 

            productos[codigo][2] -= 1
            print(f"✓ Vendido: {descripcion} - ${precio}")
        else: 
            print(f"   ✗ Sin stock: {descripcion}")
    else:
        print(f"✗ Código {codigo} no existe")

print("Montro total: $", monto_total)
print("Productos vendidos: ", productos_vendidos)

