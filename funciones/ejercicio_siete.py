#Un año es bisiesto si es divisible entre 4 y no entre 100, O si es divisible entre 400.
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False

# O en una línea:
def es_bisiesto_corta(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

# Pruebas
for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {es_bisiesto(y)}")