import os

os.system("clear")

# 19 - Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que 
# seleccionamos la opción de "Salir".
clave = True
while clave:
    try:
        menu = int(input("""
        Introduce una opción:
            - 1: Saludar
            - 2: Padre Nuestro
            - 3: Maestro Python
            - 4: Maldecir
            - 5: SALIR
            ## ¿Cuán eliges?: """))

        if menu == 1:
            print("\nHola, holita, vecinito!")
            continue
        elif menu == 2:
            print("\nPadre Nuestro que estás en los cielos. Bendito sea tu nombre. Ven a nosotros tu reino...")
            continue
        elif menu == 3:
            print("\nSeré el mejor Maestro Python. Hazte con todo!")
            continue
        elif menu == 4:
            print("\nMardiciones pa tóhs!")
            continue
        elif menu == 5:
            print("\nChaito!")
            clave = False
        elif menu > 5:
            print("\n ¡¡Ese menú aún no existe!!")
    except ValueError:
        print("\n¡¡¡ Escribe bien el número, hijo!!!")
print("Sayonara, baby!")