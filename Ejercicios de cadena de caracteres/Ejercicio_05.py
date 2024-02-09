import os

os.system("clear")


# 10 - Introducir una cadena de caracteres e indicar si es un palíndromo. 
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.
print("## Para este ejemplo simple de búsqueda de palabras palíndromas, mejor probar sin tildes. Ejemplo de palíndromo:'Radar'")
palabra = str(input("Introduce una palabra para saber si es palíndroma: ")).lower()

palabra_invertida = []
palabra_correcta = []

for letra in palabra[::-1]:
    palabra_invertida.append(letra)


for letra2 in palabra:
    palabra_correcta.append(letra2)


print(palabra_invertida[::])
print(palabra_correcta[::])

if palabra_correcta == palabra_invertida:
    print("Eso era una palabra palíndroma.")
else:
    print("No era una palabra palíndroma.")