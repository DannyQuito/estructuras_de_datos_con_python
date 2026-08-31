#Leer la base y la altura de un rectángulo y mostrar su área y su perímetro. 
# Recuerda: área = base × altura, perímetro = 2 × (base + altura).
# base = float(input("Base: "))
# altura = float(input("Altura: "))

# area = base * altura                # PROCESO 1
# perimetro = 2 * (base + altura)     # PROCESO 2

# print(f"Área: {area:.2f}")
# print(f"Perímetro: {perimetro:.2f}")

#Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r). Usa import math y math.pi.
import math

print("--- CÁLCULOS DEL RECTÁNGULO ---")
base = float(input("Base: "))
altura = float(input("Altura: "))

area_rectangulo = base * altura
perimetro_rectangulo = 2 * (base + altura)

print(f"Área del rectángulo: {area_rectangulo:.2f}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo:.2f}\n")

print("--- CÁLCULOS DEL CÍRCULO ---")
radio = float(input("Radio del círculo: "))

area_circulo = math.pi * (radio ** 2)  
perimetro_circulo = 2 * math.pi * radio

print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")
