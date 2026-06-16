# Registra una venta, aplica descuento a clientes frecuentes y muestra resumen

# Entrada de datos
nombre_vendedor = input("Nombre del vendedor: ")
clave_producto = input("Clave del producto: ")

# Validar cantidad (entero positivo)
while True:
    try:
        cantidad = int(input("Cantidad vendida (entero positivo): "))
        if cantidad > 0:
            break
        print("Error: debe ser un entero positivo.")
    except ValueError:
        print("Error: ingrese un número entero.")

# Validar precio unitario (float positivo)
while True:
    try:
        precio = float(input("Precio unitario (positivo): "))
        if precio > 0:
            break
        print("Error: el precio debe ser positivo.")
    except ValueError:
        print("Error: ingrese un número válido.")

# Validar tipo de cliente
while True:
    cliente = input("Tipo de cliente ('nuevo' o 'frecuente'): ").lower()
    if cliente in ['nuevo', 'frecuente']:
        break
    print("Error: escriba 'nuevo' o 'frecuente'.")

# Cálculos
subtotal = cantidad * precio
descuento = subtotal * 0.10 if cliente == 'frecuente' else 0
total = subtotal - descuento

# Mostrar resumen
print("\n--- RESUMEN DE VENTA ---")
print(f"Vendedor: {nombre_vendedor}")
print(f"Clave del producto: {clave_producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Tipo de cliente: {cliente}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
