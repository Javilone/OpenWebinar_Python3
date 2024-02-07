import math

# 1 - Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
usuario = input("¡Hola! ¿Cómo te llamas? ")
print(f"Encantado de conocerte, {usuario}")
print("\n")

# 2 - Calcular el perímetro y área de un rectángulo dada su base y su altura.
rect_altura = 10
rect_ancho = 25

area = rect_altura * rect_ancho
perímetro = (2*rect_altura) + (2*rect_ancho)
print(f"El area del rectángulo es: {area}. \nEl perímetro del rectángulo es: {perímetro}.")
print("\n")

# 3 - Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
catetoA = float(input("Introduce un número: "))
catetoB = float(input("Introduce un segundo número: "))
hipotenusa = math.sqrt(catetoA ** 2 + catetoB ** 2)
print(f"La hipotenusa es {hipotenusa}")