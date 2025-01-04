x = int(input())
mod = 10**9 + 7

# dp table of size (x+1) by 3, initialized to 0
dp = [[0] * 3 for _ in range(x + 1)]

# Base case: when i == x, only one valid way (all paths terminate)
dp[x] = [1, 1, 1]

# Fill the DP table from bottom to top
for i in range(x - 1, -1, -1):
    # Calculate dp[i][0], dp[i][1], dp[i][2] based on transitions
    dp[i][0] = (dp[i + 1][1] + dp[i + 1][0]) % mod
    dp[i][1] = dp[i + 1][2] % mod
    dp[i][2] = (dp[i + 1][2] + dp[i + 1][0]) % mod

# Output the result starting from dp[0][0]
print(dp[0][0])
