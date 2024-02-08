import os

os.system("clear")


# 8 - Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; 
# además, se quiere saber cuánto lleva ahorrado cada mes.

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
ahorrado = 0
mes = 0

while mes < 12:
    ahorrado = ahorrado + int(input(f"¿Cuánto dinero quieres ahorrar en {meses[mes]}: "))
    mes += 1
        
    
print(f"A final de año habrás ahorrado un total de {ahorrado} euros.")