from numpy import mean
import os

# 4 - Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
os.system("clear")
num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero: "))

suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print(f"""
      {num1} + {num2} = {suma}
      {num1} - {num2} = {resta}
      {num1} / {num2} = {division}
      {num1} * {num2} = {multiplicacion}
      """)

# 5 - Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
# Recordar que la fórmula para la conversión es: C = (F-32)*5/9

print("## Convertidos de Farenheit a Celsius.")
temperatura = int(input("Introduce la temperatura que deseas convertir a grados Celsius: "))
celsius = int((temperatura-32)*(5/9))
print(f"La temperatura ({temperatura}) equivale a {celsius} grados Celsius")

# 6 - Calcular la media de tres números pedidos por teclado.
(print("\n## Calcular la media de 3 números."))
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
media = mean([num1, num2, num3])
print(media)