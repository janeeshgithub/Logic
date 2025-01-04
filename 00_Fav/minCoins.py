def minCoins(coins, amount):
    # Create a dp array where dp[i] will store the minimum number of coins required to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Loop through each amount from 1 to 'amount'
    for i in range(1, amount + 1):
        # Try every coin
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp)

    # If dp[amount] is still 'inf', it means it's not possible to make the amount
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
coins = [4,1,6]
amount = 11
result = minCoins(coins, amount)
print("Minimum coins required:", result)  # Output: 3 (5 + 5 + 1)
