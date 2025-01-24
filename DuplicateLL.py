class Solution(object):
    def superEggDrop(self, eggs, floors):
        # Create DP table where dp[i][j] represents the minimum number of drops
        # needed for i eggs and j floors.
        dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

        # Base cases: when we have 1 egg
        for i in range(1, eggs + 1):
            dp[i][0] = 0  # 0 floors -> 0 drops
            dp[i][1] = 1  # 1 floor -> 1 drop
        for j in range(1, floors + 1):
            dp[1][j] = j  # With 1 egg, we need j drops for j floors (worst case)

        # Fill the DP table for more than 1 egg and more than 1 floor
        for i in range(2, eggs + 1):  # For each number of eggs from 2 to `eggs`
            for j in range(2, floors + 1):  # For each number of floors from 2 to `floors`
                low, high = 1, j  # Initialize binary search bounds

                # Binary search to find the floor to drop the egg from
                while low + 1 < high:  # When there's more than 1 floor to consider
                    mid = (low + high) // 2
                    breaks_case = dp[i - 1][mid - 1]  # Egg breaks
                    no_breaks_case = dp[i][j - mid]  # Egg does not break

                    # Minimize the maximum of the two cases
                    if breaks_case > no_breaks_case:
                        high = mid
                    else:
                        low = mid

                # Once binary search is complete, we compute the result
                dp[i][j] = 1 + min(
                    max(dp[i - 1][low - 1], dp[i][j - low]),  # Egg breaks (worst case)
                    max(dp[i - 1][high - 1], dp[i][j - high])  # Egg doesn't break (worst case)
                )

        # The answer is stored in dp[eggs][floors]
        for i in dp:
            print(i)
        return dp[eggs][floors]


# Main function
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Example input
    eggs = 3  # Number of eggs
    floors = 14  # Number of floors

    # Call the superEggDrop method to find the minimum number of drops
    result = solution.superEggDrop(eggs, floors)

    # Output the result
    print(f"The minimum number of drops required for {eggs} eggs and {floors} floors is: {result}")
