nums=[4,1,2,3,4,5,6,5,4,3]
dp = [1] * len(nums)
for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)

