import os
from random import randint

os.system("clear")

# 3 - Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.

num = 0
entradas = 0

clave_bucle = True
while clave_bucle:
    introducir = int(input("Introduce los números enteros que quieres para saber la suma y la media de todos ellos. \nPara acabar, introduce el 0: "))

    if introducir != 0:
        num = num + introducir
        entradas += 1
    elif introducir == 0:
        print(f"La suma de todos los números es {num}. ")
        print(f"La media de los números que introdujiste es {num / entradas}.")
        clave_bucle = False


print("\n")
# 4 - Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
mayor = 0
menor = 0
igual = 0

clave = randint(1,6)
while clave > 0:
    entrada = int(input(f"Introduce {clave} números: "))
    clave -= 1
    
    if entrada > 0:
        mayor += 1
        continue
    elif entrada < 0:
        menor += 1
        continue
    elif entrada == 0:
        igual += 1
        continue
print(f"""
      Introdujiste: 
      {mayor} números mayor que 0.
      {menor} números menores que 0.
      {igual} números igual a 0.""")