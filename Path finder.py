def is_valid(x, y, matrix, visited):
    return (0 <= x < len(matrix) and
            0 <= y < len(matrix[0]) and
            matrix[x][y] == 1 and
            not visited[x][y])

def find_path(matrix, x, y, end_x, end_y, path, visited):
    if (x, y) == (end_x, end_y):
        path.append((x, y))
        return True 
    visited[x][y] = True
    path.append((x, y))

    # Possible directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, matrix, visited):
            if find_path(matrix, new_x, new_y, end_x, end_y, path, visited):
                return True

    path.pop()  # Backtrack if no path is found
    visited[x][y] = False
    return False


def main():
    matrix = [
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]

    start = (0, 0)  # Starting point
    end = (3, 3)  # Ending point
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    path = []

    if find_path(matrix, start[0], start[1], end[0], end[1], path, visited):
        print("Path found:", path)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
