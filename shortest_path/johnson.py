from shortest_path import dijkstra, bellman_ford
from structures.graph import Graph


def johnson(g: Graph):
    """
    Algoritmo de Johnson

    Notación:
    - V: número de vértices del grafo
    - E: número de aristas del grafo

    Caso normal (grafo disperso):
    - Bellman-Ford se ejecuta una sola vez: O(V * E)
    - Dijkstra se ejecuta V veces: O(V * (V + E) log V)
    - Complejidad total dominante:
        O(V * E + V * (V + E) log V) = O(V · E log V)

    Caso especial (grafo muy denso):
    - E ≈ V^2
    - Complejidad aproximada:
        O(V^3 log V)

    Complejidad espacial:
    - Almacena distancias para todos los pares de nodos: O(V^2)
    - Grafos auxiliares y estructuras: O(V + E)
    - Complejidad espacial total: O(V^2)
    """

    V = g.V  # O(1)

    g_ext = Graph(V + 1, directed=True)  # O(V)


    for u in range(V):                   # O(V)
        for v, w in g.adj[u]:            # O(E)
            g_ext.add_edge(u, v, w)      # O(1)

    # Nodo ficticio q conectado a todos los nodos
    q = V
    for v in range(V):                   # O(V)
        g_ext.add_edge(q, v, 0)          # O(1)

    # ==========================
    # Bellman-Ford desde q
    # ==========================
    # Complejidad temporal: O(V * E)
    # Complejidad espacial: O(V)
    h, _ = bellman_ford(g_ext, q)

    # ==========================
    # Reponderar aristas
    # ==========================
    # Se crea un nuevo grafo con pesos no negativos
    g_rw = Graph(V, directed=True)        # O(V)

    for u in range(V):                   # O(V)
        for v, w in g.adj[u]:            # O(E)
            w_new = w + h[u] - h[v]      # O(1)
            g_rw.add_edge(u, v, w_new)   # O(1)

    # ==========================
    # Dijkstra desde cada nodo
    # ==========================
    dist = {}    # Diccionario de distancias finales
    prev = {}    # Diccionario de predecesores

    for u in range(V):                   # O(V)

        # Complejidad: O((V + E) log V)
        d_rw, p = dijkstra(g_rw, u)

        dist[u] = {}
        prev[u] = p

        for v in range(V):               # O(V)
            if d_rw[v] < float("inf"):
                dist[u][v] = d_rw[v] - h[u] + h[v]  # O(1)
            else:
                dist[u][v] = float("inf")

    # ==========================
    # Análisis final:
    # ==========================
    # - Crear grafos auxiliares: O(V + E)
    # - Bellman-Ford: O(V * E)
    # - Dijkstra V veces: O(V * (V + E) log V)
    # - Ajuste final de distancias: O(V^2)
    #
    # Complejidad temporal total dominante:
    #   O(V * E + V * (V + E) log V)
    # aproximadamente = O(3n ^ 2)
    #
    # Complejidad espacial total:
    #   O(V^2)
    # ==========================

    return dist, prev
