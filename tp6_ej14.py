from typing import Any, Optional
from grafo import Graph


def existe_paso(grafo, origen, destino) -> bool:
    def __buscar_camino(g, v_actual, v_destino):
        pos = g.search(v_actual, 'value')
        if pos is None:
            return False
            
        nodo_actual = g[pos]
        
        # Caso base: llegamos al destino
        if nodo_actual.value == v_destino:
            return True
            
        nodo_actual.visited = True
        
        # Explorar aristas hacia los vecinos no visitados
        for edge in nodo_actual.edges:
            pos_vecino = g.search(edge.destination, 'value')
            if pos_vecino is not None and not g[pos_vecino].visited:
                if __buscar_camino(g, edge.destination, v_destino):
                    return True
                    
        return False

    # 1. Marcar todos los vértices como no visitados antes de empezar
    for vertex in grafo:
        vertex.visited = False

    # 2. Ejecutar la búsqueda desde el origen
    return __buscar_camino(grafo, origen, destino)

#grafo dirigido para probar
g = Graph(is_dir=True)

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge(1, 'A', 'B')
g.add_edge(1, 'B', 'C')

# Existe camino A -> B -> C
print(existe_paso(g, 'A', 'C'))  # True

# No existe camino C -> A (es dirigido)
print(existe_paso(g, 'C', 'A'))  # False

# No existe camino hacia D
print(existe_paso(g, 'A', 'D'))  # False