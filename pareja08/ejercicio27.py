'''Se leen los datos de los productos que comercializa el supermercado 'Coto'. Para cada producto se lee: el código del producto, el tipo de producto (“lácteo”, “almacén”, “verdulería”, “limpieza”, “carnicería”, “otros”), la descripción, el stock actual, el stock mínimo y el precio unitario. La lectura de datos finaliza cuando se ingresa el código de producto '-1'. Se pide almacenar los datos de los productos en una estructura adecuada para resolver de la mejor manera los siguientes puntos:
a. Determinar si es posible vender una unidad del producto con código 124.
b. Código y descripción de los productos que están por debajo del stock mínimo.
c. Cantidad de productos lácteos que comercializa el supermercado.
d. El producto de almacén que tiene menor stock actual.
e. La descripción del producto cuyo código es 3148 (puede no existir ese producto).
f. El tipo de producto con menor cantidad de unidades disponibles para la venta.
g. Un pedido puede representarse como una lista que contiene los códigos de los productos a comprar. Dado un pedido, calcular el monto total a pagar tras la compra de dichos productos y generar otra lista con los códigos de los productos que pudieron efectivamente venderse (ya que podría no haber stock de un producto que el cliente quería comprar). En el proceso, se deberá reducir el stock de cada producto efectivamente vendido.'''

from funciones import cargar_productos, resolver_consultas, procesar_pedido
def cargar_productos():
    productos = {}
    while True:
        codigo = int(input("Código de producto (-1 para terminar): "))
        if codigo == -1:
            break
        tipo = input("Tipo de producto: ").lower()
        descripcion = input("Descripción: ")
        stock_actual = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio_unitario = float(input("Precio unitario: "))
        productos[codigo] = {
            "tipo": tipo,
            "descripcion": descripcion,
            "stock_actual": stock_actual,
            "stock_minimo": stock_minimo,
            "precio_unitario": precio_unitario
        }
    return productos

def resolver_consultas(productos):
    # a. ¿Se puede vender el producto 124?
    print("\na. ¿Se puede vender el producto 124?")
    if 124 in productos and productos[124]["stock_actual"] > 0:
        print("  Sí, hay stock disponible.")
    else:
        print("  No, no hay stock disponible o el producto no existe.")

    # b. Productos por debajo del stock mínimo
    print("\nb. Productos por debajo del stock mínimo:")
    for codigo, datos in productos.items():
        if datos["stock_actual"] < datos["stock_minimo"]:
            print(f"  Código: {codigo} | Descripción: {datos['descripcion']}")

    # c. Cantidad de productos lácteos
    lacteos = sum(1 for datos in productos.values() if datos["tipo"] == "lácteo")
    print(f"\nc. Cantidad de productos lácteos: {lacteos}")

    # d. Producto de almacén con menor stock actual
    almacen = [(codigo, datos) for codigo, datos in productos.items() if datos["tipo"] == "almacén"]
    if almacen:
        menor = min(almacen, key=lambda x: x[1]["stock_actual"])
        print(f"\nd. Producto de almacén con menor stock: Código {menor[0]} | {menor[1]['descripcion']}")
    else:
        print("\nd. No hay productos de almacén registrados.")

    # e. Descripción del producto 3148
    print("\ne. Descripción del producto 3148:")
    if 3148 in productos:
        print(f"  {productos[3148]['descripcion']}")
    else:
        print("  No existe el producto con código 3148.")

    # f. Tipo con menor cantidad total de unidades disponibles
    tipo_unidades = {}
    for datos in productos.values():
        tipo = datos["tipo"]
        tipo_unidades[tipo] = tipo_unidades.get(tipo, 0) + datos["stock_actual"]
    if tipo_unidades:
        tipo_menor = min(tipo_unidades.items(), key=lambda x: x[1])
        print(f"\nf. Tipo con menor cantidad de unidades disponibles: {tipo_menor[0]} ({tipo_menor[1]} unidades)")
    else:
        print("\nf. No hay productos registrados.")

def procesar_pedido(productos, pedido):
    monto_total = 0
    vendidos = []
    for codigo in pedido:
        if codigo in productos and productos[codigo]["stock_actual"] > 0:
            monto_total += productos[codigo]["precio_unitario"]
            productos[codigo]["stock_actual"] -= 1
            vendidos.append(codigo)
    return monto_total, vendidos

productos = cargar_productos()
resolver_consultas(productos)

pedido = [124, 3148, 9999]  # ejemplo de pedido
monto, vendidos = procesar_pedido(productos, pedido)
print(f"\nMonto total a pagar: ${monto:.2f}")
print(f"Productos vendidos: {vendidos}")
