#Un producto vale $12. Si compras 10 o más te dan 15% de descuento, 
# si compras entre 5 y 9 te dan 5%. Calcula el total.
PRECIO = 12
cant = int(input("Cantidad: "))

# Determinar el descuento
if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")