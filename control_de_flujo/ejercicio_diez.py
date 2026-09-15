#Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       # sale del while
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")