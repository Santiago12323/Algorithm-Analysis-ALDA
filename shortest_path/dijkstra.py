import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm

    Total time complexity: O((V + E) log V)
    Total space complexity: O(V)
    """

    # Distance dictionary for all vertices
    # Iterates over V vertices
    dist = {v: float("inf") for v in range(graph.V)}  # O(V)

    # Predecessor dictionary to reconstruct the path
    # Iterates over V vertices
    prev = {v: None for v in range(graph.V)}  # O(V)

    dist[start] = 0  # O(1)

    # Priority queue (min-heap)
    pq = [(0, start)]  # O(1)

    # The while loop can execute up to O(E) times
    # E = number of edges
    while pq:  # O(E)

        # Extract minimum from heap
        current_dist, u = heapq.heappop(pq)  # O(log V)

        if current_dist > dist[u]:  # O(1)
            continue

        # Traverse neighbors of node u
        # Loop depends on the edges of node u
        for v, w in graph.adj[u]:  # O(degree(u))

            alt = dist[u] + w  # O(1)
            if alt < dist[v]:  # O(1)

                dist[v] = alt  # O(1)
                prev[v] = u    # O(1)

                heapq.heappush(pq, (alt, v))  # O(log V)

    # Final analysis:
    # Normal case (graph not very dense):
    # - Initialize distances and predecessors: O(V)
    # - Traverse all connections between nodes: O(E)
    # - Each path update uses the priority queue: O(E log V)
    # - Dominant total complexity: O((V + E) log V)
    # - That is O(n log n) in simplified terms

    # Special case (very dense graph, almost all connections present):
    # - Since there are many connections (E ≈ V^2),
    #   time complexity approaches O(V^2 log V)

    return dist, prev


def get_shortest_path(prev, start, end):
    """
    Reconstructs the shortest path using the predecessor array
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