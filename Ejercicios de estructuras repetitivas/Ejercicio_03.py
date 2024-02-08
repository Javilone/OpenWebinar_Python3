import os

os.system("clear")

# 5 -  Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 
# 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.
vocales = ['a', 'e', 'i', 'o', 'u']

clave = True
while clave:
    entrada = str(input("Introduce una letra para saber si es vocal o consonante. (En blanco para terminar): "))
    if entrada == '':
        clave = False
    if entrada in vocales:
        print(f"La letras que escribiste, {entrada}, es una vocal.")
    elif entrada not in vocales and entrada != '':
        print(f"La letra {entrada} no es una vocal, es una consonante.")

print("Programa terminado")


print("\n")
# 6 - Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
print("## Para ver los números pares entre dos números que escribas a continuación.")
entrada = int(input("Introduce un número entero: "))
entrada2 = int(input("Introduce otro número entero más: "))

clave2 = entrada + entrada2
while clave2 > 0:
    if clave2 % 2 == 0:
        print(clave2)
        clave2 -= 1
        continue
    else:
        clave2 -= 1
        continue
        
print("Programa terminado!")