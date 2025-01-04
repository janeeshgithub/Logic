

def egg_drop_recursive(k, n):
    if n == 0 or n == 1:
        return n
    if k == 1:
        return n

    min_drops = float('inf')
    for x in range(1, n + 1):
        drops = 1 + max(egg_drop_recursive(k - 1, x - 1), egg_drop_recursive(k, n - x))
        min_drops = min(min_drops, drops)

    return min_drops

def egg_drop_dp(k, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    # Base cases
    for i in range(1, k + 1):
        dp[i][0] = 0  # 0 floors need 0 drops
        dp[i][1] = 1  # 1 floor needs 1 drop
    for j in range(1, n + 1):
        dp[1][j] = j  # 1 egg needs j drops for j floors

    # Fill the DP table
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], res)

    return dp[k][n]
def egg_drop_optimized(k, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    for j in range(1, n + 1):
        dp[1][j] = j

    for i in range(2, k + 1):
        for j in range(2, n + 1):
            low, high = 1, j
            while low + 1 < high:
                mid = (low + high) // 2
                break_case = dp[i-1][mid-1]
                no_break_case = dp[i][j-mid]
                if break_case > no_break_case:
                    high = mid
                else:
                    low = mid

            dp[i][j] = 1 + min(
                max(dp[i-1][low-1], dp[i][j-low]),
                max(dp[i-1][high-1], dp[i][j-high])
            )

    return dp[k][n]
