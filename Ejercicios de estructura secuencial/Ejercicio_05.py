import os

os.system("clear")

# 11 - Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
distancia = abs(num1-num2)
print(f"Distancia: {distancia}")


# 12 - Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos.
print("\n")
eje_1x = float(input("Coordenada 1 valor X: "))
eje_1y = float(input("Coordenada 1 valor Y: "))
eje_2x = float(input("Coordenada 2 valor X: "))
eje_2y = float(input("Coordenada 2 valor Y: "))
distanciaX = abs(eje_1x - eje_2x)
distanciaY = abs(eje_1y - eje_2y)
print(f"""
      Distancia X entre coordenadas 1 y 2: {distanciaX}
      Distancia Y entre coordenadas 1 y 2: {distanciaY}""")