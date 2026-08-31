#Escribir una función calcular_iva(precio) que reciba un precio y 
# retorne el IVA (15%). Usarla desde el programa principal.
# def calcular_iva(precio):
#     return precio * 0.15

# # --- Programa principal ---
# precio = float(input("Precio: $"))
# iva = calcular_iva(precio)
# print(f"IVA de ${precio}: ${iva:.2f}")

#Amplíala: define calcular_total(precio) que retorne precio + IVA usando la función anterior.
def calcular_iva(precio):
    return precio * 0.15

def calcular_total(precio):
    iva = calcular_iva(precio) 
    return precio + iva

precio_producto = float(input("Precio del producto: $"))

iva_final = calcular_iva(precio_producto)
total_final = calcular_total(precio_producto)

# Mostramos todos los resultados
print(f"\nSubtotal: ${precio_producto:.2f}")
print(f"IVA (15%): ${iva_final:.2f}")
print(f"Total:     ${total_final:.2f}")
