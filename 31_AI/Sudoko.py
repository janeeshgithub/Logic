def helper(g, r, c, k):
    # Check the row and column for the same number
    for i in range(9):
        if g[i][c] == k or g[r][i] == k:
            return False
        # Check the 3x3 subgrid for the same number
        if g[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
            return False
    return True

def sudoku(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == "0":  # Found an empty cell
                for k in "123456789":  # Try numbers 1 to 9
                    if helper(g, i, j, k):  # Check if the number is valid
                        g[i][j] = k  # Place the number
                        if sudoku(g)[0]:  # Recursively solve the rest of the grid
                            return True, g  # Return the grid if it's solved
                        else:
                            g[i][j] = "0"  # Backtrack if not valid
                return False, []  # No solution possible for this configuration
    return True, g  # Return the solved grid

# Example Sudoku grid (filled with zeros for testing)
g = [["0"] * 9 for _ in range(9)]

# Solve the Sudoku
a, b = sudoku(g)
for i in b:
    print(i)  # Prints the solved grid
