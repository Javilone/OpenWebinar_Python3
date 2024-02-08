import os

os.system("clear")

# 12 - Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, 
# pero no si es divisible por 100, excepto que también sea divisible por 400.

año = int(input("Introduce un año para saber si es bisiesto o no: "))

if (año % 4 == 0):
    print("El año es bisiesto.")
else:
    print("El año NO es bisiesto.")
    
    
# 13 - Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = int(input("Introduce el número de un día del mes: "))
mes = int(input("Introduce el número correspondiente a un mes: "))
año = int(input("Introduce un año: "))
if (dia > 0 and dia < 32) and (mes > 0 and mes < 13):
    print(f"La fecha {dia}/{mes}/{año} es una fecha válida.")
else:
    print("La fecha no es válida.")
    