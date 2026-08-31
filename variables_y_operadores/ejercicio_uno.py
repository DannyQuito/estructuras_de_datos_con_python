#Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. El IVA en Ecuador es 15%.
# IVA = 0.15                              # constante en MAYÚSCULA

# precio = float(input("Precio sin IVA: $"))
# iva = precio * IVA
# total = precio + iva

# print(f"IVA:   ${iva:.2f}")
# print(f"Total: ${total:.2f}")

#Añadir un descuento del 10% que se aplique antes del IVA. Muestra los tres valores: descuento, IVA, total.
IVA = 0.15
DESCUENTO_PORCENTAJE = 0.10 
precio = float(input("Precio sin IVA: $"))

descuento = precio * DESCUENTO_PORCENTAJE
precio_con_descuento = precio - descuento
iva = precio_con_descuento * IVA
total = precio_con_descuento + iva

print(f"Descuento (10%): ${descuento:.2f}")
print(f"IVA (15%):       ${iva:.2f}")
print(f"Total a pagar:   ${total:.2f}")
