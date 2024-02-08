import os
import time

os.system("clear")

# 18 - Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

for hora in range(0,24):
	for minuto in range(0,60):
		for segundo in range(0,60):
			os.system("clear")
			print(hora,":",minuto,":",segundo)
			time.sleep(1)