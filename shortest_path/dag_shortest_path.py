from collections import deque


def dag_shortest_path(graph, start):
    """
    Camino mínimo en DAG (Directed Acyclic Graph)

    Notación:
    - V: número de vértices
    - E: número de aristas

    Complejidad temporal:
    - Orden topológico: O(V + E)
    - Relajación de aristas: O(E)
    - Complejidad total: O(V + E)
    - aproximadamente O(2n)

    Complejidad espacial:
    - Distancias + predecesores + indegree: O(V)
    """

    V = graph.V  # O(1)

    indegree = {v: 0 for v in range(V)}  # O(V)

    for u in range(V):                   # O(V)
        for v, _ in graph.adj[u]:        # O(E)
            indegree[v] += 1             # O(1)

    # ==========================
    # 2. Orden topológico (Kahn)
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
    # 3. Inicializar distancias
    # ==========================
    dist = {v: float("inf") for v in range(V)}  # O(V)
    prev = {v: None for v in range(V)}          # O(V)
    dist[start] = 0                             # O(1)

    # ==========================
    # 4. Relajación de aristas
    # ==========================
    for u in topo:                       # O(V)
        if dist[u] != float("inf"):
            for v, w in graph.adj[u]:    # O(E)
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

    return dist, prev
