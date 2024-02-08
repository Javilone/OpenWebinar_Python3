import os

os.system("clear")


# 7 - Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y
# el exponente. Pueden ocurrir tres cosas:
#   El exponente sea positivo, sólo tienes que imprimir la potencia.
#   El exponente sea 0, el resultado es 1.
#   El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
varA = float(input("Introduce un número para el la base: "))
varB = float(input("Introduce un número para el exponente: "))
varC = varA ** varB

if varB < 0:
    print("El exponente introducido es un número negativo, por lo que el resultado de la potencia es 1.") 
if varB > 0: 
    if varC >= 0:
        print(f"{varA} elevado a {varB} equivale a {varC}")
if varB == 0:
        varB = 0
        print("El exponente indicado es 0. El resultado de la potencia sería de 1.")


# 8 - Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' y muestre el
# mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, la edad es mayor o igual a
# dieciocho y el sexo es 'F'. En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe
# imprimir 'POSIBLE'. Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
print("\n")
nota = float(input("Introduce la nota que obtuviste: "))
edad = int(input("Introduce tu edad: "))
sexo = str(input("Introduce tu sexo, 'm' para masculino o 'f' para femenino: ")).upper()
if (nota >= 5) and (edad >= 18) and (sexo == 'F'):
    print("ACEPTADA")
elif (nota >= 5) and (edad >= 18) and (sexo == 'M'):
    print("POSIBLE")
else:
    print("NO ACEPTADA")
