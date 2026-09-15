#Genera un número secreto entre 1 y 100. El usuario intenta adivinar. 
#En cada intento le dices si es «mayor» o «menor». Cuenta cuántos intentos usó.
import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")