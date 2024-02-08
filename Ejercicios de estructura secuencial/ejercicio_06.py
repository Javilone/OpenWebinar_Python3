import os
from math import sqrt


os.system("clear")

# 13 - Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, 
# ¿Cómo se puede calcular?
num1 = float(input("Introduce un número: "))
raizcuadrada = round(sqrt(num1),4)
def raiz_cubica(numero):
    return round(numero**(1. / 3.),2)
print(f""" 
      La raiz cuadrada de {num1} es {raizcuadrada}.
      La raiz cúbica de {num1} es {raiz_cubica(num1)}.""")

print("\n")
# 14 - Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
# Ejemplo, si se introduce 23 que muestre 32.
num2 = str(input("Introduce un número entero de dos cifras: "))
num3 = num2[0]
num4 = num2[1]
print(f"El número dado al revés es: {num4}{num3}")

print("\n")
# 15 - Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo 
# que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
# Igual al ejercicio anterior
varA = int(input("Introduce un numero entero para el valor A: "))
varB = int(input("Introduce otro valor numérico para el valor B: "))
varC = varA
varA = varB
varB = varC
print(f"Ahora tu valor A equivale {varA} y tu valor B equivale a {varB}")