from random import randint

# 1 - Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

lista_aleatoria = []
clave = 10
while clave != 0:
    lista_aleatoria.append(randint(1,10))
    clave -=1
    
for n in lista_aleatoria:
    print(f"Valor: {n} en la lista. Su cuadrado es: {n * n}")