import time

from structures.graph import Graph
from shortest_path import (
    dijkstra,
    bellman_ford,
    floyd_warshall,
    get_shortest_path,
    get_shortest_path_fw
)


def run_experiment(name, g, source, target):
    print("=" * 65)
    print(f"GRAFO: {name}")
    print(f"Ruta más corta: nodo {source} → nodo {target}")
    print("=" * 65)
    print(g)
    print()

    # ==========================
    # DIJKSTRA (solo cálculo)
    # ==========================
    start = time.perf_counter()
    dist_dij, prev_dij = dijkstra(g, source)
    t_dij = time.perf_counter() - start

    path_dij = get_shortest_path(prev_dij, source, target)

    # ==========================
    # BELLMAN-FORD (solo cálculo)
    # ==========================
    start = time.perf_counter()
    dist_bell, prev_bell = bellman_ford(g, source)
    t_bell = time.perf_counter() - start

    path_bell = get_shortest_path(prev_bell, source, target)

    # ==========================
    # FLOYD–WARSHALL (solo cálculo)
    # ==========================
    start = time.perf_counter()
    dist_fw, next_fw = floyd_warshall(g)
    t_fw = time.perf_counter() - start

    path_fw = get_shortest_path_fw(next_fw, source, target)

    # ==========================
    # RESULTADOS
    # ==========================
    print("Distancia mínima y recorrido:")
    print(f"  Dijkstra       ({source} → {target})")
    print(f"    Distancia = {dist_dij[target]}")
    print(f"    Camino    = {path_dij}")

    print(f"  Bellman-Ford   ({source} → {target})")
    print(f"    Distancia = {dist_bell[target]}")
    print(f"    Camino    = {path_bell}")

    print(f"  Floyd-Warshall ({source} → {target})")
    print(f"    Distancia = {dist_fw[source][target]}")
    print(f"    Camino    = {path_fw}")

    print()
    print("Tiempos de ejecución (solo cálculo del algoritmo):")
    print(f"  Dijkstra       : {t_dij:.6f} s")
    print(f"  Bellman-Ford   : {t_bell:.6f} s")
    print(f"  Floyd-Warshall : {t_fw:.6f} s")
    print()


def main():
    # -------- Grafo pequeño --------
    g_small = Graph(5)
    g_small.add_edge(0, 1, 4)
    g_small.add_edge(0, 2, 1)
    g_small.add_edge(2, 1, 2)
    g_small.add_edge(1, 3, 1)
    g_small.add_edge(2, 3, 5)
    g_small.add_edge(3, 4, 3)

    # -------- Grafo mediano --------
    g_medium = Graph(8)
    edges_medium = [
        (0, 1, 3), (0, 2, 6), (1, 3, 4), (2, 3, 2),
        (3, 4, 5), (4, 5, 1), (5, 6, 2), (6, 7, 3),
        (2, 5, 7), (1, 6, 6)
    ]
    for u, v, w in edges_medium:
        g_medium.add_edge(u, v, w)

    # -------- Grafo grande --------
    g_large = Graph(12)
    edges_large = [
        (0, 1, 2), (0, 2, 4), (1, 3, 7), (2, 3, 1),
        (3, 4, 3), (4, 5, 2), (5, 6, 6), (6, 7, 1),
        (7, 8, 5), (8, 9, 2), (9, 10, 4), (10, 11, 3),
        (1, 6, 8), (2, 7, 9), (3, 9, 10)
    ]
    for u, v, w in edges_large:
        g_large.add_edge(u, v, w)

    run_experiment("Pequeño (5 nodos)", g_small, 0, 4)
    run_experiment("Mediano (8 nodos)", g_medium, 0, 7)
    run_experiment("Grande (12 nodos)", g_large, 0, 11)


if __name__ == "__main__":
    main()
