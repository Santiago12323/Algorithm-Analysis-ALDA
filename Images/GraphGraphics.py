import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(edges, title):
    """
    Genera un PNG del grafo usando NetworkX + Matplotlib

    Complejidad:
    - Construcción del grafo: O(E)
    - Layout (spring_layout): O(V + E)
    """

    G = nx.DiGraph()

    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1200,
        font_size=10,
        arrows=True
    )

    edge_labels = {(u, v): w for u, v, w in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    filename = title.lower().replace(" ", "_").replace(":", "") + ".png"
    plt.title(title)
    plt.savefig(filename, bbox_inches="tight")
    plt.close()

    print(f"[✓] PNG generado: {filename}")



def get_graph_cases():
    cases = {}

    # CASO 1: Grafo pequeño (DAG)
    cases[1] = {
        "name": "Grafo pequeño DAG",
        "edges": [
            (0, 1, 4), (0, 2, 1), (2, 1, 2),
            (1, 3, 1), (2, 3, 5), (3, 4, 3)
        ]
    }

    # CASO 2: Pesos negativos (sin ciclo negativo)
    cases[2] = {
        "name": "Pesos negativos",
        "edges": [
            (0, 1, 2), (0, 2, 4),
            (1, 2, -2), (1, 3, 2),
            (2, 3, 3), (3, 4, 2)
        ]
    }

    # CASO 3: Grafo con ciclos
    cases[3] = {
        "name": "Grafo con ciclos",
        "edges": [
            (0, 1, 2), (1, 2, 3), (2, 3, 1),
            (3, 1, 1), (3, 4, 5), (4, 5, 2)
        ]
    }

    # CASO 4: Grafo grande y disperso (NO dibujar)
    edges_sparse = []
    for i in range(49):
        edges_sparse.append((i, i + 1, 1))
        if i + 2 < 50:
            edges_sparse.append((i, i + 2, 2))

    cases[4] = {
        "name": "Grafo grande disperso",
        "edges": edges_sparse
    }

    edges_dense = []
    for u in range(20):
        for v in range(20):
            if u != v:
                edges_dense.append((u, v, (u + v) % 5 + 1))

    cases[5] = {
        "name": "Grafo denso",
        "edges": edges_dense
    }

    return cases


def main():
    cases = get_graph_cases()

    print("\nSeleccione el grafo a generar (PNG):")
    print("1 → Grafo pequeño (DAG)")
    print("2 → Pesos negativos")
    print("3 → Grafo con ciclos")
    print("4 → Grafo grande (omitido)")
    print("5 → Grafo denso")
    print("0 → Generar TODOS menos el 4")

    option = int(input("\nOpción: "))

    if option == 0:
        for i in cases:
            if i != 4:
                draw_graph(
                    cases[i]["edges"],
                    f"CASO {i}: {cases[i]['name']}"
                )
    elif option in cases:
        if option == 4:
            print("⚠️ El grafo 4 es muy grande y se omite automáticamente.")
        else:
            draw_graph(
                cases[option]["edges"],
                f"CASO {option}: {cases[option]['name']}"
            )
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()
