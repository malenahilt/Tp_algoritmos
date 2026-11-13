from typing import Any, Optional
from grafo import Graph


def eliminar_arista(vertice, destino) -> Optional[Any]:
    return vertice.edges.delete_value(destino, 'destination')



g = Graph(is_dir=True)

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge(10, 'A', 'B')
g.add_edge(25, 'A', 'C')

print("--- Grafo antes de eliminar ---")
g.show()


pos_vertice = g.search('A', 'value')

if pos_vertice is not None:
    vertice_a = g[pos_vertice]

    # Caso 1: Eliminar una arista que SÍ existe ('B')
    arista_eliminada = eliminar_arista(vertice_a, 'B')
    print(f"\nResultado al eliminar 'B': {arista_eliminada}")

    # Caso 2: Intentar eliminar una arista que NO existe ('Z')
    arista_inexistente = eliminar_arista(vertice_a, 'Z')
    print(f"Resultado al eliminar 'Z': {arista_inexistente}")

print("\n--- Grafo después de eliminar ---")
g.show()