class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]


def largestIsland(grid):
    ROWS, COLS = len(grid), len(grid[0])
    uf = UnionFind(ROWS * COLS)

    def index(r, c):
        return r * COLS + c

    # Step 1: Union adjacent 1's in the grid.
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    uf.union(index(r, c), index(r + 1, c))
                if c + 1 < COLS and grid[r][c + 1] == 1:
                    uf.union(index(r, c), index(r, c + 1))

    # Step 2: Calculate the size of each island
    island_sizes = {}
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                root = uf.find(index(r, c))
                if root not in island_sizes:
                    island_sizes[root] = uf.size[root]

    # Step 3: Try flipping each 0 and calculating the largest possible island size
    max_island_size = max(island_sizes.values(), default=0)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                # Track the unique neighbors of 1's
                neighboring_islands = set()
                potential_size = 1  # Start with flipping the current 0 to 1

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                        root = uf.find(index(nx, ny))
                        if root not in neighboring_islands:
                            potential_size += island_sizes.get(root, 0)
                            neighboring_islands.add(root)

                max_island_size = max(max_island_size, potential_size)

    return max_island_size


# Example usage:
grid = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]

print(largestIsland(grid))  # Output will be the size of the largest possible island after flipping one 0
