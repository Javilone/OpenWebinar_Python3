import os

os.system("clear")


# 8 - Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
print("## Vamos a cambiar el orden de las mayúsculas minúsculas.")

cadena = str(input("Introduce alguna frase corta: "))
cadena2 = cadena.swapcase()
print(cadena2)


# 9 - Realizar un programa que compruebe si una cadena contiene una subcadena. 
# Las dos cadenas se introducen por teclado.
textoA = str(input("Introduce algunas palabras: "))
textoB = str(input("Introduce algunas otras palabras: "))
if textoB in textoA:
    print("Habían algunas coincidencias entre tus frases.")
else:
    print("No se encontraron coincidencias.")


