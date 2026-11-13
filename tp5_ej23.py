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
                        root.other_values = aux.other_values  

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



CRIATURAS = [
    ('Ceto', []), ('Tifón', ['Zeus']), ('Equidna', ['Argos Panoptes']),
    ('Dino', []), ('Pefredo', []), ('Enio', []), ('Escila', []),
    ('Caribdis', []), ('Euríale', []), ('Esteno', []),
    ('Medusa', ['Perseo']), ('Ladón', ['Heracles']),
    ('Águila del Cáucaso', []), ('Quimera', ['Belerofonte']),
    ('Hidra de Lerna', ['Heracles']), ('León de Nemea', ['Heracles']),
    ('Esfinge', ['Edipo']), ('Dragón de la Cólquida', []), ('Cerbero', []),
    ('Cerda de Cromión', ['Teseo']), ('Ortro', ['Heracles']),
    ('Toro de Creta', ['Teseo']), ('Jabalí de Calidón', ['Atalanta']),
    ('Carcinos', []), ('Gerión', ['Heracles']), ('Cloto', []),
    ('Láquesis', []), ('Átropos', []), ('Minotauro de Creta', ['Teseo']),
    ('Harpías', []), ('Argos Panoptes', ['Hermes']),
    ('Aves del Estínfalo', []), ('Talos', ['Medea']), ('Sirenas', []),
    ('Pitón', ['Apolo']), ('Cierva de Cerinea', []), ('Basilisco', []),
    ('Jabalí de Erimanto', []),
]

DESCRIPCIONES = {
    'Talos': 'Gigante de bronce que custodiaba la isla de Creta.',
    'Cerbero': 'Perro de tres cabezas que guardaba la entrada al Hades.',
    'Hidra de Lerna': 'Serpiente acuática de múltiples cabezas que se regeneraban.',
    'Ladón': 'Dragón que custodiaba las manzanas de oro del Jardín de las Hespérides.',
    'Quimera': 'Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.',
    'León de Nemea': 'León de piel invulnerable que aterrorizaba la región de Nemea.',
}


def cargar_criaturas():
    arbol = BinaryTree()
    for nombre, derrotado_por in CRIATURAS:
        arbol.insert_node(nombre, {
            'derrotado_por': derrotado_por,
            'descripcion': '',
            'capturada': None,
        })
    return arbol



def nodos_inorden(arbol):
    """Devuelve la lista de nodos en orden inorden."""
    nodos = []

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            nodos.append(root)
            recorrer(root.right)

    recorrer(arbol.root)
    return nodos


def mostrar_criatura(nodo):
    datos = nodo.other_values
    derrotado = ', '.join(datos['derrotado_por']) if datos['derrotado_por'] else 'Nadie'
    print(f"Criatura: {nodo.value}")
    print(f"  Derrotada por: {derrotado}")
    print(f"  Capturada por: {datos['capturada'] if datos['capturada'] else 'Nadie'}")
    print(f"  Descripción: {datos['descripcion'] if datos['descripcion'] else 'Sin descripción'}")


# b. cargar una breve descripción
def cargar_descripcion(arbol, nombre, descripcion):
    nodo = arbol.search(nombre)
    if nodo is None:
        return False
    nodo.other_values['descripcion'] = descripcion
    return True


# d. los 3 héroes/dioses que derrotaron más criaturas
def top_derrotadores(arbol, cantidad=3):
    conteo = {}
    for nodo in nodos_inorden(arbol):
        for heroe in nodo.other_values['derrotado_por']:
            conteo[heroe] = conteo.get(heroe, 0) + 1
    ranking = sorted(conteo.items(), key=lambda par: (-par[1], par[0]))
    return ranking[:cantidad]


# e. criaturas derrotadas por un héroe/dios
def criaturas_derrotadas_por(arbol, heroe):
    for nodo in nodos_inorden(arbol):
        if heroe in nodo.other_values['derrotado_por']:
            print(nodo.value)


