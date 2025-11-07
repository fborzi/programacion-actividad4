from funciones import cargar_productos, puede_vender, productos_bajo_stock, contar_lacteos, almacen_menor_stock, descripcion_por_codigo, tipo_menor_stock_total, procesar_pedido

productos = cargar_productos()

puede_vender(productos, 124)
productos_bajo_stock(productos)
contar_lacteos(productos)
almacen_menor_stock(productos)
descripcion_por_codigo(productos, 3148)
tipo_menor_stock_total(productos)

pedido = [124, 200, 300, 124]
procesar_pedido(productos, pedido)
