import os

os.system("clear")

# 1 -Escribir por pantalla cada carácter de una cadena introducida por teclado.
cadena1 = "Javilone"
for n in cadena1:
    print(n)
    

print("\n")
# 2 - Realizar un programa que comprueba si una cadena leída por teclado comienza 
# por una subcadena introducida por teclado.
cadena2 = str(input("Introduce alguna palabra o palabras: "))
cadena3 = str(input("Introduce otra palabra o palabras:" ))
if cadena2.startswith(cadena3):
    print("El primer texto comienza igual que el segundo que pusiste.")
else:
    print("No comienzan de la misma forma.")
    
    
print("\n")
# 3 - Pide una cadena y un carácter por teclado (valida que sea un carácter) y 
# muestra cuantas veces aparece el carácter en la cadena.
cadena4 = str(input("Introduce alguna palabra: "))
caracter = str(input("Introduce alguna letra: "))
print(f"El caracter {caracter} aparece {cadena4.count(caracter)} veces.")