# f. criaturas que no han sido derrotadas
def criaturas_no_derrotadas(arbol):
    for nodo in nodos_inorden(arbol):
        if not nodo.other_values['derrotado_por']:
            print(nodo.value)


# g / h. registrar quién capturó a una criatura
def capturar(arbol, nombre, heroe):
    nodo = arbol.search(nombre)
    if nodo is None:
        return False
    nodo.other_values['capturada'] = heroe
    return True


# k. agregar un derrotador a una criatura (la clave no cambia, se edita el nodo)
def agregar_derrotador(arbol, nombre, heroe, nota=None):
    nodo = arbol.search(nombre)
    if nodo is None:
        return False
    if heroe not in nodo.other_values['derrotado_por']:
        nodo.other_values['derrotado_por'].append(heroe)
    if nota:
        nodo.other_values['descripcion'] = (nodo.other_values['descripcion'] + ' ' + nota).strip()
    return True


# l. cambiar el nombre (como es la clave del árbol: se elimina y se reinserta)
def renombrar_criatura(arbol, nombre_actual, nombre_nuevo):
    valor, datos = arbol.delete_node(nombre_actual)
    if valor is None:
        return False
    arbol.insert_node(nombre_nuevo, datos)
    return True


# n. criaturas capturadas por un héroe/dios
def criaturas_capturadas_por(arbol, heroe):
    for nodo in nodos_inorden(arbol):
        if nodo.other_values['capturada'] == heroe:
            print(nodo.value)



def main():
    arbol = cargar_criaturas()

    print('--- b. Carga de descripciones ---')
    for nombre, descripcion in DESCRIPCIONES.items():
        cargar_descripcion(arbol, nombre, descripcion)
    print(f'Se cargaron {len(DESCRIPCIONES)} descripciones')

    print('\n--- a. Listado inorden de criaturas y quién las derrotó ---')
    for nodo in nodos_inorden(arbol):
        derrotado = ', '.join(nodo.other_values['derrotado_por']) or '-'
        print(f'{nodo.value}: {derrotado}')

    print('\n--- c. Información de Talos ---')
    nodo = arbol.search('Talos')
    if nodo is not None:
        mostrar_criatura(nodo)

    print('\n--- d. Los 3 que derrotaron más criaturas ---')
    for heroe, cantidad in top_derrotadores(arbol, 3):
        print(f'{heroe}: {cantidad}')

    print('\n--- e. Criaturas derrotadas por Heracles ---')
    criaturas_derrotadas_por(arbol, 'Heracles')

    print('\n--- f. Criaturas no derrotadas ---')
    criaturas_no_derrotadas(arbol)

    print('\n--- h. Heracles captura a cuatro criaturas ---')
    for nombre in ('Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto'):
        capturar(arbol, nombre, 'Heracles')
    print('Listo')

    print('\n--- i. Búsqueda por coincidencia: "jabal" ---')
    arbol.proxy_search('jabal')

    print('\n--- j. Eliminar Basilisco y Sirenas ---')
    for nombre in ('Basilisco', 'Sirenas'):
        valor, _ = arbol.delete_node(nombre)
        print(f'{nombre}: {"eliminado" if valor else "no encontrado"}')

    print('\n--- k. Aves del Estínfalo: Heracles derrotó a varias ---')
    agregar_derrotador(arbol, 'Aves del Estínfalo', 'Heracles', 'Heracles derrotó a varias de ellas.')
    mostrar_criatura(arbol.search('Aves del Estínfalo'))

    print('\n--- l. Ladón pasa a llamarse Dragón Ladón ---')
    if renombrar_criatura(arbol, 'Ladón', 'Dragón Ladón'):
        mostrar_criatura(arbol.search('Dragón Ladón'))

    print('\n--- m. Listado por nivel ---')
    arbol.by_level()

    print('\n--- n. Criaturas capturadas por Heracles ---')
    criaturas_capturadas_por(arbol, 'Heracles')


if __name__ == '__main__':
    main()