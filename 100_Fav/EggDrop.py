def egg_drop_recursive(eggs, floors):
    if floors == 0 or floors == 1:
        return floors
    if eggs == 1:  # Base case: 1 egg
        return floors
    min_drops = float('inf')
    for x in range(1, floors + 1):  # Try each floor
        drops = 1 + max(
            egg_drop_recursive(eggs - 1, x - 1),  # Egg breaks
            egg_drop_recursive(eggs, floors - x)  # Egg doesn't break
        )
        min_drops = min(min_drops, drops)
    return min_drops


def egg_drop_dp(eggs, floors):
    """
    Dynamic Programming solution to the egg drop problem.
    """
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]  # Create DP table

    # Base cases
    for i in range(1, eggs + 1):
        dp[i][0] = 0  # 0 floors need 0 drops
        dp[i][1] = 1  # 1 floor needs 1 drop
    for j in range(1, floors + 1):
        dp[1][j] = j  # 1 egg needs j drops for j floors

    # Fill the DP table
    for i in range(2, eggs + 1):  # For each egg
        for j in range(2, floors + 1):  # For each floor
            dp[i][j] = float('inf')
            for x in range(1, j + 1):  # Check each floor
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])  # Worst case
                dp[i][j] = min(dp[i][j], res)  # Minimize worst-case attempts

    return dp[eggs][floors]


def egg_drop_optimized(eggs, floors):
    """
    Optimized Dynamic Programming solution to the egg drop problem using binary search.
    """
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]  # Create DP table

    # Base cases
    for i in range(1, eggs + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    for j in range(1, floors + 1):
        dp[1][j] = j

    # Fill the DP table
    for i in range(2, eggs + 1):  # For each egg
        for j in range(2, floors + 1):  # For each floor
            low, high = 1, j
            while low + 1 < high:  # Binary search
                mid = (low + high) // 2
                breaks_case = dp[i - 1][mid - 1]
                no_breaks_case = dp[i][j - mid]
                if breaks_case > no_breaks_case:
                    high = mid
                else:
                    low = mid

            dp[i][j] = 1 + min(
                max(dp[i - 1][low - 1], dp[i][j - low]),
                max(dp[i - 1][high - 1], dp[i][j - high])
            )

    return dp[eggs][floors]


if __name__ == "__main__":
    eggs = 10
    floors = 100

    # Uncomment below to test the recursive approach (Warning: Very slow for large inputs)
    # print("Recursive:", egg_drop_recursive(eggs, floors))

    print("Dynamic Programming:", egg_drop_dp(eggs, floors))
    print("Optimized DP:", egg_drop_optimized(eggs, floors))
