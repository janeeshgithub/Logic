def search_in_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1, -1  # Return invalid indices for an empty matrix

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row, col  # Target found
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return -1, -1  # Target not found


# Example usage:
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5
result = search_in_matrix(matrix, target)
print(f"The position of {target} is: {result}")
