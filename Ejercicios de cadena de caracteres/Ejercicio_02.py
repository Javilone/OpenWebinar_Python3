import os

os.system("clear")


# 4 - Suponiendo que hemos introducido una cadena por teclado que representa una frase 
# (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
print("# Vamos a contar palabras.")
cadena1 = str(input("Introduce alguna pequeña frase: "))
cadena1 = cadena1.split()
print(f"La frase tenía {len(cadena1)} palabras ")


print("\n")
# 5 - Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las 
# iniciales en mayúsculas.
print("# Método title()")
nombre = "javier lopez lara"
print(f"La variable {nombre} está en minúsculas. Y así queda con su método title: {nombre.title()}")

print("\n")
# 6 - Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena 
# resultado de invertir la primera.
print("# Dar la vuelta a tu palabra.")
palabra = str(input("Introduce la palabra a la que quieres dar la vuelta: ")).strip()
lista = []
for n in palabra:
    lista.append(n)
print("".join(lista[::-1]))
