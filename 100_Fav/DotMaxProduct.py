class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        a=len(nums1)
        b=len(nums2)
        dp=[[float('-inf')]*(a+1) for _ in range(b+1)]
        m=-1
        for i in range(1,b+1):
            for j in range(1,a+1):
                t=nums1[j-1]*nums2[i-1]
                dp[i][j] = max(dp[i - 1][j - 1] + t, t, dp[i][j - 1], dp[i - 1][j])
        return dp[b][a]

