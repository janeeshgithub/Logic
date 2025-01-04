# Define the matrix
matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 0]
]
rows, cols = len(matrix), len(matrix[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = set()

def dfs(row, col):
    # Check if the current cell is out of bounds or already visited or is water (0)
    if (row < 0 or row >= rows or col < 0 or col >= cols or
            (row, col) in visited or matrix[row][col] == 0):
        return
    visited.add((row, col))
    print(f"Visited cell ({row}, {col})")

    for dr, dc in directions:
        dfs(row + dr, col + dc)


dfs(0, 0)
