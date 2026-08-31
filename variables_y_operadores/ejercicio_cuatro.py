#Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto, 
# mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
# monto = int(input("Monto: $"))
# resto = monto

# b20 = resto // 20; resto = resto % 20
# b10 = resto // 10; resto = resto % 10
# b5  = resto // 5;  resto = resto % 5
# b1  = resto // 1;  resto = resto % 1

# print(f"$20 × {b20}")
# print(f"$10 × {b10}")
# print(f"$5  × {b5}")
# print(f"$1  × {b1}")

#Añadir billete de $50 al inicio. Después probar con monedas de $0.25, $0.10, $0.05 y $0.01 (necesitas trabajar con centavos).
# Pedimos el monto. Ahora usamos float porque el usuario ingresará decimales (ej. 87.36)
monto = float(input("Monto en dólares (ej. 87.36): $"))

#round() no queden decimales
resto = round(monto * 100)

# --- BILLETES en centavos---
b50 = resto // 5000; resto %= 5000  
b20 = resto // 2000; resto %= 2000  
b10 = resto // 1000; resto %= 1000 
b5  = resto // 500;  resto %= 500  
b1  = resto // 100;  resto %= 100   

# --- MONEDAS (Expresadas en centavos) ---
m25 = resto // 25;   resto %= 25   
m10 = resto // 10;   resto %= 10   
m05 = resto // 5;    resto %= 5    
m01 = resto // 1;    resto %= 1   

print("\n--- Desglose de Billetes ---")
print(f"$50 × {b50}")
print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")

print("\n--- Desglose de Monedas ---")
print(f"$0.25 × {m25}")
print(f"$0.10 × {m10}")
print(f"$0.05 × {m05}")
print(f"$0.01 × {m01}")
