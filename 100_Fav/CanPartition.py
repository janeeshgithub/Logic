class Solution:
    # 1. Bitmasking Approach
    def canPartition_bitmasking(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = 1 << 0  # A single integer to represent all subset sums

        for num in nums:
            dp |= dp << num  # Update dp to include new subset sums with `num`

        return (dp & (1 << target)) != 0

    # 2. 1D Dynamic Programming
    def canPartition_1D_DP(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: Subset sum of 0 is always achievable

        for num in nums:
            for j in range(target, num - 1, -1):  # Traverse backwards
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

    # 3. Set-Based Dynamic Programming
    def canPartition_set_based(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for num in nums:
            nextDP = set()
            for t in dp:
                if t + num == target:
                    return True
                nextDP.add(t + num)
                nextDP.add(t)
            dp = nextDP

        return False

    # 4. 2D Dynamic Programming
    def canPartition_2D_DP(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True  # Base case: Subset sum of 0 is always possible

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]


# Example Usage
if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    solution = Solution()

    # Uncomment the method you want to test
    print("Bitmasking:", solution.canPartition_bitmasking(nums))
    print("1D DP:", solution.canPartition_1D_DP(nums))
    print("Set-Based DP:", solution.canPartition_set_based(nums))
    print("2D DP:", solution.canPartition_2D_DP(nums))
