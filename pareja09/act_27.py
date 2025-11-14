productos = {}

while True:
    codigo = int(input("Ingrese el código del producto (-1 para terminar): "))
    if codigo == -1:
        break

    tipo = input("Ingrese el tipo de producto (lácteo, almacén, verdulería, limpieza, carnicería, otros): ").lower()
    descripcion = input("Ingrese la descripción del producto: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo: "))
    precio = float(input("Ingrese el precio unitario: "))

    productos[codigo] = {
        "tipo": tipo,
        "descripcion": descripcion,
        "stock_actual": stock_actual,
        "stock_minimo": stock_minimo,
        "precio": precio
    }

print("\n=== INFORMES ===")

if 124 in productos and productos[124]["stock_actual"] > 0:
    print("Se puede vender una unidad del producto con código 124.")
elif 124 in productos:
    print("El producto con código 124 no tiene stock disponible.")
else:
    print("No existe producto con código 124.")

print("\nProductos por debajo del stock mínimo:")
for codigo, datos in productos.items():
    if datos["stock_actual"] < datos["stock_minimo"]:
        print(f" - Código {codigo}: {datos['descripcion']}")

cantidad_lacteos = sum(1 for datos in productos.values() if datos["tipo"] == "lácteo")
print(f"\nCantidad de productos lácteos: {cantidad_lacteos}")

menor_stock = None
codigo_menor = None
for codigo, datos in productos.items():
    if datos["tipo"] == "almacén":
        if menor_stock is None or datos["stock_actual"] < menor_stock:
            menor_stock = datos["stock_actual"]
            codigo_menor = codigo

if codigo_menor is not None:
    print(f"\nEl producto de almacén con menor stock es '{productos[codigo_menor]['descripcion']}' (Código {codigo_menor})")
else:
    print("\nNo hay productos de almacén cargados.")

if 3148 in productos:
    print(f"\nEl producto con código 3148 es: {productos[3148]['descripcion']}")
else:
    print("\nNo existe un producto con código 3148.")

tipos_stock = {}
for datos in productos.values():
    tipo = datos["tipo"]
    tipos_stock[tipo] = tipos_stock.get(tipo, 0) + datos["stock_actual"]

if tipos_stock:
    tipo_menor = min(tipos_stock, key=tipos_stock.get)
    print(f"\nEl tipo de producto con menor cantidad total de unidades es: {tipo_menor}")
else:
    print("\nNo hay productos cargados.")

pedido = []
print("\n=== REGISTRO DE PEDIDO ===")
while True:
    codigo = int(input("Ingrese código de producto para el pedido (-1 para finalizar): "))
    if codigo == -1:
        break
    pedido.append(codigo)

total = 0
vendidos = []

for codigo in pedido:
    if codigo in productos and productos[codigo]["stock_actual"] > 0:
        total += productos[codigo]["precio"]
        productos[codigo]["stock_actual"] -= 1
        vendidos.append(codigo)
    elif codigo not in productos:
        print(f"Producto con código {codigo} no existe.")
    else:
        print(f"Producto con código {codigo} sin stock.")

print(f"\nMonto total a pagar: ${total:.2f}")
print(f"Productos efectivamente vendidos: {vendidos}")