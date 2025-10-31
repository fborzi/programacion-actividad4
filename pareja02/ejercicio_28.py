"""
EJERCICIO 28: Sistema de gestión de productos de supermercado
Gestionar productos con código, tipo, descripción, stock, stock mínimo y precio.
"""

print("Sistema de Gestión de Productos - Supermercado COTO")
print("="*60)

# Diccionario de productos (código: [tipo, descripción, stock, stock_min, precio])
productos = {
    124: ["lácteo", "Leche entera 1L", 50, 20, 250.50],
    125: ["lácteo", "Yogur natural", 30, 15, 180.00],
    200: ["almacén", "Arroz 1kg", 100, 30, 320.00],
    201: ["almacén", "Fideos 500g", 5, 25, 150.00],
    300: ["verdulería", "Tomate por kg", 80, 20, 450.00],
    400: ["limpieza", "Detergente 500ml", 40, 15, 280.00],
    500: ["carnicería", "Carne molida kg", 25, 10, 1500.00],
    3148: ["otros", "Pilas AA pack x4", 60, 20, 420.00],
}

print("\nProductos cargados en el sistema:")
for codigo, datos in productos.items():
    tipo, desc, stock, stock_min, precio = datos
    print(f"  [{codigo}] {desc} - Stock: {stock} - ${precio:.2f}")

print("\n" + "="*60)

# a) Determinar si es posible vender una unidad del producto 124
print("\na) ¿Es posible vender una unidad del producto 124?")
codigo = 124
if codigo in productos and productos[codigo][2] > 0:
    print(f"   SÍ, hay {productos[codigo][2]} unidades disponibles")
else:
    print("   NO, no hay stock disponible")

# b) Productos por debajo del stock mínimo
print("\nb) Productos por debajo del stock mínimo:")
for codigo, datos in productos.items():
    tipo, desc, stock, stock_min, precio = datos
    if stock < stock_min:
        print(f"   Código {codigo}: {desc} (Stock: {stock}, Mínimo: {stock_min})")

# c) Cantidad de productos lácteos
print("\nc) Cantidad de productos lácteos:")
lacteos = sum(1 for datos in productos.values() if datos[0] == "lácteo")
print(f"   {lacteos} productos lácteos")

# d) Producto de almacén con menor stock
print("\nd) Producto de almacén con menor stock:")
productos_almacen = {cod: datos for cod, datos in productos.items() if datos[0] == "almacén"}
if productos_almacen:
    codigo_min = min(productos_almacen.keys(), key=lambda c: productos_almacen[c][2])
    print(f"   Código {codigo_min}: {productos[codigo_min][1]}")
    print(f"   Stock actual: {productos[codigo_min][2]} unidades")

# e) Descripción del producto con código 3148
print("\ne) Descripción del producto con código 3148:")
codigo = 3148
if codigo in productos:
    print(f"   {productos[codigo][1]}")
else:
    print("   Producto no encontrado")

# f) Tipo de producto con menor cantidad de unidades disponibles
print("\nf) Tipo de producto con menor cantidad de unidades:")
stock_por_tipo = {}
for datos in productos.values():
    tipo = datos[0]
    stock = datos[2]
    if tipo in stock_por_tipo:
        stock_por_tipo[tipo] += stock
    else:
        stock_por_tipo[tipo] = stock

tipo_min = min(stock_por_tipo.keys(), key=lambda t: stock_por_tipo[t])
print(f"   Tipo: {tipo_min}")
print(f"   Total de unidades: {stock_por_tipo[tipo_min]}")

# g) Procesar un pedido
print("\n" + "="*60)
print("g) Procesar pedido:")
pedido = [124, 200, 201, 999]  # 999 no existe
print(f"   Pedido: {pedido}")

productos_vendidos = []
monto_total = 0

for codigo in pedido:
    if codigo in productos:
        tipo, desc, stock, stock_min, precio = productos[codigo]
        if stock > 0:
            # Vender una unidad
            productos[codigo][2] -= 1
            productos_vendidos.append(codigo)
            monto_total += precio
            print(f"   ✓ Vendido: {desc} - ${precio:.2f}")
        else:
            print(f"   ✗ Sin stock: {desc}")
    else:
        print(f"   ✗ Producto {codigo} no existe")

print(f"\n   Productos vendidos: {productos_vendidos}")
print(f"   Monto total: ${monto_total:.2f}")
