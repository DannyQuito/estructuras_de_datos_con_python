#Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: 
# IMC = peso / estatura². Muestra el IMC con 2 decimales.
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")