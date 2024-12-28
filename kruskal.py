class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n            # Rank array for union by rank

    def find(self, u):
        if self.parent[u] != u:
            # Path compression
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1  # Increment rank if both are of the same rank


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges


# Example usage
if __name__ == "__main__":
    n = 4  # Number of cities (nodes)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    cost, mst = kruskal(n, edges)
    print("Minimum Cost:", cost)
    print("Edges in MST:", mst)
