def floyd_warshall(graph):
    """
    Floyd–Warshall

    Notación:
    - V: número de vértices del grafo

    Caso normal (grafo no muy lleno):
    - Inicializa la matriz de distancias y la matriz de seguimiento: O(V^2)
    - Llena las distancias directas de cada arista: O(E)
    - Algoritmo principal: tres bucles anidados sobre V → O(V^3)
    - Complejidad total dominante: O(V^3)

    Caso especial (grafo muy grande o denso):
    - Igual que el caso normal, ya que la complejidad depende solo de V
    - Complejidad dominante: O(V^3)

    Complejidad espacial: O(V^2)
    """

    INF = float("inf") #O(1)
    V = graph.V #O(1)

    # Inicializa matrices de distancia y seguimiento
    dist = [[INF] * V for _ in range(V)]        # O(V^2)
    next_node = [[None] * V for _ in range(V)] # O(V^2)

    for i in range(V):                          # O(V)
        dist[i][i] = 0

    # Coloca las distancias directas de las aristas
    for u in range(V):                          # O(V)
        for v, w in graph.adj[u]:               # O(E total sobre todos los nodos)
            dist[u][v] = w
            next_node[u][v] = v

    # Algoritmo principal: prueba todos los nodos intermedios k
    for k in range(V):                          # O(V)
        for i in range(V):                      # O(V)
            for j in range(V):                  # O(V)
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # -------------------------
    # Análisis paso a paso:
    # 1. Inicialización de matrices: O(V^2) + O(V^2) = O(V^2)
    # 2. Colocar distancias directas de aristas: O(E)
    # 3. Bucle principal de Floyd–Warshall (tres bucles anidados): O(V^3)
    # -------------------------
    # Caso normal y caso especial: O(V^3) domina
    # Espacio: dos matrices VxV → O(V^2)
    return dist, next_node



def get_shortest_path_fw(next_node, start, end):
    """
    Reconstruye el camino entre start y end
    Complejidad temporal: O(V)
    """
    if next_node[start][end] is None:
        return []

    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)

    return path
