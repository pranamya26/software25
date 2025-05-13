import sys

def prims_algorithm(graph):
    num_nodes = len(graph)
    selected = [False] * num_nodes
    key = [sys.maxsize] * num_nodes
    parent = [-1] * num_nodes

    key[0] = 0  # Start from node 0

    for _ in range(num_nodes):
        min_key = sys.maxsize
        u = -1
        for v in range(num_nodes):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True

        for v in range(num_nodes):
            if graph[u][v] and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print MST
    print("Edge \tWeight")
    for i in range(1, num_nodes):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

# Define the graph
graph = [
    [0, 2, 3, 0, 0],
    [2, 0, 4, 6, 5],
    [3, 4, 0, 0, 7],
    [0, 6, 0, 0, 8],
    [0, 5, 7, 8, 0]
]

prims_algorithm(graph)

# Disjoint Set (Union-Find) utility
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False  # Cycle
        self.parent[v_root] = u_root
        return True

def kruskal_algorithm(num_nodes, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(num_nodes)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
            if len(mst) == num_nodes - 1:
                break

    print("Edge \tWeight")
    for u, v, w in mst:
        print(f"{u} - {v} \t{w}")
    print("Total Cost of MST:", total_cost)

# Edges from the graph (u, v, weight)
edges = [
    (0, 1, 2),
    (0, 2, 3),
    (1, 2, 4),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 8)
]

kruskal_algorithm(5, edges)
