#Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")