import heapq

def dijkstra(graph, start):
    """
    Dijkstra
    Complejidad temporal total: O((V + E) log V)
    Complejidad espacial total: O(V^2 log V)
    """

    # Diccionario de distancias para todos los vértices
    # Recorre V vértices
    dist = {v: float("inf") for v in range(graph.V)}  # O(V)


    # Diccionario de predecesores para reconstruir el camino
    # Recorre V vértices
    prev = {v: None for v in range(graph.V)}  # O(V)

    dist[start] = 0  # O(1)

    # Cola de prioridad
    pq = [(0, start)]  # O(1)

    # El while puede ejecutarse hasta O(E)
    # E siendo el número de aristas
    while pq:  # O(E)

        # Extracción del mínimo del heap
        current_dist, u = heapq.heappop(pq)  # O(log V)

        if current_dist > dist[u]:  # O(1)
            continue

        # Recorre los vecinos del nodo u
        # El ciclo depende de las aristas del nodo u
        for v, w in graph.adj[u]:  # O(grado(u))

            alt = dist[u] + w  # O(1)
            if alt < dist[v]:  # O(1)

                dist[v] = alt  # O(1)
                prev[v] = u    # O(1)

                heapq.heappush(pq, (alt, v))  # O(log V)

    # Análisis final:
    # Caso normal (grafo no tan lleno):
    # - Inicializa distancias y predecesores: O(V)
    # - Recorre todas las conexiones entre nodos: O(E)
    # - Cada vez que actualiza un camino usa la cola de prioridad: O(E log V)
    # - Complejidad total dominante: O((V + E) log V)
    # - osea O(n) log(n)

    # Caso especial (grafo muy lleno, casi todas las conexiones presentes):
    # - Como hay muchas conexiones (E ≈ V^2), el tiempo se aproxima a O(V^2 log V)


    return dist, prev



def get_shortest_path(prev, start, end):
    """
    Reconstruye el camino más corto usando el arreglo de predecesores
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
