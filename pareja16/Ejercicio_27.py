# Programa: Gestión de productos del supermercado "Coto"

# Estructura: diccionario
# Clave: código del producto
# Valor: diccionario con sus datos

productos = {}

# --- CARGA DE DATOS ---
while True:
    codigo = int(input("Ingrese el código del producto (-1 para finalizar): "))
    if codigo == -1:
        break

    tipo = input("Ingrese el tipo de producto (lácteo / almacén / verdulería / limpieza / carnicería / otros): ").lower()
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

    print("Producto cargado correctamente.\n")

# --- 1. Determinar si es posible vender una unidad del producto con código 124 ---
codigo_buscar = 124
if codigo_buscar in productos:
    if productos[codigo_buscar]["stock_actual"] > 0:
        print(f"✅ Se puede vender una unidad del producto {codigo_buscar}.")
    else:
        print(f"❌ No hay stock del producto {codigo_buscar}.")
else:
    print(f"❌ No existe el producto con código {codigo_buscar}.")
print()

# --- 2. Código y descripción de los productos por debajo del stock mínimo ---
print("📦 Productos por debajo del stock mínimo:")
for codigo, datos in productos.items():
    if datos["stock_actual"] < datos["stock_minimo"]:
        print(f"- Código: {codigo} | {datos['descripcion']}")
print()

# --- 3. Cantidad de productos lácteos ---
lacteos = sum(1 for datos in productos.values() if datos["tipo"] == "lácteo")
print(f"🥛 Cantidad de productos lácteos: {lacteos}\n")

# --- 4. Producto de almacén con menor stock actual ---
almacenes = {codigo: datos for codigo, datos in productos.items() if datos["tipo"] == "almacén"}
if almacenes:
    menor_stock = min(almacenes, key=lambda c: almacenes[c]["stock_actual"])
    print(f"📉 Producto de almacén con menor stock: {menor_stock} ({almacenes[menor_stock]['descripcion']})")
else:
    print("No hay productos de tipo almacén.")
print()

# --- 5. Descripción del producto cuyo código es 3148 ---
codigo_3148 = 3148
if codigo_3148 in productos:
    print(f"🛒 Descripción del producto 3148: {productos[codigo_3148]['descripcion']}")
else:
    print("❌ No existe un producto con código 3148.")
print()

# --- 6. Tipo de producto con menor cantidad total de unidades disponibles ---
unidades_por_tipo = {}
for datos in productos.values():
    tipo = datos["tipo"]
    unidades_por_tipo[tipo] = unidades_por_tipo.get(tipo, 0) + datos["stock_actual"]

if unidades_por_tipo:
    tipo_menor = min(unidades_por_tipo, key=unidades_por_tipo.get)
    print(f"📊 Tipo de producto con menor cantidad de unidades: {tipo_menor}")
print()

# --- 7. Procesar un pedido ---
pedido = []
print("Ingrese los códigos de los productos del pedido (0 para finalizar):")
while True:
    cod_pedido = int(input("> "))
    if cod_pedido == 0:
        break
    pedido.append(cod_pedido)

total_pagar = 0
vendidos = []

for codigo in pedido:
    if codigo in productos and productos[codigo]["stock_actual"] > 0:
        total_pagar += productos[codigo]["precio"]
        productos[codigo]["stock_actual"] -= 1
        vendidos.append(codigo)

print(f"\n💰 Total a pagar: ${total_pagar:.2f}")
print(f"🧾 Productos efectivamente vendidos: {vendidos}")
