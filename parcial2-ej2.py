from grafo import Graph
from monton import HeapMin
from typing import Any, Optional
from copy import copy

g = Graph(is_dir=False)

#1)Carga de personajes
personajes = [
    ['Luke Skywalker', [4, 5, 6, 7, 8, 9]],
    ['Darth Vader', [3, 4, 5, 6]],
    ['Yoda', [1, 2, 3, 5, 6, 8]],
    ['Boba Fett', [2, 5, 6]],
    ['C-3PO', [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ['Leia', [3, 4, 5, 6, 7, 8, 9]],
    ['Rey', [7, 8, 9]],
    ['Kylo Ren', [7, 8, 9]],
    ['Chewbacca', [3, 4, 5, 6, 7, 8, 9]],
    ['Han Solo', [4, 5, 6, 7, 9]],
    ['R2-D2', [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ['BB-8', [7, 8, 9]],
]

for nombre, episodios in personajes:
    g.add_vertex(nombre, episodios)

#El peso de la arista es la cantidad de capitulos que tienen en comun, si no comparten ninguno no se crea la arista
for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        en_comun = 0
        for ep in personajes[i][1]:
            if ep in personajes[j][1]:
                en_comun += 1
        if en_comun > 0:
            g.add_edge(en_comun, personajes[i][0], personajes[j][0])


# 2)Arbol de expansion minimo (Kruskal)
def kruskal(g, origen_vertex):
    bosque = []              #Cada elemento es un arbol
    aristas = HeapMin()      #Por cola de prioridad sale primero la que pesa menos
    for vertice in g:
        bosque.append([vertice.value])
        for arista in vertice.edges:
            aristas.arrive([vertice.value, arista.destination], arista.weight)

    elegidas = []
    while aristas.size() > 0:
        peso, par = aristas.attention()
        ind_a = -1
        ind_b = -1
        for i in range(len(bosque)):
            if par[0] in bosque[i]:
                ind_a = i
            if par[1] in bosque[i]:
                ind_b = i
        if ind_a != ind_b:                      
            bosque[ind_a] = bosque[ind_a] + bosque[ind_b]
            bosque.pop(ind_b)
            elegidas.append([par[0], par[1], peso])

    
    arbol = []
    for ar in elegidas:
        for componente in bosque:
            if origen_vertex in componente and ar[0] in componente:
                arbol.append(ar)
    return arbol


print('Arbol de expansion minimo :')
for inicio in ['C-3PO', 'Yoda', 'Leia']:
    arbol = kruskal(g, inicio)
    total = 0
    print('Desde', inicio + ':')
    for origen, destino, peso in arbol:
        print('  ', origen, '-', destino, '(peso', peso, ')')
        total += peso
    print('  peso total:', total)


# 3)Maximo de episodios compartidos
maximo = 0
for vertice in g:
    for arista in vertice.edges:
        if arista.weight > maximo:
            maximo = arista.weight

print('Maximo de episodios compartidos: ', maximo,)
for vertice in g:
    for arista in vertice.edges:
        # el grafo no es dirigido, cada par aparece dos veces: lo muestro una sola
        if arista.weight == maximo and vertice.value < arista.destination:
            print('  ', vertice.value, 'y', arista.destination)


# 4)Camino mas corto con Dijkstra
def camino_corto(grafo, origen, destino):
    paths = grafo.dijkstra(origen)
    peso_total = None
    camino = []
    buscado = destino
    while paths.size() > 0:
        value = paths.pop()        # value = [vertice, costo, vertice anterior]
        if value[0] == buscado:
            if peso_total is None:
                peso_total = value[1]
            camino.append(value[0])
            buscado = value[2]
    camino.reverse()
    print('  ', ' --> '.join(camino), ' costo total:', peso_total)


print('Caminos mas cortos: ')
camino_corto(g, 'C-3PO', 'R2-D2')
camino_corto(g, 'Yoda', 'Darth Vader')


# 5)Personajes que aparecen en los nueve capitulos
print('Aparecieron en los 9 episodios: ')
for vertice in g:
    if len(vertice.other_values) == 9:
        print('  ', vertice.value)