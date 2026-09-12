def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":
    precio_producto = 12.50
    cantidad_comprada = 3
    resultado_final = calcular_total(precio_producto, cantidad_comprada)
    print(f"El total de la compra es: ${resultado_final}")
