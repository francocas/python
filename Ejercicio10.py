# -*- coding: utf-8 -*-
import random
usuario = int(input("Piedra(0), Papel (1) o Tijera(2): "))
print ("Usuario: ", usuario)
maquina = random.randrange(3)
print ("Maquina: ", maquina)
if maquina == 1 and usuario == 0:
    print ("Gana la maquina")
elif maquina == 1 and usuario == 2:
    print ("Gana el usuario")
elif maquina == 1 and usuario == 1:
    print("Empate")
elif maquina == 0 and usuario == 0:
    print("Empate")
elif maquina == 0 and usuario == 1:
    print("Gana el usuario")
elif maquina == 0 and usuario == 2:
    print("Gana la maquina")
elif maquina == 2 and usuario == 0:
    print("Gana el usuario")
elif maquina == 2 and usuario == 1:
    print("Gana la maquina")
elif maquina == 2 and usuario == 2:
    print("Empate")