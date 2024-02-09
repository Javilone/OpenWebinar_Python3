from random import randint


# 5 - Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
# y posterior ordene los elementos de menor a mayor.

lista_aleatoria = []
clave = 10
while clave != 0:
    lista_aleatoria.append(randint(1,10))
    clave -=1
    
lista_aleatoria.sort()
print(lista_aleatoria[::])