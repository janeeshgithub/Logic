class Solution:
    def maxChoc(self, i, j1, j2, n, m, grid, dp):
        # Base cases
        # If either robot goes out of bounds, return a very negative value (invalid case)
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return float('-inf')

        # If we are at the last row, the robots collect chocolates
        # If both robots are in the same column, only count it once
        if i == n - 1:
            return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]

        # Memoization check: If already computed, return the stored result
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        # Initialize maximum chocolates collected for this state
        maxi = float('-inf')

        # Try all possible moves for both robots
        # Robot 1 moves to j1 + di, Robot 2 moves to j2 + dj
        for di in range(-1, 2):  # Robot 1 can move left, stay, or move right
            for dj in range(-1, 2):  # Robot 2 can move left, stay, or move right
                # If both robots are in the same column, count chocolates only once
                chocolates = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]

                # Add chocolates collected from the next row (recursive call)
                chocolates += self.maxChoc(i + 1, j1 + di, j2 + dj, n, m, grid, dp)

                # Update the maximum chocolates collected
                maxi = max(maxi, chocolates)

        # Store the result in the memoization table
        dp[i][j1][j2] = maxi
        return maxi

    def solve(self, n, m, grid):
        # Initialize a 3D memoization table with -1 (not computed states)
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]

        # Start the recursion from the first row, with robots at columns 0 and m-1
        return self.maxChoc(0, 0, m - 1, n, m, grid, dp)
