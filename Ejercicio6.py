# -*- coding: utf-8 -*-
hola = int(input("Dame un numero: "))
sumatoria = 0

while(True):
    if (hola % 3) == 0 or (hola % 5) == 0 or (hola % 7) == 0:
        sumatoria = sumatoria + hola
    hola = hola - 1
    if(hola == 0):
        break
print(sumatoria)
