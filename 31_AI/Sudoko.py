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


def solveSudoku(self, mat):
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    box_set = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if mat[i][j] != 0:
                row_set[i].add(mat[i][j])
                col_set[j].add(mat[i][j])
                box_set[(i//3)*3 + j//3].add(mat[i][j])

    def backtrack(r, c):
        if r == 9:
            return True
        if c == 9:
            return backtrack(r + 1, 0)
        if mat[r][c] != 0:
            return backtrack(r, c + 1)

        b = (r//3)*3 + c//3
        for k in range(1, 10):
            if k not in row_set[r] and k not in col_set[c] and k not in box_set[b]:
                mat[r][c] = k
                row_set[r].add(k)
                col_set[c].add(k)
                box_set[b].add(k)

                if backtrack(r, c + 1):
                    return True

                mat[r][c] = 0
                row_set[r].remove(k)
                col_set[c].remove(k)
                box_set[b].remove(k)

        return False

    backtrack(0, 0)
    return mat
