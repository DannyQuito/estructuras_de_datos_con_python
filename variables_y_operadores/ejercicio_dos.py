#Leer un número entero y determinar si es par o impar.
# num = int(input("Ingresa un número: "))

# # Ternario: expresión que devuelve un valor u otro según la condición
# resultado = "par" if num % 2 == 0 else "impar"

# print(f"{num} es {resultado}")

#Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.
num = int(input("Ingresa un número: "))
resultado = "par" if num % 2 == 0 else "impar"
print(f"{num} es {resultado}")

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} es múltiplo de ambos (de 3 y de 5).")
elif num % 3 == 0:
    print(f"{num} es múltiplo de 3.")
elif num % 5 == 0:
    print(f"{num} es múltiplo de 5.")
else:
    print(f"{num} no es múltiplo ni de 3 ni de 5.")
