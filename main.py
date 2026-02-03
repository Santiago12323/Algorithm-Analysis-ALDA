import time

from structures.graph import Graph
from shortest_path import (
    dijkstra,
    bellman_ford,
    floyd_warshall,
    get_shortest_path,
    get_shortest_path_fw
)
from shortest_path.johnson import johnson
from shortest_path.dag_shortest_path import dag_shortest_path


def run_experiment(name, g, source, target):
    print("=" * 70)
    print(f"GRAFO: {name}")
    print(f"Ruta más corta: nodo {source} → nodo {target}")
    print("=" * 70)
    print(g)
    print()

    # ==========================
    # DIJKSTRA
    # ==========================
    start = time.perf_counter()
    dist_dij, prev_dij = dijkstra(g, source)
    t_dij = time.perf_counter() - start
    path_dij = get_shortest_path(prev_dij, source, target)

    # ==========================
    # BELLMAN-FORD
    # ==========================
    start = time.perf_counter()
    dist_bell, prev_bell = bellman_ford(g, source)
    t_bell = time.perf_counter() - start
    path_bell = get_shortest_path(prev_bell, source, target)

    # ==========================
    # FLOYD–WARSHALL
    # ==========================
    start = time.perf_counter()
    dist_fw, next_fw = floyd_warshall(g)
    t_fw = time.perf_counter() - start
    path_fw = get_shortest_path_fw(next_fw, source, target)

    # ==========================
    # JOHNSON
    # ==========================
    start = time.perf_counter()
    dist_john, prev_john = johnson(g)
    t_john = time.perf_counter() - start
    path_john = get_shortest_path(prev_john[source], source, target)

    # ==========================
    # DAG SHORTEST PATH
    # ==========================
    try:
        start = time.perf_counter()
        dist_dag, prev_dag = dag_shortest_path(g, source)
        t_dag = time.perf_counter() - start
        path_dag = get_shortest_path(prev_dag, source, target)
    except Exception:
        t_dag = 0
        dist_dag = {}
        path_dag = ["No aplica (no es DAG)"]

    # ==========================
    # RESULTADOS
    # ==========================
    print("Distancia mínima y recorrido:")
    print(f"  Dijkstra        : {dist_dij[target]}  {path_dij}")
    print(f"  Bellman-Ford    : {dist_bell[target]}  {path_bell}")
    print(f"  Floyd-Warshall  : {dist_fw[source][target]}  {path_fw}")
    print(f"  Johnson         : {dist_john[source][target]}  {path_john}")
    print(f"  DAG Shortest    : {dist_dag.get(target, 'N/A')}  {path_dag}")

    print("\nTiempos de ejecución:")
    print(f"  Dijkstra        : {t_dij:.6f} s")
    print(f"  Bellman-Ford    : {t_bell:.6f} s")
    print(f"  Floyd-Warshall  : {t_fw:.6f} s")
    print(f"  Johnson         : {t_john:.6f} s")
    print(f"  DAG Shortest    : {t_dag:.6f} s")
    print()


def main():

    # ==================================================
    # CASO 1: Grafo pequeño (DAG, pesos positivos)
    # ==================================================
    g_small = Graph(5)
    edges_small = [
        (0, 1, 4), (0, 2, 1), (2, 1, 2),
        (1, 3, 1), (2, 3, 5), (3, 4, 3)
    ]
    for u, v, w in edges_small:
        g_small.add_edge(u, v, w)

    # ==================================================
    # CASO 2: Grafo con pesos negativos (SIN ciclo negativo)
    # ==================================================
    g_negative = Graph(5)
    edges_negative = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 2, -2),  # peso negativo
        (1, 3, 2),
        (2, 3, 3),
        (3, 4, 2)
    ]
    for u, v, w in edges_negative:
        g_negative.add_edge(u, v, w)

    # ==================================================
    # CASO 3: Grafo con ciclos (NO DAG)
    # ==================================================
    g_cycle = Graph(6)
    edges_cycle = [
        (0, 1, 2), (1, 2, 3), (2, 3, 1),
        (3, 1, 1),  # ciclo
        (3, 4, 5), (4, 5, 2)
    ]
    for u, v, w in edges_cycle:
        g_cycle.add_edge(u, v, w)

    # ==================================================
    # CASO 4: Grafo grande y disperso
    # ==================================================
    g_sparse = Graph(50)
    for i in range(49):
        g_sparse.add_edge(i, i + 1, 1)
        if i + 2 < 50:
            g_sparse.add_edge(i, i + 2, 2)

    # ==================================================
    # CASO 5: Grafo denso
    # ==================================================
    g_dense = Graph(20)
    for u in range(20):
        for v in range(20):
            if u != v:
                g_dense.add_edge(u, v, (u + v) % 5 + 1)

    # ==========================
    # EJECUCIÓN
    # ==========================
    run_experiment("Pequeño (DAG)", g_small, 0, 4)
    run_experiment("Pesos negativos", g_negative, 0, 4)
    run_experiment("Con ciclos", g_cycle, 0, 5)
    run_experiment("Grande disperso", g_sparse, 0, 49)
    run_experiment("Denso", g_dense, 0, 19)


if __name__ == "__main__":
    main()
