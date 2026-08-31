#Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
# def saludar():
#     nombre = input("Nombre: ")
#     print(f"¡Hola, {nombre}!")

# def despedir():
#     nombre = input("Nombre: ")
#     print(f"¡Adiós, {nombre}!")

# def mostrar_menu():
#     print("\n--- MENÚ ---")
#     print("1. Saludar")
#     print("2. Despedir")
#     print("3. Salir")

# # Programa principal
# while True:
#     mostrar_menu()
#     opcion = input("Opción: ")
#     if opcion == "1":
#         saludar()
#     elif opcion == "2":
#         despedir()
#     elif opcion == "3":
#         print("Adiós")
#         break
#     else:
#         print("Opción inválida")

#Añade una función calcular() que pida dos números y muestre suma,
#resta, multiplicación y división. Nueva opción del menú.
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

# --- Nueva Función Solicitada ---
def calcular():
    print("\n--- Operaciones Matemáticas ---")
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    
    print(f"Suma:           {suma:.2f}")
    print(f"Resta:          {resta:.2f}")
    print(f"Multiplicación: {multiplicacion:.2f}")
    
    # Validación crítica: Evitar la división para cero
    if n2 != 0:
        division = n1 / n2
        print(f"División:       {division:.2f}")
    else:
        print("División:       Error (No se puede dividir para cero)")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Calcular operaciones básicas")  # Nueva opción añadida
    print("4. Salir")                         # Cambió de la opción 3 a la 4

# --- Programa principal ---
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        calcular()  # Invocamos la nueva función
    elif opcion == "4":
        print("Fin del programa. ¡Adiós!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")


