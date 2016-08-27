'''
Created on Aug 27, 2016

@author: python
'''
def agregar (variable):
    lista = []
    lista.append((variable))
    return lista
    
def borrar (indice, lista):
        lista.remove(lista[indice])
        return lista
if __name__ == "__main__":
    seguir = 'S'
    lista = []
    lista2 = []
    while seguir == 'S':
        opcion = int(raw_input("Ingrese opcion 1 para agregar una persona, opcion 2 para borrar"))
        if opcion == 1:
            lista2 = agregar(raw_input("Ingrese un nombre: "))
            lista = lista2[ : ]
        elif opcion == 2:
            lista2 = borrar(int(raw_input("Ingrese indice a borrar")), lista)
            lista = lista2 [ : ]
