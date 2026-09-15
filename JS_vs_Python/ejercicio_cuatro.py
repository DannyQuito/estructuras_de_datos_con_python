#Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
celsius = float(input("Temperatura en °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f} °F")