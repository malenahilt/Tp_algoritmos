#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posicion uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
#la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
from copy import copy, deepcopy
from typing import Any


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()

    def show(self) -> None:
        stack_aux = Stack()
        stack_aux._Stack__elements = copy(self.__elements)
        while stack_aux.size() > 0:
            value = stack_aux.pop()
            print(value)

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]


# ── Carga de datos ──────────────────────────────────────────
# Cada elemento: (nombre, cantidad de películas)
# El último en pushearse queda en el tope (posición 1)

class Stack:
 
    def __init__(self):
        self.__elements = []
 
    def push(self, value: Any) -> None:
        self.__elements.append(value)
 
    def pop(self) -> Any:
        return self.__elements.pop()
 
    def show(self) -> None:
        stack_aux = Stack()
        stack_aux._Stack__elements = copy(self.__elements)
        while stack_aux.size() > 0:
            value = stack_aux.pop()
            print(value)
 
    def size(self) -> int:
        return len(self.__elements)
 
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
        

pila = Stack()
pila.push(("Gamora",          4))
pila.push(("Hulk",            7))
pila.push(("Captain America", 6))
pila.push(("Clint Barton",    6))
pila.push(("Wanda Maximoff",  5))
pila.push(("Rocket Raccoon",  6))
pila.push(("Black Widow",     7))
pila.push(("Doctor Strange",  5))
pila.push(("Nebula",          6))
pila.push(("Groot",           5))
pila.push(("Thor",            8))
pila.push(("Iron Man",        9))
 
 

print('pila de los heroes de marvel: ')
pila.show()

#punto a)
pila_aux = Stack()
posicion = 0
posicion_roc= 0
posicion_gro = 0

while pila.size() > 0:
    heroe, peliculas = pila.pop()
    if heroe == 'Rocket Raccoon':
        posicion_roc = posicion

    if heroe == 'Groot' :
        posicion_gro = posicion
    posicion += 1   
    pila_aux.push((heroe, peliculas))   

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print ('el heroe Rocket Raccon se encuentra en la posicion: {posicion_roc}')
print('el heroe Groot se encuentra en la posicion {posicion_gro}')

#punto b)
pila_aux = Stack()

while pila.size() > 0:
    heroe, peliculas = pila.pop()
    if peliculas > 5:
        pila_aux.push((heroe, peliculas))

while pila_aux.size () > 0:
    pila.push(pila_aux.pop())

#punto c)
pila_aux = Stack()
total_pel = 0
while pila.size() > 0:
    heroe, peliculas = pila.pop()
    if heroe == 'Black Widow':
        total_pel = peliculas
    pila_aux.push((heroe,peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

#punto d)
pila_aux = Stack()
while pila.size() > 0:
    heroe, peliculas = pila.pop()
    if heroe[0] in ('C','D','G'):
        print(f'{heroe} ({peliculas} peliculas)')
    pila_aux.push((heroe, peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())