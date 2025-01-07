class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def largestIsland(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    n = rows * cols
    disjoint_set = DisjointSet(n)

    def index(r, c):
        return r * cols + c
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r + 1 < rows and grid[r + 1][c] == 1:
                    disjoint_set.union(index(r, c), index(r + 1, c))
                if c + 1 < cols and grid[r][c + 1] == 1:
                    disjoint_set.union(index(r, c), index(r, c + 1))

    # Count the size of each island by finding the root of each cell
    island_size = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                root = disjoint_set.find(index(r, c))
                if root in island_size:
                    island_size[root] += 1
                else:
                    island_size[root] = 1

    # The largest island will have the maximum size
    return max(island_size.values(), default=0)


# Example usage:
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0]
]

print(largestIsland(grid))  # Output will be the area of the largest island
