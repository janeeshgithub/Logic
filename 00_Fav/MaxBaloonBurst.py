def maxCoins(nums):
    # Add boundary values (1) at both ends of the list
    nums = [1] + nums + [1]

    # Length of the array after padding
    n = len(nums)

    # dp[i][j] will store the maximum coins we can get by bursting balloons between i and j
    dp = [[0] * n for _ in range(n)]

    # Iterate over subarray lengths
    for length in range(2, n):  # length of subarray from 2 to n-1
        for i in range(n - length):  # Starting index of the subarray
            j = i + length  # Ending index of the subarray

            # Try each k as the last balloon to burst in the subarray (i, j)
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j],
                               nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

    # The answer is in dp[0][n-1], which represents bursting all balloons
    for i in dp:
        print(i)
    return dp[0][n - 1]


# Example usage
nums = [3, 1, 5, 8]
result = maxCoins(nums)
print(f"Maximum Coins: {result}")
