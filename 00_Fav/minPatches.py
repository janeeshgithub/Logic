class Solution(object):
    def minPatches(self, nums, n):
        m = 1
        r = 0
        i = 0
        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1

            else:
                m += m
                r += 1
            print(m)
        print(r)

a=Solution()
a.minPatches([1,5,10],20)