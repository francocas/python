# -*- coding: utf-8 -*-
import webbrowser
import time
var = "S"
tiempo = int(input("Ingrese el tiempo a esperar (En segundos)"))
while var == "S":

    time.sleep(tiempo)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=U9nXl68XnVI")
    var=input("Desea continuar? (Ingrese S para continuar)")
    var = var.upper