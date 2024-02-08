import os

os.system("clear")

# 1 - Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
varA = float(input("Escribe un primer valor numérico: "))
varB = float(input("Escribe el segundo valor numérico: "))
if varA > varB:
    print(f"El primer valor ({varA}) es mayor que el segundo valor ({varB})")
else:
    print("El primer valor no es mayor que el segundo.")


# 2 - Algoritmo que pida un número y diga si es positivo, negativo o 0.
print("\n")
varC = float(input("Escribe un valor numérico: "))
if varC < 0:
    print(f"El valor que pusiste ({varC}) es un número negativo.")
elif varC == 0:
    print(f"EL valor que escribiste ({varC}) es igual a 0.")
else:
    print(f"El valor que escribiste es un número positivo ({varC})")
    

# 3 - Escribe un programa que lea un número e indique si es par o impar.
print("\n")
varD = float(input("Escribe un valor numérico: "))
if varD % 2 == 0:
    print("El valor es un número PAR.")
else:
    print("El valor es un número IMPAR")