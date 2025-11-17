# Diccionario de productos predefinidos
# Clave: código del producto
# Valor: diccionario con tipo, descripción, stock actual, stock mínimo y precio
productos = {
    124: {"tipo": "lácteo", "descripcion": "Leche entera 1L", "stock_actual": 10, "stock_minimo": 5, "precio": 150.0},
    2001: {"tipo": "almacén", "descripcion": "Arroz 1kg", "stock_actual": 2, "stock_minimo": 5, "precio": 120.0},
    3148: {"tipo": "verdulería", "descripcion": "Lechuga", "stock_actual": 0, "stock_minimo": 3, "precio": 50.0},
    4023: {"tipo": "limpieza", "descripcion": "Detergente 1L", "stock_actual": 8, "stock_minimo": 4, "precio": 300.0},
    5000: {"tipo": "almacén", "descripcion": "Fideos 500g", "stock_actual": 1, "stock_minimo": 5, "precio": 80.0},
}

# 1️⃣ Determinar si es posible vender una unidad del producto con código 124
codigo_buscar = 124
if codigo_buscar in productos and productos[codigo_buscar]["stock_actual"] > 0:
    print(f"Se puede vender el producto {codigo_buscar}")
else:
    print(f"No se puede vender el producto {codigo_buscar}")

# 2️⃣ Código y descripción de productos por debajo del stock mínimo
print("\nProductos por debajo del stock mínimo:")
for cod, datos in productos.items():
    if datos["stock_actual"] < datos["stock_minimo"]:
        print(f"Código: {cod}, Descripción: {datos['descripcion']}")

# 3️⃣ Cantidad de productos lácteos
lacteos = sum(1 for p in productos.values() if p["tipo"] == "lácteo")
print(f"\nCantidad de productos lácteos: {lacteos}")

# 4️⃣ Producto de almacén con menor stock actual
productos_almacen = {cod: datos for cod, datos in productos.items() if datos["tipo"] == "almacén"}
if productos_almacen:
    cod_min_stock = min(productos_almacen, key=lambda c: productos_almacen[c]["stock_actual"])
    print(f"\nProducto de almacén con menor stock: Código {cod_min_stock}, Descripción {productos_almacen[cod_min_stock]['descripcion']}")

# 5️⃣ Descripción del producto con código 3148
codigo_buscar = 3148
if codigo_buscar in productos:
    print(f"\nProducto 3148: {productos[codigo_buscar]['descripcion']}")
else:
    print("\nNo existe el producto con código 3148")

# 6️⃣ Tipo de producto con menor cantidad de unidades disponibles
stock_por_tipo = {}
for datos in productos.values():
    stock_por_tipo[datos["tipo"]] = stock_por_tipo.get(datos["tipo"], 0) + datos["stock_actual"]

tipo_min_stock = min(stock_por_tipo, key=lambda t: stock_por_tipo[t])
print(f"\nTipo de producto con menor cantidad de unidades disponibles: {tipo_min_stock} ({stock_por_tipo[tipo_min_stock]} unidades)")

# 7️⃣ Procesar un pedido
pedido = [124, 3148, 2001, 5000]  # ejemplo de pedido
monto_total = 0
productos_vendidos = []

for cod in pedido:
    if cod in productos and productos[cod]["stock_actual"] > 0:
        monto_total += productos[cod]["precio"]
        productos_vendidos.append(cod)
        productos[cod]["stock_actual"] -= 1  # descontar stock
    else:
        print(f"Producto {cod} no se pudo vender (sin stock o no existe)")

print(f"\nMonto total a pagar: ${monto_total:.2f}")
print(f"Productos efectivamente vendidos: {productos_vendidos}")
