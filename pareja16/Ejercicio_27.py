
productos = {}

cod = int(input("Codigo: "))
while cod != -1:
    tipo = input("Tipo: ")
    descripcion = input("Descripcion: ")
    stock_actual = int(input("Stock actual: "))
    stock_minimo = int(input("Stock minimo: "))
    precio = float(input("Precio unitario: "))

    productos[cod] = {
        "tipo": tipo,
        "descripcion": descripcion,
        "stock": stock_actual,
        "minimo": stock_minimo,
        "precio": precio
    }

    cod = int(input("Codigo: "))

if 124 in productos and productos[124]["stock"] > 0:
    print("Se puede vender el producto 124")
else:
    print("NO se puede vender el producto 124")

print("Productos por debajo del stock minimo:")
for cod in productos:
    if productos[cod]["stock"] < productos[cod]["minimo"]:
        print(cod, productos[cod]["descripcion"])

lacteos = sum(1 for cod in productos if productos[cod]["tipo"] == "lácteo")
print("Cantidad de productos lácteos:", lacteos)

producto_menor_stock = None
menor = None
for cod in productos:
    if productos[cod]["tipo"] == "almacén":
        if menor is None or productos[cod]["stock"] < menor:
            menor = productos[cod]["stock"]
            producto_menor_stock = cod

print("Producto de almacén con menor stock:", producto_menor_stock)

if 3148 in productos:
    print("Descripcion del 3148:", productos[3148]["descripcion"])
else:
    print("No existe producto con codigo 3148")

unidades_por_tipo = {}
for cod in productos:
    tipo = productos[cod]["tipo"]
    unidades_por_tipo[tipo] = unidades_por_tipo.get(tipo, 0) + productos[cod]["stock"]

tipo_menor = min(unidades_por_tipo, key=unidades_por_tipo.get)
print("Tipo de producto con menor cantidad de unidades:", tipo_menor)

pedido = [124, 124, 3148, 5000]
total = 0
vendidos = []

for codigo in pedido:
    if codigo in productos and productos[codigo]["stock"] > 0:
        total += productos[codigo]["precio"]
        productos[codigo]["stock"] -= 1
        vendidos.append(codigo)

print("Monto total por el pedido:", total)
print("Productos vendidos:", vendidos)

