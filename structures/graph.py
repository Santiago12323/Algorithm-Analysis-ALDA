class Graph:
    def __init__(self, n, directed=True):
        self.V = n
        self.directed = directed
        self.adj = {i: [] for i in range(n)}

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))

    def __str__(self):
        lines = []
        lines.append("GRAFO")
        lines.append("=" * 35)

        for u in range(self.V):
            lines.append(f"[{u}]")
            if not self.adj[u]:
                lines.append("   └── sin aristas")
            else:
                for i, (v, w) in enumerate(self.adj[u]):
                    connector = "└──" if i == len(self.adj[u]) - 1 else "├──"
                    lines.append(f"   {connector} [{u}] --{w}--> [{v}]")

        return "\n".join(lines)
