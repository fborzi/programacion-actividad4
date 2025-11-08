def leer_productos():
    """
    Lee los datos de los productos hasta que se ingrese el código '-1'
    Retorna un diccionario con todos los productos
    """
    productos = {}
    
    print("Ingrese los datos de los productos (código '-1' para finalizar):")
    codigo = input("\nCódigo del producto: ")
    
    while codigo != '-1':
        tipo = input("Tipo de producto (lácteo/almacén/verdulería/limpieza/carnicería/otros): ")
        descripcion = input("Descripción: ")
        stock_actual = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio = float(input("Precio unitario: "))
        
        productos[codigo] = {
            'tipo': tipo,
            'descripcion': descripcion,
            'stock_actual': stock_actual,
            'stock_minimo': stock_minimo,
            'precio': precio
        }
        
        codigo = input("\nCódigo del producto: ")
    
    return productos

def punto_A(productos, codigo_buscado="124"):
    """A. Determinar si es posible vender una unidad del producto con código 124"""
    if codigo_buscado in productos and productos[codigo_buscado]['stock_actual'] > 0:
        return f"Sí es posible vender una unidad del producto {codigo_buscado}"
    else:
        return f"No es posible vender una unidad del producto {codigo_buscado}"

def punto_B(productos):
    """B. Código y descripción de productos por debajo del stock mínimo"""
    productos_bajo_stock = []
    for codigo, datos in productos.items():
        if datos['stock_actual'] < datos['stock_minimo']:
            productos_bajo_stock.append((codigo, datos['descripcion']))
    return productos_bajo_stock

def punto_C(productos):
    """C. Cantidad de productos lácteos"""
    count = 0
    for datos in productos.values():
        if datos['tipo'].lower() == 'lácteo':
            count += 1
    return count

def punto_D(productos):
    """D. Producto de almacén con menor stock actual"""
    productos_almacen = {}
    for codigo, datos in productos.items():
        if datos['tipo'].lower() == 'almacén':
            productos_almacen[codigo] = datos
    
    if not productos_almacen:
        return None
    
    menor_stock = min(productos_almacen.items(), key=lambda x: x[1]['stock_actual'])
    return menor_stock[0], menor_stock[1]['descripcion'], menor_stock[1]['stock_actual']

def punto_E(productos, codigo_buscado="3148"):
    """E. Descripción del producto con código 3148"""
    if codigo_buscado in productos:
        return productos[codigo_buscado]['descripcion']
    else:
        return "Producto no encontrado"

def punto_F(productos):
    """F. Tipo de producto con menor cantidad de unidades disponibles"""
    stock_por_tipo = {}
    
    for datos in productos.values():
        tipo = datos['tipo']
        if tipo in stock_por_tipo:
            stock_por_tipo[tipo] += datos['stock_actual']
        else:
            stock_por_tipo[tipo] = datos['stock_actual']
    
    if not stock_por_tipo:
        return "No hay productos"
    
    tipo_menor_stock = min(stock_por_tipo.items(), key=lambda x: x[1])
    return tipo_menor_stock[0], tipo_menor_stock[1]

def punto_G(productos, pedido):
    """
    G. Procesar un pedido: calcular monto total y lista de productos vendidos
    Retorna: (monto_total, productos_vendidos, productos_sin_stock)
    """
    monto_total = 0
    productos_vendidos = []
    productos_sin_stock = []
    
    for codigo in pedido:
        if codigo in productos:
            producto = productos[codigo]
            if producto['stock_actual'] > 0:
                # Vender el producto
                monto_total += producto['precio']
                productos_vendidos.append(codigo)
                # Reducir stock
                productos[codigo]['stock_actual'] -= 1
            else:
                productos_sin_stock.append(codigo)
        else:
            productos_sin_stock.append(codigo)
    
    return monto_total, productos_vendidos, productos_sin_stock

def main():
    # Leer todos los productos
    productos = leer_productos()
    
    if not productos:
        print("No se ingresaron productos.")
        return
    
    print("\n" + "="*50)
    print("RESULTADOS:")
    print("="*50)
    
    # A. Vender producto 124
    print("\nA.", punto_A(productos))
    
    # B. Productos por debajo del stock mínimo
    productos_bajo_stock = punto_B(productos)
    print("\nB. Productos por debajo del stock mínimo:")
    if productos_bajo_stock:
        for codigo, descripcion in productos_bajo_stock:
            print(f"   - {codigo}: {descripcion}")
    else:
        print("   No hay productos por debajo del stock mínimo")
    
    # C. Cantidad de productos lácteos
    print(f"\nC. Cantidad de productos lácteos: {punto_C(productos)}")
    
    # D. Producto de almacén con menor stock
    resultado_D = punto_D(productos)
    print("\nD. Producto de almacén con menor stock:")
    if resultado_D:
        codigo, descripcion, stock = resultado_D
        print(f"   - Código: {codigo}, Descripción: {descripcion}, Stock: {stock}")
    else:
        print("   No hay productos de almacén")
    
    # E. Descripción del producto 3148
    print(f"\nE. Descripción del producto 3148: {punto_E(productos)}")
    
    # F. Tipo con menor stock total
    tipo, stock_total = punto_F(productos)
    print(f"\nF. Tipo con menor stock total: {tipo} (Stock total: {stock_total})")
    
    # G. Procesar un pedido de ejemplo
    print("\nG. Procesamiento de pedido:")
    pedido_ejemplo = ['124', '3148', '999']  # Códigos de ejemplo
    monto, vendidos, sin_stock = punto_G(productos, pedido_ejemplo)
    
    print(f"   Pedido: {pedido_ejemplo}")
    print(f"   Monto total: ${monto:.2f}")
    print(f"   Productos vendidos: {vendidos}")
    print(f"   Productos sin stock/no encontrados: {sin_stock}")

if __name__ == "__main__":
    main()