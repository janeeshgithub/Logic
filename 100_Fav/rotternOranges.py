from collections import deque

# Input the grid dimensions and grid data
rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

# Initialize variables
queue = deque()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
healthy_cells = 0
days = 0

# Populate the initial queue with all rotten cells and count healthy cells
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:  # Healthy cell
            healthy_cells += 1
        elif grid[i][j] == 2:  # Rotten cell
            queue.append((i, j))

# Add a delimiter to separate days
queue.append(None)

# Perform BFS to rot adjacent healthy cells
while queue:
    cell = queue.popleft()

    if cell is None:
        # End of a day
        if queue:
            days += 1
            queue.append(None)
        continue

    x, y = cell
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
            # Rot the healthy cell
            grid[nx][ny] = 2
            healthy_cells -= 1
            queue.append((nx, ny))

# Output the result
print(days if healthy_cells == 0 else -1)
