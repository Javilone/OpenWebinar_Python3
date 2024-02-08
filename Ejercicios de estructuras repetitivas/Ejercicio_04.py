import os

os.system("clear")


# 7 - Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
print("## Escribe un número para saber la tabla de multiplicar de dicho número: ")
numero = int(input("Introduce un número entero: "))

tabla = 10
multiplicador = 0
while tabla >= 0:
    print(f"{numero} * {multiplicador} = {numero * multiplicador}")
    multiplicador += 1
    tabla -= 1

