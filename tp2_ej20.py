#Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.

from pila import Stack

Direcciones = {
    'norte'
    'sur'
    'este'
    'oeste'
    'noreste'
    'sureste'
    'noroeste'
    'suroeste'
}

Direccion_Opuesta = {
    'norte' : 'sur',
    'sur' : 'norte',
    'este' : 'oeste',
    'oeste' : 'este',
    'noreste' : 'suroeste',
    'sureste' : 'noroeste',
    'noroeste' : 'sureste',
    'suroeste' : 'noreste',
}

def Movimientos() -> Stack:
#guarda los movimientos en la pila

    pila = Stack()

    direccion = ''

    while direccion != 'fin':
        direccion = input('ingrese la direccion (puntos cardinales), para salir ingrese fin')
        if direccion not in Direcciones:
            print ('direccion invalida')
            continue
        pasos = int(input('ingrese la cantidad de pasos a esa direccion'))    
        if pasos <= 0:
            print ('los pasos deben ser mayor a 0')
        continue
    movimiento= (pasos, direccion)
    pila.push(movimiento)

    return pila

def pila_retorno(pila_movimientos: Stack) -> Stack:

    pila_retorno = Stack()
    pila_aux = Stack()
    pila_copia = Stack()
    #pilas para copiar y no perder la original

    while pila_movimientos.size() > 0:
        value = pila_movimientos.pop()
        pila_aux.push(value)

    while pila_aux.size() > 0  :
        value = pila_aux.pop()
        pila_copia.push(value)
        pila_movimientos.push(value)

    while pila_copia.size() > 0:
        value = pila_copia.pop()
        pila_aux.push(value)

    while pila_aux.size() > 0:
        pasos,direccion = pila_aux.pop()
        pila_retorno.push((pasos, Direccion_Opuesta[direccion]))        

    return pila_retorno


#main
print('movimientos de ida ')
Movimientos.show()

pila_vuelta=pila_retorno(Movimientos)

print('movimientos de vuelta ')
pila_vuelta.show()

