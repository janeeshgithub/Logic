def find(grid, start, end):
    r, c = len(grid), len(grid[0])
    p = []
    v = [[False] * c for _ in range(r)]

    # Correct the direction mapping
    dm = {(-1, 0): "U", (1, 0): "D", (0, -1): "L", (0, 1): "R"}

    def dfs(x, y, cp):
        if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == 0 or v[x][y]:
            return

        # If we reach the destination, add the path
        if (x, y) == end:
            p.append("".join(cp))

        v[x][y] = True

        # Directions to move: Up, Down, Left, Right
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Explore each direction
        for dr, dc in d:
            nx, ny = x + dr, y + dc
            dfs(nx, ny, cp + [dm[(dr, dc)]])

        # Backtrack
        v[x][y] = False

    # Start DFS from the start point
    dfs(start[0], start[1], [])
    return p


# Example grid: 1 is path, 0 is wall
grid = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

start = (0, 0)  # Starting point
end = (3, 3)  # Ending point

# Find all paths
paths = find(grid, start, end)

# Sort paths by length and print the result
paths.sort(key=len)
print(len(paths))  # Number of valid paths
for path in paths:
    print(path)  # Print each path
