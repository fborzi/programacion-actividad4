def cargar_productos():
    productos = {}

    codigo = int(input("Ingrese el código del producto (-1 para terminar): "))

    while codigo != -1:
        tipo = input("Tipo de producto: ")
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

        codigo = int(input("Ingrese el código del producto (-1 para terminar): "))

    return productos


def puede_vender(productos, codigo):
    if codigo in productos and productos[codigo]["stock"] > 0:
        print(f"Se puede vender una unidad del producto {codigo}.")
    else:
        print(f"No se puede vender el producto {codigo}.")


def productos_bajo_stock(productos):
    print("Productos por debajo del stock mínimo:")
    for cod, datos in productos.items():
        if datos["stock"] < datos["stock_min"]:
            print(f"Código: {cod} - {datos['descripcion']}")


def contar_lacteos(productos):
    cantidad = sum(1 for datos in productos.values() if datos["tipo"].lower() == "lácteo")
    print(f"El supermercado comercializa {cantidad} productos lácteos.")


def almacen_menor_stock(productos):
    min_stock = None
    producto_min = None
    for cod, datos in productos.items():
        if datos["tipo"].lower() == "almacén":
            if min_stock is None or datos["stock"] < min_stock:
                min_stock = datos["stock"]
                producto_min = (cod, datos["descripcion"])
    if producto_min:
        print(f"Producto de almacén con menor stock: {producto_min}")
    else:
        print("No hay productos de almacén.")


def descripcion_por_codigo(productos, codigo):
    if codigo in productos:
        print(f"Descripción del producto {codigo}: {productos[codigo]['descripcion']}")
    else:
        print(f"No existe producto con código {codigo}.")


def tipo_menor_stock_total(productos):
    tipos = {}
    for datos in productos.values():
        tipo = datos["tipo"]
        tipos[tipo] = tipos.get(tipo, 0) + datos["stock"]
    tipo_min = min(tipos, key=tipos.get)
    print(f"Tipo con menor cantidad total en stock: {tipo_min}")


def procesar_pedido(productos, pedido):
    total = 0
    vendidos = []

    for codigo in pedido:
        if codigo in productos and productos[codigo]["stock"] > 0:
            productos[codigo]["stock"] -= 1
            total += productos[codigo]["precio"]
            vendidos.append(codigo)

    print(f"Total a pagar: ${total:.2f}")
    print(f"Productos efectivamente vendidos: {vendidos}")


productos = cargar_productos()

puede_vender(productos, 124)
productos_bajo_stock(productos)
contar_lacteos(productos)
almacen_menor_stock(productos)
descripcion_por_codigo(productos, 3148)
tipo_menor_stock_total(productos)

pedido = [124, 200, 300, 124]
procesar_pedido(productos, pedido)
