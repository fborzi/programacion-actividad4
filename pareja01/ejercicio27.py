# Se leen los datos de los productos que comercializa el supermercado 'Coto'. Para cada producto se lee: el código del producto, el tipo de producto (“lácteo”, “almacén”, “verdulería”, “limpieza”, “carnicería”, “otros”), la descripción, el stock actual, el stock mínimo y el precio unitario. La lectura de datos finaliza cuando se ingresa el código de producto '-1'. Se pide almacenar los datos de los productos en una estructura adecuada para resolver de la mejor manera los siguientes puntos:
# Determinar si es posible vender una unidad del producto con código 124.
# Código y descripción de los productos que están por debajo del stock mínimo.
# Cantidad de productos lácteos que comercializa el supermercado.
# El producto de almacén que tiene menor stock actual.
# La descripción del producto cuyo código es 3148 (puede no existir ese producto).
# El tipo de producto con menor cantidad de unidades disponibles para la venta.
# Un pedido puede representarse como una lista que contiene los códigos de los productos a comprar. Dado un pedido, calcular el monto total a pagar tras la compra de dichos productos y generar otra lista con los códigos de los productos que pudieron efectivamente venderse (ya que podría no haber stock de un producto que el cliente quería comprar). En el proceso, se deberá reducir el stock de cada producto efectivamente vendido.

# Carga de los productos
productos = {}

print("Ingrese los datos de los productos del supermercado COTO")
while True:
    codigo = int(input("\nCódigo del producto (-1 para terminar): "))
    if codigo == -1:
        break
    
    tipo = input("Tipo (lácteo, almacén, verdulería, limpieza, carnicería, otros): ").lower()
    descripcion = input("Descripción: ")
    stock = int(input("Stock actual: "))
    stock_min = int(input("Stock mínimo: "))
    precio = float(input("Precio unitario: "))

    productos[codigo] = {
        "tipo": tipo,
        "descripcion": descripcion,
        "stock": stock,
        "stock_min": stock_min,
        "precio": precio
    }


print("\nRESULTADOS")

# Determinar si es posible vender una unidad del producto 124
if 124 in productos and productos[124]["stock"] > 0:
    print("Es posible vender una unidad del producto 124.")
else:
    print("No es posible vender ese producto o no existe.")

# Productos debajo del stock mínimo
print("\nProductos debajo del stock mínimo:")
for codigo, datos in productos.items():
    if datos["stock"] < datos["stock_min"]:
        print(f"Código: {codigo} - {datos['descripcion']}")

#Cantidad de productos lácteos
cant_lacteos = sum(1 for datos in productos.values() if datos["tipo"] == "lácteo")
print(f"\nCantidad de productos lácteos: {cant_lacteos}")

#Producto de almacén con menor stock
almacen = [ (codigo, datos) for codigo, datos in productos.items() if datos["tipo"] == "almacén" ]
if almacen:
    cod_min_almacen, prod_min_almacen = min(almacen, key=lambda x: x[1]["stock"])
    print(f"\nProducto de almacén con menor stock: {cod_min_almacen} - {prod_min_almacen['descripcion']}")
else:
    print("\nNo hay productos de almacén.")

#Descripción del producto 3148
if 3148 in productos:
    print(f"\nDescripción del producto 3148: {productos[3148]['descripcion']}")
else:
    print("\nEl producto con código 3148 NO existe.")

#Tipo de producto con menor cantidad de unidades disponibles
unidades_por_tipo = {}
for datos in productos.values():
    tipo = datos["tipo"]
    unidades_por_tipo[tipo] = unidades_por_tipo.get(tipo, 0) + datos["stock"]

tipo_menos_unidades = min(unidades_por_tipo, key=unidades_por_tipo.get)
print(f"\nTipo con menor cantidad de unidades disponibles: {tipo_menos_unidades}")

#Procesar un pedido
pedido = []
print("\nIngrese los códigos del pedido (0 para terminar):")
while True:
    c = int(input())
    if c == 0:
        break
    pedido.append(c)

total_pagar = 0.0
vendidos = []

for cod in pedido:
    if cod in productos and productos[cod]["stock"] > 0:
        total_pagar += productos[cod]["precio"]
        productos[cod]["stock"] -= 1
        vendidos.append(cod)

print(f"\nMonto total a pagar: ${total_pagar:.2f}")
print("Productos efectivamente vendidos:", vendidos)
