from typing import Any, Optional
from cola import Queue


class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0

    def __str__(self):
        return self.value


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

    def insert_node(self, value: Any, other_value=None) -> None:

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

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            aux = None
            if root.right is None:
                return root.left, root
            else:
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    root.left, x, other_value = __delete_node(root.left, value)
                elif value > root.value:
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        return root.right, x, other_value
                    elif root.right is None:
                        return root.left, x, other_value
                    else:
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values  # CORREGIDO

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
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

        node = __search(self.root, value)

        return node

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
        if control:  # rotacion hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:  # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:  # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:  # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:

        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)
            print(root.value, root.height)
            if root.right is not None:
                __inorden(root.right)

        __inorden(self.root)

    def postorden(self) -> None:

        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

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

    def inorden_villain(self) -> None:

        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

        __inorden_villain(self.root)  # CORREGIDO

    def postorden_hero(self):

        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:

        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:

        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix in root.value.lower():
                print(root.value)
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count



def generar_bosque(arbol):
    """Recorre el árbol y devuelve (arbol_heroes, arbol_villanos)."""
    heroes = BinaryTree()
    villanos = BinaryTree()

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            destino = villanos if root.other_values['is_villain'] else heroes
            destino.insert_node(root.value, root.other_values)
            recorrer(root.right)

    recorrer(arbol.root)
    return heroes, villanos


def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)



def cargar_mcu():
    arbol = BinaryTree()

    heroes = [
        'Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye',
        'Spider-Man', 'Black Panther', 'Captain Marvel', 'Ant-Man',
        'Scarlet Witch', 'Vision', 'Falcon', 'Star-Lord', 'Gamora', 'Drax',
        'Groot', 'Rocket Raccoon',
        'Doctor Strage',          # mal cargado a propósito (punto e)
    ]
    villanos = [
        'Thanos', 'Loki', 'Ultron', 'Red Skull', 'Hela', 'Killmonger', 'Ronan',
        'Vulture', 'Mysterio', 'Ego', 'Kang', 'Dormammu', 'Whiplash',
        'Crossbones',
    ]

    for nombre in heroes:
        arbol.insert_node(nombre, {'is_villain': False})
    for nombre in villanos:
        arbol.insert_node(nombre, {'is_villain': True})

    return arbol


def main():
    arbol = cargar_mcu()

    print('--- b. Villanos ordenados alfabéticamente ---')
    arbol.inorden_villain()

    print('\n--- c. Superhéroes que empiezan con C ---')
    arbol.inorden_hero_star_with('C')

    print('\n--- d. Cantidad de superhéroes ---')
    print(arbol.count_heroes())

    print('\n--- e. Búsqueda por proximidad de "doctor" y corrección ---')
    arbol.proxy_search('doctor')                     # muestra "Doctor Strage"
    nombre, datos = arbol.delete_node('Doctor Strage')
    arbol.insert_node('Doctor Strange', datos)
    print('Después de corregir:')
    arbol.proxy_search('doctor')

    print('\n--- f. Superhéroes en orden descendente ---')
    arbol.postorden_hero()

    print('\n--- g. Bosque ---')
    arbol_heroes, arbol_villanos = generar_bosque(arbol)

    print('I. Cantidad de nodos')
    print('Árbol de superhéroes:', contar_nodos(arbol_heroes.root))
    print('Árbol de villanos:', contar_nodos(arbol_villanos.root))

    print('\nII. Barrido ordenado alfabéticamente (nombre, altura del nodo)')
    print('Superhéroes:')
    arbol_heroes.inorden()
    print('Villanos:')
    arbol_villanos.inorden()


if __name__ == '__main__':
    main()