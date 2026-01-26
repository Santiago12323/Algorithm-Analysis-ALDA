def bellman_ford(graph, start):
    """
    Bellman-Ford

    Caso normal (grafo no muy lleno):
    - Inicializa distancias y predecesores: O(V)
    - Recorre cada nodo y todas sus aristas V-1 veces: O(V * E)
    - Verifica ciclos negativos: O(V * E)
    - Complejidad total dominante: O(V * E)
    - en general O(n^2)

    Caso especial (grafo muy lleno, casi todas las conexiones presentes):
    - Número de aristas E ≈ V^2
    - Complejidad total aproximada: O(V^3)

    Complejidad espacial: O(V)
    """

    # Inicializa distancias y predecesores
    # V = número de vértices
    dist = {v: float("inf") for v in range(graph.V)}  # O(V)
    prev = {v: None for v in range(graph.V)}           # O(V)

    dist[start] = 0  # O(1)

    # Paso principal: actualizar caminos V-1 veces
    for _ in range(graph.V - 1):                      # O(V)
        for u in range(graph.V):                      # O(V)
            for v, w in graph.adj[u]:                 # O(E total sobre todos los nodos)
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u]                 # O(1)
                    prev[v] = u                        # O(1)

    # Verificación de ciclos negativos
    for u in range(graph.V):                          # O(V)
        for v, w in graph.adj[u]:                     # O(E)
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                raise ValueError("El grafo contiene un ciclo de peso negativo")

    # -------------------------
    # Análisis paso a paso:
    # 1. Inicialización de distancias y predecesores: O(V) + O(V) = O(V)
    # 2. Bucles principales:
    #    - Repetición V-1 veces: O(V)
    #    - Recorre todos los nodos: O(V)
    #    - Recorre todas las aristas de cada nodo: O(E)
    #    → Total bucles = O(V) * O(E) = O(V * E)
    # 3. Verificación de ciclos negativos: O(V * E)
    # total = O(V * E)
    # general = O(n^2)
    # -------------------------
    # Caso normal: grafos dispersos → E << V^2 → O(V * E)
    # Caso especial: grafos densos → E ≈ V^2 → O(V^3)

    return dist, prev



def get_shortest_path(prev, start, end):
    """
    Reconstruye el camino más corto
    Complejidad temporal: O(V)
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
