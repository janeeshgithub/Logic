class Solution(object):
    def solveSudoku(self, board):
        def iss(g, r, c, n):
            if any(g[i][c] == n or g[r][i] == n for i in range(9)):
                return False
            sr, sc = 3 * (r // 3), 3 * (c // 3)
            return all(g[i + sr][j + sc] != n for i in range(3) for j in range(3))

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for i in range(1, 10):
                            n = chr(i + ord('0'))
                            if iss(board, r, c, n):
                                board[r][c] = n
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()

# Main function to test the solveSudoku method
def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", ".", ".", ".", "7", "9"]
    ]

    solver = Solution()
    solver.solveSudoku(board)

    # Print the solved board
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    main()
