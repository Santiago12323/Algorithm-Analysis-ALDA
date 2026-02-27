def bellman_ford(graph, start):
    """
    Bellman-Ford Algorithm

    Normal case (not very dense graph):
    - Initialize distances and predecessors: O(V)
    - Iterate over every node and its edges V-1 times: O(V * E)
    - Check for negative cycles: O(V * E)
    - Total dominant complexity: O(V * E)
    - In general: O(n^2)

    Special case (very dense graph, almost all connections present):
    - Number of edges E ≈ V^2
    - Total approximate complexity: O(V^3)

    Space complexity: O(V)
    """

    # Initialize distances and predecessors
    # V = number of vertices
    dist = {v: float("inf") for v in range(graph.V)}  # O(V)
    prev = {v: None for v in range(graph.V)}          # O(V)

    dist[start] = 0  # O(1)

    # Main step: relax edges V-1 times
    for _ in range(graph.V - 1):                      # O(V)
        for u in range(graph.V):                      # O(V)
            for v, w in graph.adj[u]:                 # O(E total across all nodes)
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w             # O(1)
                    prev[v] = u                       # O(1)

    # Negative cycle detection
    for u in range(graph.V):                          # O(V)
        for v, w in graph.adj[u]:                     # O(E)
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                raise ValueError("The graph contains a negative weight cycle")

    # -------------------------
    # Step-by-step analysis:
    # 1. Distance and predecessor initialization: O(V) + O(V) = O(V)
    # 2. Main loops:
    #    - Repeat V-1 times: O(V)
    #    - Traverse all nodes: O(V)
    #    - Traverse all edges of each node: O(E)
    #    → Total loops = O(V) * O(E) = O(V * E)
    # 3. Negative cycle check: O(V * E)
    # Total = O(V * E)
    # General = O(n^2)
    # -------------------------
    # Normal case: sparse graphs → E << V^2 → O(V * E)
    # Special case: dense graphs → E ≈ V^2 → O(V^3)

    return dist, prev


def get_shortest_path(prev, start, end):
    """
    Reconstructs the shortest path
    Time complexity: O(V)
    """
    path = []
    cur = end

    while cur is not None:
        path.append(cur)
        cur = prev[cur]

    path.reverse()

    if path and path[0] == start:
        return path
    return []