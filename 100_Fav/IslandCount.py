from collections import deque
def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    def dfs(r,c):
        s=[]
        v[r][c]=True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while s:
            s
    def bfs(r, c):
        # Initialize a queue and add the starting point
        queue = deque([(r, c)])
        visited[r][c] = True

        # Explore all 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                # Check if the neighbor is within bounds and part of the island
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    island_count = 0

    # Iterate over all cells in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:  # Found an unvisited island
                bfs(r, c)  # Start BFS to mark the whole island
                island_count += 1  # Increment island count

    return island_count

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))  # Output: 3
