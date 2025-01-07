def countOfPairs(self, A: List[int]) -> int:
    mod = 10 ** 9 + 7
    n, m = len(A), max(A) + 1
    dp, dp2 = [1] * m, [0] * m
    for i in range(1, n):
        d = max(0, A[i] - A[i - 1])
        for j in range(d, A[i] + 1):
            dp2[j] = (dp2[j - 1] + dp[j - d]) % mod
        dp, dp2 = dp2, [0] * m
    return sum(dp) % mod