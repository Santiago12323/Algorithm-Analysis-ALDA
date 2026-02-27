def floyd_warshall(graph):
    """
    Floyd–Warshall Algorithm

    Notation:
    - V: number of vertices in the graph

    Normal case (not very dense graph):
    - Initialize distance matrix and path matrix: O(V^2)
    - Fill direct edge distances: O(E)
    - Main algorithm: three nested loops over V → O(V^3)
    - Dominant total complexity: O(V^3)

    Special case (very large or dense graph):
    - Same as normal case, since complexity depends only on V
    - Dominant complexity: O(V^3)

    Space complexity: O(V^2)
    """

    INF = float("inf")  # O(1)
    V = graph.V         # O(1)

    # Initialize distance and path matrices
    dist = [[INF] * V for _ in range(V)]         # O(V^2)
    next_node = [[None] * V for _ in range(V)]   # O(V^2)

    for i in range(V):                           # O(V)
        dist[i][i] = 0

    # Set direct edge distances
    for u in range(V):                           # O(V)
        for v, w in graph.adj[u]:                # O(E total across all nodes)
            dist[u][v] = w
            next_node[u][v] = v

    # Main algorithm: try all intermediate nodes k
    for k in range(V):                           # O(V)
        for i in range(V):                       # O(V)
            for j in range(V):                   # O(V)
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # -------------------------
    # Step-by-step analysis:
    # 1. Matrix initialization: O(V^2) + O(V^2) = O(V^2)
    # 2. Set direct edge distances: O(E)
    # 3. Main Floyd–Warshall loop (three nested loops): O(V^3)
    # -------------------------
    # Normal and special case: O(V^3) dominates
    # Space: two VxV matrices → O(V^2)

    return dist, next_node


def get_shortest_path_fw(next_node, start, end):
    """
    Reconstructs the path between start and end
    Time complexity: O(V)
    """
    if next_node[start][end] is None:
        return []

    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)

    return path