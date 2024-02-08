import os

os.system("clear")

# 15 - Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, 
# el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó 
# después de los 20 meses.

valor_producto = 0
mensualidad = 10
meses = 1

while meses <= 20:
    print(f"En el mes {meses} deberás pagar {mensualidad}€. ")
    
    mensualidad *= 2
    valor_producto = valor_producto + mensualidad
    meses += 1 
print(f"Estás en la ruina, muchacho. \nLo que compraste cuesta la friolera de {valor_producto}€ ")