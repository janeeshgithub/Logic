from collections import deque


def rabbit_maze(grid, start, target):
    """
    Check if the rabbit can reach the target in the maze.
    Args:
        grid: 2D list representing the maze.
        start: Tuple (x, y) for the starting position.
        target: Tuple (x, y) for the target position.
    Returns:
        True if the rabbit can reach the target, otherwise False.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0

    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))

    return False


# Example Usage
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]
start = (0, 0)
target = (3, 3)
result = rabbit_maze(maze, start, target)
print(f"Can the rabbit reach the target? {result}")
