import os

os.system("clear")


# 7 - Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.
print("## Vamos a sustituir en unas palabras, la primera letra que indiques por la segunda.")
cadena = str(input("Introduce algunas palabras: "))

clave = True
while clave:
    caracter1 = str(input("Escribe una única letra: "))
    if len(caracter1) == 0:
        print("Te había pedido solo una letra.")
        pass
    elif len(caracter1) == 1 :
        clave = False
clave2 = True
while clave2:
    caracter2 = str(input("Escribe otra única letra: "))
    if len(caracter2)  == 0:
        print("Te había pedido solo una letra.")
        pass
    elif len(caracter2) == 1 :
        clave2 = False
            
cadena2 = cadena.replace(caracter1, caracter2)
print(cadena2)



