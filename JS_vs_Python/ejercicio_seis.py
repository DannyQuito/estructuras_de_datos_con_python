#Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
a = int(input("a: "))
b = int(input("b: "))

# Intercambio pythónico (una sola línea)
a, b = b, a

print(f"a = {a}, b = {b}")