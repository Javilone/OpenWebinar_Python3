# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) 
# y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
# Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

entrada = int(input("Indica el número correspondiente del mes para saber cuántos días tiene. Ejemplo: Enero es 1: "))

print(f"El mes de {meses[entrada - 1]} contiene {dias_meses[entrada - 1]} días.")