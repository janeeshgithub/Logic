def helper(g, r, c, k):
    for i in range(9):
        if g[i][c] == k or g[r][i] == k:
            return False
        if g[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
            return False
    return True

def sudoku(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == "0":  
                for k in "123456789": 
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
g[0][0] = "5"

# Solve the Sudoku
a, b = sudoku(g)
for i in b:
    print(i)  # Prints the solved grid

