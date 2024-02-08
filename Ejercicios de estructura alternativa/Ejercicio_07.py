import os

os.system("clear")

# 14 - La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
# ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que 
# entrega en un embarque, considerando lo siguiente: 
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; 
# y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.  
# Realice  un  algoritmo  para  determinar  la  ganancia  obtenida.

precio_uvas = int(input("¿A cuánto está el precio de la uva en céntimos?: "))
tipo_uva = str(input("¿Cuál es el tipo de uva? A | B: ")).lower()
tamaño_uva = int(input("¿Cuál es el tamaño de la uva?: "))
cantidad = float(input("¿Cuantos kilos de uva entregas?: "))

if tipo_uva == "a" or tipo_uva == "b":
    if tipo_uva == "a":
        if tamaño_uva == 1:
            precio_uvas = precio_uvas + 20
        else:
            precio_uvas = precio_uvas + 30
        if tamaño_uva == 2:
            precio_uvas = precio_uvas - 30
        else:
            precio_uvas = precio_uvas - 50
        precio_uvas = precio_uvas * cantidad
        print(f"""
              Por {cantidad} kilos de uvas del tipo {tipo_uva} y tamaño {tamaño_uva}, 
              se te paga la cantidad de: 
              {precio_uvas/100}€""")
else: 
    print("No es un tipo válido de uva.")