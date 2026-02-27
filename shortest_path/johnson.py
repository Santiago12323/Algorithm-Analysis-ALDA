from shortest_path import dijkstra, bellman_ford
from structures.graph import Graph


def johnson(g: Graph):
    """
    Johnson's Algorithm

    Notation:
    - V: number of vertices in the graph
    - E: number of edges in the graph

    Normal case (sparse graph):
    - Bellman-Ford runs once: O(V * E)
    - Dijkstra runs V times: O(V * (V + E) log V)
    - Dominant total complexity:
        O(V * E + V * (V + E) log V) = O(V · E log V)

    Special case (very dense graph):
    - E ≈ V^2
    - Approximate complexity:
        O(V^3 log V)

    Space complexity:
    - Stores distances for all pairs of nodes: O(V^2)
    - Auxiliary graphs and structures: O(V + E)
    - Total space complexity: O(V^2)
    """

    V = g.V  # O(1)

    g_ext = Graph(V + 1, directed=True)  # O(V)

    # Copy original edges into extended graph
    for u in range(V):                   # O(V)
        for v, w in g.adj[u]:            # O(E)
            g_ext.add_edge(u, v, w)      # O(1)

    # Add artificial node q connected to all nodes
    q = V
    for v in range(V):                   # O(V)
        g_ext.add_edge(q, v, 0)          # O(1)

    # ==========================
    # Bellman-Ford from q
    # ==========================
    # Time complexity: O(V * E)
    # Space complexity: O(V)
    h, _ = bellman_ford(g_ext, q)

    # ==========================
    # Reweight edges
    # ==========================
    # Create new graph with non-negative weights
    g_rw = Graph(V, directed=True)        # O(V)

    for u in range(V):                   # O(V)
        for v, w in g.adj[u]:            # O(E)
            w_new = w + h[u] - h[v]      # O(1)
            g_rw.add_edge(u, v, w_new)   # O(1)

    # ==========================
    # Run Dijkstra from each node
    # ==========================
    dist = {}    # Final distance dictionary
    prev = {}    # Predecessor dictionary

    for u in range(V):                   # O(V)

        # Complexity: O((V + E) log V)
        d_rw, p = dijkstra(g_rw, u)

        dist[u] = {}
        prev[u] = p

        for v in range(V):               # O(V)
            if d_rw[v] < float("inf"):
                dist[u][v] = d_rw[v] - h[u] + h[v]  # O(1)
            else:
                dist[u][v] = float("inf")

    # ==========================
    # Final Analysis:
    # ==========================
    # - Create auxiliary graphs: O(V + E)
    # - Bellman-Ford: O(V * E)
    # - Dijkstra V times: O(V * (V + E) log V)
    # - Final distance adjustment: O(V^2)
    #
    # Dominant total time complexity:
    #   O(V * E + V * (V + E) log V)
    # approximately = O(3n^2) in simplified terms
    #
    # Total space complexity:
    #   O(V^2)
    # ==========================

    return dist, prev