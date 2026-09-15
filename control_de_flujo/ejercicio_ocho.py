#Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
num = int(input("Número: "))
n = abs(num)                # trabajar con el positivo
digitos = 0

if n == 0:
    digitos = 1             # caso especial: el 0 tiene 1 dígito
else:
    while n > 0:
        digitos += 1
        n = n // 10         # quitamos el último dígito

print(f"{digitos} dígitos")