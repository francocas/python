# -*- coding: utf-8 -*-
hola = int(input("Dame un numero: "))
sumatoria = 0

while(True):
    sumatoria = sumatoria + hola
    hola = hola - 1
    if(hola == 0):
        break
print(sumatoria)
