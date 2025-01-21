class Solution:
    def findMinimumCoin(self, coins, N):
        coins.sort()  # Sort the coins to check them in increasing order
        current_sum = 0  # The current maximum sum we can form
        for coin in coins:
            if coin > current_sum + 1:
                # If coin is greater than current_sum + 1, we need coin (current_sum + 1)
                return current_sum + 1
            current_sum += coin  # Extend the range of sums we can form

        # If we can form all sums from 1 to N, return the next possible sum (current_sum + 1)
        return current_sum + 1


# Test the solution
coins = [1, 2, 5]
N = 11
solution = Solution()
print(solution.findMinimumCoin(coins, N))  # Output: 3
