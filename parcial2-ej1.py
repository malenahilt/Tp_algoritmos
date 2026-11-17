from arbol import BinaryTree
from cola import Queue
from typing import Any

import json
with open('pokemon.json', 'r', encoding='utf-8') as archivo:
    lista_pokemons = json.load(archivo)


class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value, other_value=None):

        def __insert_node(root, value, other_value=None):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)

            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = __insert_node(self.root, value, other_value)

    def search(self, value):
        def __search(root, value):
            aux = None
            if root is not None:
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)
            return aux

        return __search(self.root, value)

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control:  #rotacion hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:  #rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    
    def inorden(self):
        #orden ascendentte
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value, '-', root.other_values['nombre'])
                __inorden(root.right)

        __inorden(self.root)

    def by_level(self):
        #por nivel, usando cola
        pendings = Queue()
        if self.root is not None:
            pendings.arrive(self.root)
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)

    def proximity_search(self, text):
        #muestra los que contienen el texto
        def __proximity(root, text):
            if root is not None:
                __proximity(root.left, text)
                if text in root.value.lower():
                    mostrar_pokemon(root.other_values)
                __proximity(root.right, text)

        __proximity(self.root, text.lower())

    def show_weak_against(self, tipos):
        #muestra los que tienen alguna debilidad en la lista "tipos"
        def __weak(root, tipos):
            if root is not None:
                __weak(root.left, tipos)
                debil = False
                for t in tipos:
                    if t in root.other_values['debilidades']:
                        debil = True
                if debil:
                    print(root.value)
                __weak(root.right, tipos)

        __weak(self.root, tipos)

    def count_types(self):
        #el arbol de tipos guarda una lista de nombres por cada tipo
        def __count(root):
            if root is not None:
                __count(root.left)
                print(root.value, ':', len(root.other_values))
                __count(root.right)

        __count(self.root)

    def count_M_G(self, campo):
        #cuenta cuantos pokemon tienen True en 'mega' o 'gigamax'
        def __count(root):
            cant = 0
            if root is not None:
                cant += __count(root.left)
                if root.other_values[campo]:
                    cant += 1
                cant += __count(root.right)
            return cant

        return __count(self.root)


def mostrar_pokemon(p):
    print('Nombre :', p['nombre'], ' N° :', p['numero'])
    print('Tipos :', p['tipos'])
    print('Debilidades :', p['debilidades'])
    print('Mega evolucion :', p['mega_evolucion'], ' Gigamax :', p['gigamax'])


def cargar_arboles(pokemons):
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()

    for p in pokemons:
        arbol_nombre.insert_node(p['nombre'], p)
        arbol_numero.insert_node(p['numero'], p)

        #un nodo por tipo, con la lista de nombres de ese tipo
        for tipo in p['tipos']:
            nodo = arbol_tipo.search(tipo)
            if nodo is None:
                arbol_tipo.insert_node(tipo, [p['nombre']])
            else:
                nodo.other_values.append(p['nombre'])

    return arbol_nombre, arbol_numero, arbol_tipo


def mostrar_nombres_tipo(arbol_tipo, tipo):
    nodo = arbol_tipo.search(tipo)
    if nodo is not None:
        print('Pokemons de tipo', tipo + ':')
        for nombre in nodo.other_values:
            print(' ', nombre)
    else:
        print('No hay pokemons de tipo', tipo)


def debiles_frente(arbol_nombre, nombre):
    #busca al pokemon, toma sus tipos y muestra a los que son debiles a ellos
    nodo = arbol_nombre.search(nombre)
    if nodo is not None:
        tipos = nodo.other_values['tipos']
        print('Debiles frente a', nombre, '(tipos :', tipos, '):')
        arbol_nombre.show_weak_against(tipos)
    else:
        print(nombre, 'no encontrado')


arbol_nombre, arbol_numero, arbol_tipo = cargar_arboles(lista_pokemons)

# 1)datos de un pokemon por numero
print('Busqueda por numero (25): ')
nodo = arbol_numero.search(25)
if nodo is not None:
    mostrar_pokemon(nodo.other_values)

# 2)datos por nombre, por proximidad
print('Busqueda por proximidad ("bul") : ')
arbol_nombre.proximity_search('bul')

# 3)nombres por tipo
print('Nombres por tipo : ')
for tipo in ['fantasma', 'fuego', 'acero', 'electrico']:
    mostrar_nombres_tipo(arbol_tipo, tipo)

# 4)listados
print('Ascendente por numero : ')
arbol_numero.inorden() 
print('Ascendente por nombre : ')
arbol_nombre.inorden()
print('Por nivel por nombre : ')
arbol_nombre.by_level()

# 5)debiles frente a Jolteon, Lycanroc y Tyrantrum
print('Debilidades : ')
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    debiles_frente(arbol_nombre, nombre)
    print()

# 6)cantidad por tipo
print('Cantidad por tipo : ')
arbol_tipo.count_types()

# 7) y 8)mega_evolucion y gigamax
print('Pokemons con megaevolucion :', arbol_numero.count_M_G('mega_evolucion'))
print('Pokemons con gigamax :', arbol_numero.count_M_G('gigamax'))