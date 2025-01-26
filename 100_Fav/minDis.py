class Solution(object):
    def minDistance(self, word1, word2):
        mem = {}

        def rec(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if (i, j) in mem:
                return mem[(i, j)]
            if word1[i] == word2[j]:
                mem[(i, j)] = 0 + rec(i - 1, j - 1)
                return mem[(i, j)]
            else:
                mem[(i, j)] = 1 + min(rec(i - 1, j - 1), rec(i - 1, j), rec(i, j - 1))
                return mem[(i, j)]

        return rec(len(word1) - 1, len(word2) - 1)


class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        # Create a DP table where dp[i][j] represents the minimum edit distance
        # between word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the base cases
        for i in range(m + 1):
            dp[i][0] = i  # Transforming prefix of word1 to an empty string
        for j in range(n + 1):
            dp[0][j] = j  # Transforming empty string to prefix of word2

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    # Take the minimum of replace, insert, or delete operation
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # Replace
                        dp[i - 1][j],  # Delete
                        dp[i][j - 1]  # Insert
                    )

        # The result is the edit distance between the entire strings
        return dp[m][n]
