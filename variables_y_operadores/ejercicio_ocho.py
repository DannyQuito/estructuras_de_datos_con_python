#Lee un número decimal y una cantidad de decimales, 
# y muéstralo redondeado. Ejemplo: 3.14159 con 2 decimales → 3.14.
num = float(input("Número: "))
dec = int(input("Decimales: "))

# La función round() redondea al entero más cercano
resultado = round(num, dec)
print(resultado)