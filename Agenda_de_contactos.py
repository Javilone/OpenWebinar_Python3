import os
import time

os.system("clear")


# 5 - Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números 
# de teléfono. El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, 
# debe permitir ingresar el teléfono correspondiente.
# 
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por 
# dicha cadena.
# 
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.

# Implementar el programa con un diccionario.

agenda = {}

clave = True
while clave:
    
    menu = int(input("""
        1 - Añadir / Mostrar contacto.
        2 - Buscar contacto.
        3 - Borrar contacto.
        4 - Ver todos los contactos.
        
        Elije una opción del menú marcando su número: """))

    if (menu < 1) or (menu > 4):
        # print("Tienes que introducir un número entre el 1 y el 3.")
        os.system("clear")
        continue
    elif menu == 1:
        nombre = str(input("\n>> Introduce nombre de usuario: "))
        if nombre in agenda:
            print("\n>> Parece que el usuario ya existe.")
            print(f"\n# Nombre: {nombre}. Teléfono: {agenda[nombre]}")
        elif nombre not in agenda:
            telefono = int(input(">> Introduce el teléfono de la persona: "))
            agenda[nombre]=telefono
            print(">> Contacto creado correctamente!")
            print("Volviendo solo al menú en breves.")
            time.sleep(4)
            os.system("clear")    
        
    elif menu == 2:
        buscar_contacto = str(input("\n>> Nombre del contacto a buscar: "))
        if buscar_contacto in agenda:
            print(f"\n# El contacto {buscar_contacto} existe en la agenda. Estos son sus datos.")
            print(f"# Nombre: {nombre}. Teléfono: {agenda[nombre]}")
        elif buscar_contacto not in agenda:
            print(f"{buscar_contacto} no existe en la agenda.")
            print("Volviendo solo al menú en breves.")
            time.sleep(4)
            os.system("clear") 
            continue
            
    elif menu == 3:
        borrar_contacto = str(input("\n >> Introduce el nombre del contacto a borrar: "))
        if borrar_contacto not in agenda:
            print(f"{borrar_contacto} no existe en la agenda")
            print("Volviendo solo al menú en breves.")
            time.sleep(4)
            os.system("clear") 
            continue
        elif borrar_contacto in agenda:
            confirmar = str(input(f"""
            ¿Seguro que deseas borrar a {nombre}?
            Escribe s (si) o n (no): """))
            if confirmar == "s":
                del(agenda[nombre])
                print(f">> {nombre} borrado correctamente.")
                print("Volviendo solo al menú en breves.")
                time.sleep(4)
                os.system("clear") 
                continue
            elif confirmar == "n":
                print(f"\n >> {nombre} se ha mantenido.")
                print("Volviendo solo al menú en breves.")
                time.sleep(4)
                os.system("clear") 
                continue
                
    elif menu == 4:
        print(f"\n>> Estos son todos los contactos almacenados en la agenda")
        for contacto, telefono in agenda.items():
            print(f"""

            Nombre: {contacto} ---> Teléfono: {telefono}""")
                