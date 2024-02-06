import os

# 7 - Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos 
# corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
os.system("clear")
minutos = int(input("¿Cuántos minutos quieres convertir en horas?: "))
horas = round((minutos / 60), 2) # o usar 2f
print(f"{minutos} minutos equivalen a {horas} horas/minutos")

# 8 - Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que 
# realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base = float(input("Cuál es el sueldo base del vendedor?: "))
comision = ((sueldo_base * 10) / 100)
print(f"""
      Este mes, por las comisiones recibirás: {comision *3}€
      Y el total del sueldo más comisiones asciende a: {sueldo_base + (comision *3)}€""")

# 9 - Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto 
# deberá pagar finalmente por su compra.
articulo = float(input("¿Cuánto cuesta el artículo?: "))
descuento = ((articulo * 15) / 100)
print(f""" 
      El artículo, que costaba {articulo}€, se queda finalmente
      en un precio de {articulo - descuento}€.
      Te ahorrarías {descuento}€""")