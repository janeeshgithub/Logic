
def countUnguarded(self, rows, cols, guards, walls):
    # Initialize the grid
    grid = [[0] * cols for _ in range(rows)]
    for r, c in guards:
        grid[r][c] = 2  # Mark guards
    for r, c in walls:
        grid[r][c] = 1  # Mark walls

    # Directions for traversal: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Mark cells visible to guards
    for r, c in guards:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in (1, 2):
                if grid[nr][nc] == 0:
                    grid[nr][nc] = -1  # Mark as seen
                nr += dr
                nc += dc

    # Count unguarded cells (remaining 0s)
    return sum(cell == 0 for row in grid for cell in row)
