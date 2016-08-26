# -*- coding: utf-8 -*-
hola = int(input("Dame un numero: "))
opcion = input("Desea el factorial o la sumatoria? : F/S \t")
opcion = opcion.upper()
sumatoria = 0
factorial = 1
if  opcion == "S":
    while(True):
        sumatoria = sumatoria + hola
        hola = hola - 1
        if(hola == 0):
            break
    print(sumatoria)
elif opcion == "F":
    while(True):
        factorial = factorial * hola
        hola = hola - 1
        if(hola == 0):
            break
    print(factorial)
else:
    print ("Opcion invalida")
