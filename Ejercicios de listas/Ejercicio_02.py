# 2 - Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, 
# y muestra sus elementos  por la pantalla.

lista = []

lista.append(str(input("Introduce una palabra: ")))
lista.append(str(input("Introduce otra palabra: ")))
lista.append(str(input("Introduce una más palabra: ")))
lista.append(str(input("Introduce otra más palabra: ")))
lista.append(str(input("Introduce la última palabra: ")))

lista_inversa = lista.copy()
lista_inversa.sort(reverse=True)

print(lista_inversa[::])