import os

os.system("clear")

# 4 - Crea un programa que pida al usuario dos números y muestre su división si 
# el segundo no es cero, o un mensaje de aviso en caso contrario.
varA = float(input("Escribe un primer valor numérico: "))
varB = float(input("Escribe el segundo valor numérico entre el que quieres dividir: "))
if varB != 0 and varB >= 0:
    print(f"{varA} dividido entre {varB} es igual a {varA/varB}")
else:
    print("El número por el que quieres dividir es erroneo. No se puede dividir por debajo de 0.")


# 5 - Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido 
# "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error.
print("\n")
varC = str(input("Escribe tu nombre de usuario: "))
varD = str(input("Escribe tu contreaseña de usuario (solo letras): "))
if (varC == "pepe") & (varD == "asdasd"):
    print(f"Bienvenido, {varC}!")
else:
    print("Usuario incorrecto.")

# 6 - Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
print("\n")
varE = str(input("Escribe una letra, mayúscula o minúscula: "))
if varE == varE.upper():
    print("Escribiste una letra mayúscula.")
else :
    print("La letra que escribiste es minúscula")