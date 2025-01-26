s="ab"
p="**"
m, n = len(s), len(p)
# dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
dp = [[False] * (n + 1) for _ in range(m + 1)]
dp[0][0] = True  # Empty string matches empty pattern
# Handle patterns that start with '*' (can match empty string)
for j in range(1, n + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 1]
# Fill the DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s[i - 1] == p[j - 1] or p[j - 1] == '?':
            dp[i][j] = dp[i - 1][j - 1]
        elif p[j - 1] == '*':
            dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
print(dp[m][n])
