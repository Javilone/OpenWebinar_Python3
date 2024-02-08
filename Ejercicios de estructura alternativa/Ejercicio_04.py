import os

os.system("clear")


# 9 - Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
num1 = int(input("Introduce un primero valor entero: "))
num2 = int(input("Introduce un segundo valor entero: "))
num3 = int(input("Introduce un tercer valor entero: "))

# Esto se podría resolver con una lista tal que: lista = [num1, num2, num3]
# para luego se ordenada y extraer sus elementos.
if num1>num2 and num1>num3:
	if num2>num3:
		print(num1,num2,num3)
	else:
		print(num1,num3,num2)
if num2>num1 and num2>num3:
	if num1>num3:
		print(num2,num1,num3)
	else:
		print(num2,num3,num1)
if num3>=num1 and num3>=num2:
	if num1>num2:
		print(num3,num1,num2)
	else:
		print(num3,num2,num1)