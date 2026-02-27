from collections import deque


def dag_shortest_path(graph, start):
    """
    Shortest Path in a DAG (Directed Acyclic Graph)

    Notation:
    - V: number of vertices
    - E: number of edges

    Time complexity:
    - Topological sort: O(V + E)
    - Edge relaxation: O(E)
    - Total complexity: O(V + E)
    - Approximately O(2n)

    Space complexity:
    - Distances + predecessors + indegree: O(V)
    """

    V = graph.V  # O(1)

    indegree = {v: 0 for v in range(V)}  # O(V)

    for u in range(V):                   # O(V)
        for v, _ in graph.adj[u]:        # O(E)
            indegree[v] += 1             # O(1)

    # ==========================
    # 2. Topological Sort (Kahn's Algorithm)
    # ==========================
    q = deque()
    for v in range(V):                   # O(V)
        if indegree[v] == 0:
            q.append(v)

    topo = []
    while q:                             # O(V)
        u = q.popleft()                  # O(1)
        topo.append(u)
        for v, _ in graph.adj[u]:        # O(E)
            indegree[v] -= 1             # O(1)
            if indegree[v] == 0:
                q.append(v)

    # ==========================
    # 3. Initialize distances
    # ==========================
    dist = {v: float("inf") for v in range(V)}  # O(V)
    prev = {v: None for v in range(V)}          # O(V)
    dist[start] = 0                             # O(1)

    # ==========================
    # 4. Edge Relaxation
    # ==========================
    for u in topo:                       # O(V)
        if dist[u] != float("inf"):
            for v, w in graph.adj[u]:    # O(E)
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

    return dist, prev