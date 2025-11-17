# Sistema de gestión de productos del supermercado

# Diccionario de productos (código: datos)
productos = {}

print("\nIngrese los datos de los productos.")
print("Ingrese código '-1' para finalizar.\n")

# Cargar datos de productos
codigo = 0
while codigo != -1:
    codigo = int(input("Código del producto: "))
    
    if codigo != -1:
        tipo = input("Tipo (lácteo/almacén/verdulería/limpieza/carnicería/otros): ")
        descripcion = input("Descripción: ")
        stock_actual = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio_unitario = float(input("Precio unitario: "))
        
        productos[codigo] = {
            'tipo': tipo,
            'descripcion': descripcion,
            'stock_actual': stock_actual,
            'stock_minimo': stock_minimo,
            'precio_unitario': precio_unitario
        }
        print()

print("\n" + "=" * 50)
print("CONSULTAS")
print("=" * 50)

# Determinar si es posible vender una unidad del producto 124
print("\na) ¿Es posible vender una unidad del producto 124?")
codigo_consulta = 124
if codigo_consulta in productos:
    if productos[codigo_consulta]['stock_actual'] > 0:
        print(f"SÍ es posible vender el producto {codigo_consulta}")
    else:
        print(f"NO es posible vender el producto {codigo_consulta} (sin stock)")
else:
    print(f"El producto {codigo_consulta} no existe")

# Productos por debajo del stock mínimo
print("\nb) Productos por debajo del stock mínimo:")
bajo_stock = [(cod, prod['descripcion']) for cod, prod in productos.items() 
              if prod['stock_actual'] < prod['stock_minimo']]
if bajo_stock:
    for codigo, descripcion in bajo_stock:
        print(f"  Código: {codigo}, Descripción: {descripcion}")
else:
    print("  No hay productos por debajo del stock mínimo")

# Cantidad de productos lácteos
print("\nc) Cantidad de productos lácteos:")
lacteos = sum(1 for prod in productos.values() if prod['tipo'] == 'lácteo')
print(f"  Total de productos lácteos: {lacteos}")

# Producto de almacén con menor stock
print("\nd) Producto de almacén con menor stock:")
almacen = {cod: prod for cod, prod in productos.items() if prod['tipo'] == 'almacén'}
if almacen:
    cod_menor = min(almacen.keys(), key=lambda c: almacen[c]['stock_actual'])
    print(f"  Código: {cod_menor}")
    print(f"  Descripción: {productos[cod_menor]['descripcion']}")
    print(f"  Stock: {productos[cod_menor]['stock_actual']}")
else:
    print("  No hay productos de almacén")

# Descripción del producto con código 3148
print("\ne) Descripción del producto 3148:")
if 3148 in productos:
    print(f"  {productos[3148]['descripcion']}")
else:
    print("  El producto con código 3148 no existe")

# Tipo de producto con menor cantidad de unidades disponibles
print("\nf) Tipo con menor cantidad de unidades disponibles:")
tipos_stock = {}
for prod in productos.values():
    tipo = prod['tipo']
    tipos_stock[tipo] = tipos_stock.get(tipo, 0) + prod['stock_actual']

if tipos_stock:
    tipo_menor = min(tipos_stock.keys(), key=lambda t: tipos_stock[t])
    print(f"  Tipo: {tipo_menor}")
    print(f"  Total de unidades: {tipos_stock[tipo_menor]}")

# Procesar un pedido
print("\ng) Procesar pedido:")
print("Ingrese códigos de productos (termine con -1):")
pedido = []
cod = 0
while cod != -1:
    cod = int(input("Código: "))
    if cod != -1:
        pedido.append(cod)

monto_total = 0
vendidos = []

for codigo in pedido:
    if codigo in productos and productos[codigo]['stock_actual'] > 0:
        monto_total += productos[codigo]['precio_unitario']
        productos[codigo]['stock_actual'] -= 1
        vendidos.append(codigo)

print(f"\nMonto total: ${monto_total:.2f}")
print(f"Productos vendidos: {vendidos}")