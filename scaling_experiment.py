import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from structures.graph import Graph
from shortest_path import dijkstra, bellman_ford, floyd_warshall
from shortest_path.johnson import johnson
from shortest_path.dag_shortest_path import dag_shortest_path



SIZES = [20, 40, 60, 80, 100]
REPEATS = 3


def generate_sparse_graph(n):
    g = Graph(n)

    for i in range(n - 1):
        g.add_edge(i, i + 1, random.randint(1, 10))

    extra_edges = n
    for _ in range(extra_edges):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            g.add_edge(u, v, random.randint(1, 10))

    return g


def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start


def run_scaling_experiment():

    results = []

    for n in SIZES:
        print(f"\nProbando tamaño: {n}")

        for _ in range(REPEATS):

            g = generate_sparse_graph(n)
            source = 0

            t = measure_time(dijkstra, g, source)
            results.append(("Dijkstra", n, t))

            t = measure_time(bellman_ford, g, source)
            results.append(("Bellman-Ford", n, t))


            t = measure_time(floyd_warshall, g)
            results.append(("Floyd-Warshall", n, t))

            t = measure_time(johnson, g)
            results.append(("Johnson", n, t))


            try:
                t = measure_time(dag_shortest_path, g, source)
                results.append(("DAG Shortest", n, t))
            except:
                pass

    # Crear DataFrame
    df = pd.DataFrame(results, columns=["Algorithm", "Nodes", "Time"])

    # Promedio por tamaño
    df = df.groupby(["Algorithm", "Nodes"]).mean().reset_index()

    df.to_csv("scaling_results.csv", index=False)

    return df


def plot_results(df):

    plt.figure(figsize=(10, 6))

    sns.lineplot(data=df, x="Nodes", y="Time", hue="Algorithm", marker="o")

    plt.title("Crecimiento Experimental - Shortest Path Algorithms")
    plt.xlabel("Número de nodos (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":

    df = run_scaling_experiment()
    plot_results(df)
