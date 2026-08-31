#Leer una cantidad total de segundos y mostrarla como hh:mm:ss. Ejemplo: 3725 segundos → 01:02:05.
# total = int(input("Segundos totales: "))

# horas = total // 3600
# resto = total % 3600
# minutos = resto // 60
# segundos = resto % 60

# print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

#Al revés: leer hh:mm:ss y convertir a segundos totales. Tendrás que usar split(":").
# Pedimos el tiempo en formato de texto hh:mm:ss
tiempo_texto = input("Ingresa el tiempo en formato hh:mm:ss: ")

partes = tiempo_texto.split(":")

horas = int(partes[0])
minutos = int(partes[1])
segundos = int(partes[2])

segundos_totales = (horas * 3600) + (minutos * 60) + segundos

print(f"Los segundos totales son: {segundos_totales}")

