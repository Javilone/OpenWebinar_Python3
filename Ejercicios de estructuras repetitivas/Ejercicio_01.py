import os
from random import randint

os.system("clear")

# 1 - Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y 
# se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)
num = int(input("Escribe un número entero para calcular su factorial: "))
resultado = 1;

contador = 2;
while contador <= num:
	resultado = resultado * contador;
	contador = contador + 1;
print("El resultado es", resultado)


print("\n")
# 2 - Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el 
# introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
# si se llega al limite de intentos te muestra el número que había generado.
aleatorio = randint(1,100)

intentos = 0
vidas = 10
while vidas > 0:
    preguntar = int(input("Introduce un número entre 1 y 100 para adivinar el que el ordenador ha escogido: "))
    
    if preguntar > aleatorio:
        print("El número que has puesto es mayor.")
        vidas -= 1
        intentos += 1
        continue
    elif preguntar < aleatorio:
        print("El número que has elegido es menor.")
        vidas -= 1
        intentos += 1
        continue
    elif preguntar == aleatorio:
        print(f"Acertaste a los {intentos} intentos!\nPrograma terminado.")
        break
if vidas == 0:
    print("Te quedaste sin vidas!")
